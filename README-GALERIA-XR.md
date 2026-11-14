# FaunaXR · Guía de galería

FaunaXR es una aplicación web progresiva instalable para explorar 21 animales y tus modelos GLB en 3D, RA, sala RV y control gestual opcional. Funciona sin cuenta; perfiles, favoritos y archivos propios permanecen en el dispositivo.

## Empezar e instalar

Prueba en local con `python3 -m http.server 8000` y abre `http://localhost:8000/`. La versión pública está disponible en [FaunaXR en GitHub Pages](https://frankdavidmarquezblanco4-cyber.github.io/fauna/galeria-xr.html#hands). Para instalarla en computadora, Android o iPhone/iPad, abre la dirección HTTPS y usa **Instalar app** o **Compartir → Agregar a pantalla de inicio**.

## Galería y modo sin conexión

Busca animales y filtra por categoría. **Aprende** ofrece teoría con fuentes y diez preguntas autocorregibles por animal; cada render baraja el orden de respuestas y conserva la respuesta correcta, su explicación y la fuente asociadas.

**Descargar para uso sin conexión** guarda los 21 modelos del catálogo uno a uno. La página avisa del tamaño y del espacio aproximado informado por el navegador, muestra una barra de progreso y etiqueta cada tarjeta como **Offline listo** o **Solo en línea**. La descarga completa actual ronda 12,5 MiB. Si un modelo falla, queda indicado para reintentar. La caché persiste entre actualizaciones normales de la app, aunque el navegador puede borrarla si necesita espacio.

## RA, RV y cámara

El botón **Ver en RA** intenta RA nativa cuando el navegador la anuncia; si no, abre **RA en pantalla**, una superposición GLB sobre la cámara que no detecta superficies ni ancla el modelo. Se requiere HTTPS o `localhost` y permiso explícito de cámara. **Activar manos** pide consentimiento por separado; la cámara se procesa localmente y se comparte entre el seguimiento y las vistas AR/RV en pantalla. Al salir de esos modos o esconder la página, se apaga. Pellizcar y arrastrar gira; dos manos acercan/alejan; los gestos de palma, puño, pulgar y barrido rotan, reinician, marcan favoritos o cambian de animal.

En **Sala RV**, **Pantalla completa** funciona como alternativa cuando no hay visor WebXR. Con manos activas, pellizcar mueve la mirada, dos manos ajustan el zoom, la palma abierta rota el animal y un barrido cambia de pedestal. Para inmersión WebXR hace falta un visor físico compatible; que el navegador permita cámara durante la sesión depende del dispositivo. En el zorro, Survey, Walk y Run se reproducen secuencialmente, uno a la vez.

## Licencias y datos

Las fichas de los modelos enlazan licencia y fuente cuando se conoce. Pato y zorro tienen créditos oficiales en `assets/models/DUCK-FOX-LICENSES.txt`. El gato Scratch del ZIP no lleva origen ni licencia específica del GLB, y Scratch Cat es marca registrada; revisa `assets/models/scratch-cat-LICENSE.txt`. Antes de redistribución pública/comercial se recomienda un gato genérico CC0 con procedencia comprobable. No se añadió un puma sin una descarga GLB y licencia verificables.

Los GLB propios y perfiles permanecen en el almacenamiento del mismo navegador; no se sincronizan entre dispositivos. Para cuota, cachés y guía de hosting HTTPS, consulta `PWA_OFFLINE.md`.
