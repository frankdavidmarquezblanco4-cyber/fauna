import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

URL = "http://127.0.0.1:8123/galeria-xr.html"
ROOT = Path(__file__).resolve().parents[1]
DUCK = str(ROOT / "assets/models/Duck.glb")
fails = []

def check(name, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + name + ((" · " + str(extra)) if extra else ""))
    if not cond:
        fails.append(name)

async def make_profile(page, name):
    if not await page.locator("#accessGate").is_visible():
        await page.click("#profileChip")
    await page.fill("#accessNickname", name)
    await page.select_option("#accessGrade", "6")
    await page.check("#accessConsent")
    await page.click("#accessSubmit")
    await page.wait_for_timeout(700)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="/usr/bin/chromium", args=[
            "--use-gl=swiftshader", "--enable-unsafe-swiftshader", "--no-sandbox",
            "--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"])
        ctx = await browser.new_context(viewport={"width": 1440, "height": 1000})
        page = await ctx.new_page()
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        await page.goto(URL, wait_until="load")
        await page.wait_for_timeout(1200)
        await make_profile(page, "Luna")
        await page.locator('[data-fav="gato"]').click()
        await page.wait_for_timeout(300)
        check("Luna favorito 1", (await page.locator("#statFav").inner_text()) == "1")

        # Switch profile
        await page.click("#changeProfileBtn")
        await page.wait_for_timeout(400)
        check("gate reabre", await page.locator("#accessGate").is_visible())
        check("gate se puede cerrar", not await page.locator("#gateCloseBtn").is_hidden())
        await page.click("#gateCloseBtn")
        await page.wait_for_timeout(300)
        check("gate cierra", not await page.locator("#accessGate").is_visible())
        await page.click("#changeProfileBtn")
        await page.wait_for_timeout(300)
        await make_profile(page, "Sol")
        await page.wait_for_timeout(500)
        check("perfil Sol", (await page.locator("#profileName").inner_text()) == "Sol")
        check("Sol sin favoritos", (await page.locator("#statFav").inner_text()) == "0")
        await page.click("#changeProfileBtn")
        await page.wait_for_timeout(400)
        check("dos perfiles guardados", await page.locator(".saved-profile").count() == 2)
        await page.locator(".saved-profile", has_text="Luna").click()
        await page.wait_for_timeout(500)
        check("vuelve a Luna", (await page.locator("#profileName").inner_text()) == "Luna")
        check("favorito de Luna", (await page.locator("#statFav").inner_text()) == "1")

        # Upload + delete
        await page.click("#tab-upload")
        await page.wait_for_timeout(300)
        await page.set_input_files("#fileInput", DUCK)
        await page.wait_for_timeout(2500)
        if await page.locator("#modelDialog").get_attribute("open") is not None:
            await page.click('[data-close-dialog="modelDialog"]')
        await page.wait_for_timeout(400)
        check("subida para borrar", await page.locator(".upload-item").count() == 1)
        await page.locator('[data-act="delete"]').click()
        await page.wait_for_timeout(300)
        check("confirmación borrado", await page.locator("#confirmDialog").get_attribute("open") is not None)
        await page.click("#confirmYes")
        await page.wait_for_timeout(900)
        check("borrado", await page.locator(".upload-item").count() == 0)
        check("galería vuelve a 21", await page.locator(".model-card").count() == 21)

        # Wipe all profiles in a separate context
        wctx = await browser.new_context(viewport={"width": 1200, "height": 900})
        wp = await wctx.new_page()
        await wp.goto(URL, wait_until="load")
        await wp.wait_for_timeout(1000)
        await make_profile(wp, "Test")
        await wp.click("#changeProfileBtn")
        await wp.wait_for_timeout(300)
        await wp.click("#wipeProfilesBtn")
        await wp.wait_for_timeout(300)
        await wp.click("#confirmYes")
        await wp.wait_for_timeout(1200)
        check("borrar perfiles vuelve a modo invitado", not await wp.locator("#accessGate").is_visible() and await wp.locator("#profileChip").is_visible())
        await wctx.close()

        # Offline test: shell v43 includes the landing art; GLBs are separate and user-triggered.
        await page.click("#tab-gallery")
        await page.evaluate("navigator.serviceWorker.ready")
        await page.wait_for_timeout(800)
        cache_state = await page.evaluate("""async () => {
          const names = await caches.keys();
          const models = await caches.open('faunaxr-models-v1');
          const shell = await caches.open('faunaxr-offline-v43');
          const puppy = await models.match(new URL('./assets/models/Puppy.glb', location.href).href);
          const landingCss = await shell.match(new URL('./assets/landing.css', location.href).href);
          const heroImage = await shell.match(new URL('./assets/landing/faunaxr-hero.webp', location.href).href);
          return {shell: names.includes('faunaxr-offline-v43'), modelCache: names.includes('faunaxr-models-v1'), puppyInitiallyCached: !!puppy, landingCss: !!landingCss, heroImage: !!heroImage};
        }""")
        check("service worker shell v43", cache_state["shell"], cache_state)
        check("portada cacheada para uso sin conexión", cache_state["landingCss"] and cache_state["heroImage"], cache_state)
        check("GLB no se precarga sin pedirlo", not cache_state["puppyInitiallyCached"], cache_state)
        await page.click("#downloadOfflineModelsBtn")
        await page.wait_for_function("document.querySelector('#offlineModelStatus').textContent.includes('Descarga completa')", timeout=60000)
        model_count = await page.evaluate("""async () => (await (await caches.open('faunaxr-models-v1')).keys()).filter(r => new URL(r.url).pathname.toLowerCase().endsWith('.glb')).length""")
        check("descarga offline de 21 modelos", model_count == 21, model_count)
        check("estado offline en cada tarjeta", await page.locator('.offline-state.ready').count() == 21)
        await page.reload(wait_until="domcontentloaded")
        await page.wait_for_timeout(1500)
        await ctx.set_offline(True)
        try:
            await page.reload(wait_until="domcontentloaded", timeout=30000)
            await page.wait_for_timeout(1500)
            check("offline carga la página", "FAUNAXR" in (await page.title()).upper())
            check("offline conserva perfil", not await page.locator("#accessGate").is_visible())
        except Exception as e:
            check("offline carga la página", False, e)
        await ctx.set_offline(False)
        # Chromium in this emulated environment can emit a stackless platform denial.
        permission_denials = [error for error in errors if error.strip() == "The request was denied."]
        unexpected_errors = [error for error in errors if error not in permission_denials]
        check("sin errores JS inesperados", len(unexpected_errors) == 0, {"errores": unexpected_errors[:5], "rechazos del navegador": len(permission_denials)})
        await ctx.close()
        await browser.close()

    print("FALLOS:", fails)
    raise SystemExit(1 if fails else 0)

asyncio.run(main())
