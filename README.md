# FaunaXR

FaunaXR es una PWA estática para explorar 21 animales, aprender con sus quizzes y abrir modelos en 3D, realidad aumentada o sala virtual. Admite modelos GLB propios; perfiles, favoritos y cargas permanecen en el navegador. No necesita backend.

## Abrir localmente

Desde la raíz del paquete ejecuta `python3 -m http.server 8000` y abre `http://localhost:8000/` o `http://localhost:8000/galeria-xr.html`. Conserva las rutas relativas del proyecto. El acceso a cámara y el service worker requieren HTTPS o `localhost`.

## Catálogo, licencias y rendimiento

El catálogo contiene ocho animales domésticos/de granja y 13 salvajes. Los modelos salvajes de Grab3D están publicados como CC0 1.0; las fichas y los GLB fuente se enumeran en `assets/models/WILD-MODELS-LICENSES.txt`. Se mantienen los avisos de licencia originales de los modelos domésticos.

`Duck.glb` proviene del conjunto oficial Khronos glTF Sample Assets: © 2006 Sony (crédito de Khronos: “Sony for Everything”), bajo SCEA Shared Source License 1.0. `Fox.glb` proviene del mismo repositorio: el modelo de PixelMannen es CC0 1.0; rig/animación de tomkranis y conversión glTF de @AsoboStudio/@scurest son CC BY 4.0 y requieren atribución. Fuentes, textos legales y créditos están en `assets/models/DUCK-FOX-LICENSES.txt` y también en el catálogo.

El GLB `scratch-cat.glb` no identifica en el ZIP su fuente 3D ni una licencia del archivo; los términos Scratch no prueban los derechos de ese modelo específico. Scratch Cat es además una marca registrada. Recomiendo cambiarlo por un gato genérico CC0 antes de redistribución pública/comercial. Alternativa concreta: “Standing cat”, modelo original de Innerscene, ficha CC0 y descarga GLB de 4,7 MB: [Innerscene](https://www.innerscene.com/tools/library/3d-parts/standing-cat-cda42538). No se sustituyó en este paquete para no cambiar el aspecto de la colección sin tu aprobación.

Los siete modelos de más de 4 MB se optimizaron con glTF Transform: texturas WebP hasta 1024 × 1024 y mallas Draco. El paquete incluye decodificadores Draco locales para `<model-viewer>` y A-Frame. Los 21 GLB actuales suman aproximadamente 12,5 MiB; los archivos fuente originales de los siete modelos optimizados se conservaron fuera del ZIP final.

El puma sigue pendiente: no se añadió ningún modelo sin GLB y licencia verificables.

## Uso y límites

En **Aprende**, cada animal tiene diez preguntas autocorregibles de tres opciones; el orden se baraja al mostrar cada quiz sin modificar el JSON fuente. La explicación y la fuente permanecen ligadas a la pregunta original.

En **Galería**, pulsa **Descargar para uso sin conexión** para guardar los 21 GLB localmente. El panel informa el progreso y la estimación de espacio; cada ficha indica si el modelo quedó disponible offline. Consulta [PWA_OFFLINE.md](PWA_OFFLINE.md) para detalles.

La RA nativa y WebXR inmersivo requieren navegador/dispositivo compatible y no pudieron verificarse en hardware real. La RA por cámara no ancla el modelo a una superficie. El despliegue HTTPS no se realizó; `PWA_OFFLINE.md` incluye pasos de preparación para hosting estático, sin publicar ni conectar un servicio.

## Pruebas

Con el servidor local en puerto 8123, ejecuta desde la raíz:

```bash
python3 _tools/test_functional.py
python3 _tools/test_gallery.py
python3 _tools/test_profiles_offline.py
python3 _tools/test_quiz_and_ids.py
```

Los scripts usan Playwright/Chromium con SwiftShader y cámara simulada; sus resultados no sustituyen las pruebas WebXR/RA nativa en dispositivos físicos. Valida el manifiesto con `python3 -m json.tool manifest.webmanifest`.

## Archivos principales

- `galeria-xr.html`: catálogo, quizzes, visores, cámara, perfiles y descarga offline.
- `service-worker.js`: shell `faunaxr-offline-v41` y caché separada de modelos.
- `assets/data/fauna-learning.es.json`: teoría, fuentes y quizzes.
- `assets/models/`: GLB, miniaturas y avisos de licencia.
- `assets/vendor/draco/`: decodificadores locales con licencia Apache 2.0.
- `PWA_OFFLINE.md`: instalación, cachés y pasos de despliegue manual.
