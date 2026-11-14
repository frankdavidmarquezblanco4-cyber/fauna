import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = "http://127.0.0.1:8123/galeria-xr.html"
FAILS = []


def check(name, condition, detail=""):
    print(("PASS " if condition else "FAIL ") + name + (f" · {detail}" if detail else ""))
    if not condition:
        FAILS.append(name)


async def unlock(page):
    await page.fill("#accessNickname", "Prueba")
    await page.select_option("#accessGrade", "6")
    await page.check("#accessConsent")
    await page.click("#accessSubmit")
    await page.wait_for_timeout(500)


async def duplicate_ids(page):
    return await page.evaluate("""() => Object.fromEntries(
      ['vrPlaceholder','vrPlaceholderText','vrFsExit'].map(id => [id, document.querySelectorAll(`[id=\\"${id}\\"]`).length])
    )""")


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="/usr/bin/chromium", args=[
            "--use-gl=swiftshader", "--enable-unsafe-swiftshader", "--no-sandbox",
            "--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"])
        context = await browser.new_context(viewport={"width": 1440, "height": 1000})
        page = await context.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        await page.goto(URL, wait_until="load")
        await page.wait_for_timeout(1000)
        await page.wait_for_function("window.SXR && typeof window.SXR.shuffleQuizOptions === 'function'")

        shuffled = await page.evaluate("""async () => {
          const source = await fetch('./assets/data/fauna-learning.es.json').then(r => r.json());
          const quiz = source.animals.find(a => a.id === 'gato').quizzes[0];
          const original = JSON.stringify(quiz);
          const results = Array.from({length: 100}, () => window.SXR.shuffleQuizOptions(quiz));
          return {
            sourceUnchanged: JSON.stringify(quiz) === original,
            allOptionsRetained: results.every(q => q.options.length === quiz.options.length && new Set(q.options).size === quiz.options.length && quiz.options.every(o => q.options.includes(o))),
            correctIndexRetained: results.every(q => q.correctIndex >= 0 && q.options[q.correctIndex] === quiz.options[quiz.correctIndex]),
            variedPositions: new Set(results.map(q => q.correctIndex)).size > 1
          };
        }""")
        check("barajado no muta el JSON fuente", shuffled["sourceUnchanged"])
        check("barajado conserva las tres opciones", shuffled["allOptionsRetained"])
        check("correctIndex acompaña la respuesta correcta", shuffled["correctIndexRetained"])
        check("posición correcta varía entre renderizados", shuffled["variedPositions"])

        await page.click("#tab-learn")
        await page.wait_for_function("document.querySelector('#learnStatus')?.textContent.includes('21 fichas')")
        await page.locator('[data-learn-card="gato"]').click()
        await page.wait_for_selector("#animalQuizForm .quiz-question")
        source = await page.evaluate("""async () => {
          const data = await fetch('./assets/data/fauna-learning.es.json').then(r => r.json());
          return data.animals.find(a => a.id === 'gato').quizzes[0];
        }""")
        options = await page.locator("#animalQuizForm .quiz-question").first.locator(".quiz-option span").all_inner_texts()
        correct_text = source["options"][source["correctIndex"]]
        correct_position = options.index(correct_text) if correct_text in options else -1
        source_url = await page.locator("#animalQuizForm .quiz-question").first.locator(".quiz-source a").get_attribute("href")
        check("pregunta renderizada conserva su opción correcta", correct_position >= 0)
        check("fuente enlazada continúa en la pregunta", source_url == source["sourceUrl"], source_url)
        if correct_position >= 0:
            await page.locator(f"#animalQuizOption0_{correct_position}").check()
            await page.locator("#animalQuizForm button[type='submit']").click()
            feedback = await page.locator("#animalQuizQuestionFeedback0").inner_text()
            check("corrección y explicación siguen alineadas", "¡Correcto!" in feedback and source["explanation"] in feedback, feedback)

        ids_initial = await duplicate_ids(page)
        check("IDs RV únicos antes de construir sala", all(count == 1 for count in ids_initial.values()), ids_initial)
        await page.click("#tab-vr")
        await page.wait_for_selector("#vrScene", timeout=30000)
        await page.wait_for_timeout(1000)
        ids_scene = await duplicate_ids(page)
        check("IDs RV únicos después de construir sala", all(count <= 1 for count in ids_scene.values()) and ids_scene["vrFsExit"] == 1, ids_scene)
        alt = await page.locator("#vrGrid").get_attribute("alt")
        aria_hidden = await page.locator("#vrGrid").get_attribute("aria-hidden")
        check("cuadrícula decorativa accesible", alt == "" and aria_hidden == "true")
        await page.locator("#vrFsExit").evaluate("button => button.click()")
        await page.wait_for_timeout(300)
        check("listener de salida RV responde", await page.locator("#vrFsExit").count() == 1)
        check("sin errores JavaScript", not errors, errors[:5])
        await context.close()
        await browser.close()

    print("FALLOS:", FAILS)
    raise SystemExit(1 if FAILS else 0)


asyncio.run(main())
