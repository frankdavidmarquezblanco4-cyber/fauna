# FaunaXR · Guía de galería

FaunaXR es una aplicación web progresiva instalable para explorar 21 animales y tus modelos GLB en 3D, RA, sala RV y control gestual opcional. Funciona sin cuenta; perfiles, favoritos y archivos propios permanecen en el dispositivo.

## Empezar e instalar

Prueba en local con `python3 -m http.server 8000` y abre `http://localhost:8000/`. Para instalarla en computadora, Android o iPhone/iPad, publica primero en HTTPS y usa la opción **Instalar app** del navegador o **Compartir → Agregar a pantalla de inicio**. No hay publicación activa asociada a este paquete.

## Galería y modo sin conexión

Busca animales y filtra por categoría. **Aprende** ofrece teoría con fuentes y diez preguntas autocorregibles por animal; cada render baraja el orden de respuestas y conserva la respuesta correcta, su explicación y la fuente asociadas.

**Descargar para uso sin conexión** guarda los 21 modelos del catálogo uno a uno. La página avisa del tamaño y del espacio aproximado informado por el navegador, muestra una barra de progreso y etiqueta cada tarjeta como **Offline listo** o **Solo en línea**. La descarga completa actual ronda 12,5 MiB. Si un modelo falla, queda indicado para reintentar. La caché persiste entre actualizaciones normales de la app, aunque el navegador puede borrarla si necesita espacio.

## RA, RV y cámara

En RA nativa, la colocación espacial depende de un dispositivo y navegador compatibles. **RA en pantalla** superpone el modelo a la imagen de cámara, pero no lo ancla a una superficie. Se requiere permiso de cámara y HTTPS o `localhost`; al salir o cambiar de pestaña, se detiene el video. El control de manos es opcional y procesa la cámara localmente.

En **Sala RV**, **Pantalla completa** funciona como alternativa cuando no hay visor WebXR. Para inmersión WebXR hace falta un visor físico compatible. En el zorro, los ciclos Survey, Walk y Run se reproducen secuencialmente en los visores; cada clip se ejecuta de a uno, como recomienda la ficha Khronos.

## Licencias y datos

Las fichas de los modelos enlazan licencia y fuente cuando se conoce. Pato y zorro tienen créditos oficiales en `assets/models/DUCK-FOX-LICENSES.txt`. El gato Scratch del ZIP no lleva origen ni licencia específica del GLB, y Scratch Cat es marca registrada; revisa `assets/models/scratch-cat-LICENSE.txt`. Antes de redistribución pública/comercial se recomienda un gato genérico CC0 con procedencia comprobable. No se añadió un puma sin una descarga GLB y licencia verificables.

Los GLB propios y perfiles permanecen en el almacenamiento del mismo navegador; no se sincronizan entre dispositivos. Para cuota, cachés y guía de hosting HTTPS, consulta `PWA_OFFLINE.md`.
