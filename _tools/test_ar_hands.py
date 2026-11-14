import asyncio
from playwright.async_api import async_playwright

URL = "http://127.0.0.1:8123/galeria-xr.html"


def check(label, condition, detail=""):
    print(("PASS " if condition else "FAIL ") + label + (f" · {detail}" if detail else ""), flush=True)
    if not condition:
        raise AssertionError(label + (f": {detail}" if detail else ""))


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="/usr/bin/chromium", args=[
            "--no-sandbox", "--use-gl=swiftshader", "--enable-unsafe-swiftshader",
            "--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream",
        ])
        context = await browser.new_context(viewport={"width": 1440, "height": 1000})
        page = await context.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        await page.goto(URL, wait_until="load")
        await page.wait_for_timeout(700)

        # In a browser without native WebXR AR, the primary CTA should open the camera overlay.
        await page.click("#tab-ar")
        await page.wait_for_function("document.querySelector('#arActivateBtn') && !document.querySelector('#arActivateBtn').disabled")
        button_text = await page.locator("#arActivateBtn").inner_text()
        await page.click("#arActivateBtn")
        await page.wait_for_function("document.querySelector('#arScreen').classList.contains('is-live')", timeout=15000)
        check("RA por cámara activable desde el botón principal", True, button_text)
        check("vista de cámara y modelo activa", await page.locator("#arScreenVideo").evaluate("el => !!el.srcObject && el.srcObject.active"))

        # Consent is requested before hand tracking; activation returns to the originating mode.
        await page.click("#arHandsBtn")
        check("solicita consentimiento antes de activar manos", await page.locator("#view-hands").is_visible() and not await page.locator("#handsConsent").is_checked())
        await page.check("#handsConsent")
        await page.click("#handsStartBtn")
        await page.wait_for_function("document.querySelector('#handsBadge').innerText.toLowerCase().includes('gestos en vivo')", timeout=60000)
        await page.wait_for_function("document.querySelector('#tab-ar').getAttribute('aria-selected') === 'true'", timeout=10000)
        await page.wait_for_function("document.querySelector('#arScreen').classList.contains('is-live') && document.querySelector('#handVideo').srcObject === document.querySelector('#arScreenVideo').srcObject", timeout=15000)
        check("el mismo flujo de cámara sirve a RA y MediaPipe", await page.locator("#arScreenVideo").evaluate("el => el.srcObject === document.querySelector('#handVideo').srcObject"))
        check("manos activas al regresar a RA", await page.locator("#arHandsBtn").get_attribute("aria-pressed") == "true")

        # Gesture tracking remains active while the VR room is opened and can be controlled there.
        await page.click("#tab-vr")
        await page.wait_for_function("document.querySelector('#vrScene')?.hasLoaded === true", timeout=60000)
        check("manos no se apagan al cambiar a RV", await page.locator("#vrHandsBtn").get_attribute("aria-pressed") == "true")
        check("la cámara de manos sigue viva en RV", await page.locator("#handVideo").evaluate("el => !!el.srcObject && el.srcObject.active"))
        check("sala RV disponible en pantalla", await page.locator("#vrScene").count() == 1)

        await page.click("#vrHandsBtn")
        await page.wait_for_function("document.querySelector('#vrHandsBtn').getAttribute('aria-pressed') === 'false'")
        check("el botón de RV puede apagar el seguimiento", await page.locator("#handVideo").evaluate("el => !el.srcObject"))
        await page.click("#vrHandsBtn")
        await page.wait_for_function("document.querySelector('#vrHandsBtn').getAttribute('aria-pressed') === 'true'", timeout=60000)
        check("el botón de RV puede activar manos tras consentimiento", True)
        await page.click("#vrHandsBtn")
        await page.wait_for_timeout(300)
        check("limpieza de cámara tras apagar manos", await page.locator("#handVideo").evaluate("el => !el.srcObject"))
        check("sin errores JavaScript", not errors, "; ".join(errors[:5]))

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
