# Estado de FaunaXR

## Completado en este paquete

- Catálogo de 21 animales; galería, perfiles locales, RA/RV, quizzes y cargas GLB.
- Barajado Fisher–Yates del quiz en cada render sin cambiar `fauna-learning.es.json`; `correctIndex` se recalcula y se mantienen explicación/fuente.
- IDs únicos para el marcador de RV, texto y salida; textura de cuadrícula declarada decorativa con `alt=""` y `aria-hidden`.
- Créditos comprobados de Duck y Fox de Khronos en el catálogo, archivos de licencia y README; tres animaciones de Fox usadas secuencialmente en los visores.
- Nota explícita del GLB Scratch Cat: la fuente/licencia exacta no está en el ZIP, Scratch Cat es marca registrada; candidato genérico CC0 documentado sin sustitución no aprobada.
- Siete GLB mayores de 4 MB optimizados a Draco/WebP, con texturas limitadas a 1024 × 1024; decodificadores locales y archivos originales preservados fuera del paquete.
- Service worker `faunaxr-offline-v41`: instalación tolerante a fallos, MediaPipe bajo demanda, botón de descarga offline para los 21 modelos, progreso, estimación de espacio y estado por animal; retirado el manejo de audio.
- Etiquetas Open Graph/Twitter y depuración de archivos obsoletos del ZIP final.
- Documentación coherente en README, guía offline, galería, plan y notas técnicas.

## Pendiente

- Incorporar puma solo cuando haya un GLB con licencia verificable y apto para redistribución. No se inventó ni añadió un modelo.
- Publicar manualmente en hosting HTTPS; el README y `PWA_OFFLINE.md` solo preparan los pasos. No se realizó despliegue.
- Probar RA nativa en un móvil real y WebXR inmersivo con visor físico; el navegador de pruebas no sustituye ese hardware.

## Privacidad

Perfiles, favoritos y GLB propios permanecen en almacenamiento local. El video del control gestual se procesa en el dispositivo y requiere permiso explícito de cámara.
