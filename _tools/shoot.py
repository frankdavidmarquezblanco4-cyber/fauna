import asyncio
from pathlib import Path
from urllib.parse import urlencode
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
BASE = "http://127.0.0.1:8123"
MODELS = [
    ("scratch-cat", "scratch-cat.glb", "Gato", "30deg 70deg 106%"),
    ("dog", "Puppy.glb", "Cachorro", "30deg 68deg auto"),
    ("rabbit", "LowPolyRabbit.glb", "Conejo", "25deg 70deg auto"),
    ("chicken", "LowPolyChicken.glb", "Gallina", "30deg 70deg auto"),
    ("cow", "LowPolyCow.glb", "Vaca", "30deg 70deg auto"),
    ("horse", "LowPolyHorse.glb", "Caballo", "30deg 70deg auto"),
    ("duck", "Duck.glb", "Pato", "30deg 70deg auto"),
    ("fox", "Fox.glb", "Zorro", "30deg 70deg auto"),
    ("wild-lion", "wild-lion.glb", "León", "30deg 70deg auto"),
    ("wild-tiger", "wild-tiger.glb", "Tigre blanco", "30deg 70deg auto"),
    ("wild-wolf", "wild-wolf.glb", "Lobo", "30deg 70deg auto"),
    ("wild-elephant", "wild-elephant.glb", "Elefante", "30deg 70deg auto"),
    ("wild-giraffe", "wild-giraffe.glb", "Jirafa", "30deg 70deg auto"),
    ("wild-rhino", "wild-rhino.glb", "Rinoceronte", "30deg 70deg auto"),
    ("wild-panda", "wild-panda.glb", "Panda", "30deg 70deg auto"),
    ("wild-shark", "wild-shark.glb", "Tiburón blanco", "30deg 70deg auto"),
    ("wild-bear", "wild-bear.glb", "Oso", "30deg 70deg auto"),
    ("wild-crocodile", "wild-crocodile.glb", "Cocodrilo", "30deg 70deg auto"),
    ("wild-gorilla", "wild-gorilla.glb", "Gorila", "30deg 70deg auto"),
    ("wild-zebra", "wild-zebra.glb", "Cebra", "30deg 70deg auto"),
    ("wild-cheetah", "wild-cheetah.glb", "Guepardo", "30deg 70deg auto"),
]


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="/usr/bin/chromium", args=[
            "--use-gl=swiftshader", "--enable-unsafe-swiftshader", "--no-sandbox"
        ])
        page = await browser.new_page(viewport={"width": 1000, "height": 750}, device_scale_factor=1.5)
        for key, filename, name, orbit in MODELS:
            query = urlencode({"src": f"/assets/models/{filename}", "name": name, "orbit": orbit})
            await page.goto(f"{BASE}/_tools/poster.html?{query}", wait_until="load")
            try:
                await page.wait_for_function("window.__ready === true || window.__error", timeout=90000)
            except Exception as error:
                print("timeout", key, error)
            error = await page.evaluate("window.__error")
            if error:
                print("error", key, error)
                continue
            await page.wait_for_timeout(1200)
            output = ROOT / "assets" / "models" / f"{key}.webp"
            await page.locator("#stage").screenshot(path=str(output), type="webp", quality=86)
            print("ok", key)
        await browser.close()


asyncio.run(main())
