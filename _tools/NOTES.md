# Notas técnicas de FaunaXR

`galeria-xr.html` es la página PWA principal. El catálogo contiene 21 modelos: gato, pato, zorro, cachorro, conejo, gallina, vaca, caballo, león, tigre blanco, lobo, elefante, jirafa, rinoceronte, panda, tiburón blanco, oso, cocodrilo, gorila, cebra y guepardo. Se usan las bibliotecas locales `model-viewer` 4.0.0, A-Frame 1.7.0 y MediaPipe Vision.

## Origen/licencias

Los 13 modelos salvajes son CC0 de Grab3D; la lista de archivos y URLs está en `assets/models/WILD-MODELS-LICENSES.txt`. Cachorro, conejo, gallina, vaca y caballo tienen avisos individuales en `assets/models/*-LICENSE.txt`. Duck es copyright © 2006 Sony bajo SCEA Shared Source License 1.0. Fox combina el modelo CC0 de PixelMannen con rig/animación de tomkranis y conversión glTF de @AsoboStudio/@scurest bajo CC BY 4.0. Los créditos completos están en `assets/models/DUCK-FOX-LICENSES.txt` y se reflejan en `MODELS`. El GLB Scratch Cat no identifica origen/licencia del archivo específico; los términos Scratch no lo sustituyen y Scratch Cat es una marca. Ver `assets/models/scratch-cat-LICENSE.txt`.

## Rendimiento y decodificadores

`Puppy.glb`, `wild-tiger.glb`, `wild-crocodile.glb`, `wild-cheetah.glb`, `wild-gorilla.glb`, `wild-giraffe.glb` y `wild-zebra.glb` se procesaron con glTF Transform 4.5.0: Draco, WebP y límite de textura 1024 × 1024. Los resultados validados se usan en el paquete. Decodificadores de navegador Draco de upstream Three.js/Google están en `assets/vendor/draco/` con Apache 2.0; el paquete no requiere instalación de npm al ejecutarse. Los GLB fuente originales se preservaron fuera del ZIP final.

## PWA/offline

`service-worker.js` usa `faunaxr-offline-v43` para shell y `faunaxr-models-v1` para los GLB bajo demanda. Los 21 modelos suman 13.13 MB decimales (12.52 MiB). La instalación usa `Promise.allSettled`; hoja de estilos e ilustración del hero se precargan, mientras los binarios y la tarea de MediaPipe se cachean al primer uso. El indicador de tarjetas consulta únicamente la caché de modelos. No hay branch de audio/HEAD/206.

## Pruebas y herramientas

La portada de miniaturas se genera con `_tools/poster.html` y `_tools/shoot.py` (Playwright/Chromium + SwiftShader). Ejecutar `python3 -m http.server 8123` y, desde la raíz, los scripts `python3 _tools/test_functional.py`, `test_gallery.py`, `test_ar_hands.py`, `test_profiles_offline.py` y `test_quiz_and_ids.py`. Los archivos de captura se escriben en `/tmp/faunaxr-test-output`, no en el paquete.
