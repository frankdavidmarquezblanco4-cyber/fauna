# FaunaXR sin conexión (PWA)

## Uso inicial

La instalación y la primera preparación requieren conexión. Abre FaunaXR bajo HTTPS (o `http://localhost`), espera a que aparezca **Modo sin conexión preparado** y luego instala desde el navegador. En Chrome/Edge se puede usar **Instalar app**; en Safari/iPadOS, **Compartir → Añadir a pantalla de inicio**. La galería se puede explorar sin crear perfil; los perfiles son opcionales. El navegador puede solicitar permiso de almacenamiento.

## Qué funciona offline

- Galería, fichas de animales, búsqueda y preferencias locales.
- Favoritos y visitas guardados en el dispositivo incluso sin crear perfil.
- Las teorías y quizzes de los 21 animales, incluidos en la caché inicial de la PWA.
- Modelos y miniaturas que ya se hayan descargado o abierto previamente.
- Sala de RV en pantalla; la sesión inmersiva necesita un visor y WebXR compatible.
- Control de manos cuando MediaPipe y la cámara están disponibles. El video se procesa localmente y no se graba ni se envía.

## Qué requiere conexión o compatibilidad

- La instalación y la preparación inicial de la PWA.
- Descargar una versión nueva del sitio o modelos remotos que aún no estén en caché.
- La RA nativa necesita un navegador/dispositivo compatible (por ejemplo, Chrome Android con ARCore o Safari en dispositivos Apple). **RA en pantalla** usa la cámara como alternativa, pero no ancla el modelo a una superficie.
- RV inmersiva requiere HTTPS, un navegador con WebXR y un visor compatible. Sin esos elementos sigue disponible la sala en pantalla completa con controles.

El sitio es una PWA estática: no crea solicitudes de aula, no consulta decisiones docentes y no sincroniza perfiles, favoritos, avances ni modelos con Supabase.

El uso de cámara es opcional y siempre depende del permiso del navegador. Para RA en pantalla o control de manos se necesita HTTPS (localhost también es contexto seguro). Si el permiso se deniega, habilítalo en los ajustes del sitio; cierra otras apps que estén usando la cámara y vuelve a intentarlo. Sin cámara se puede usar ratón, teclado o pantalla táctil.

## Publicación y actualización

Publica en la raíz `index.html`, `manifest.webmanifest`, `service-worker.js`, `assets/` y los demás archivos, conservando las rutas relativas. GitHub Pages con HTTPS y otros servidores HTTPS son válidos; `file://` no admite service workers. El app shell actual usa `faunaxr-offline-v35`. Al cambiar recursos precargados, incrementa `CACHE_NAME`; al activarse, el service worker elimina sus cachés anteriores sin borrar `localStorage` ni los datos locales del usuario.

## Privacidad y almacenamiento

La caché PWA contiene archivos de aplicación y modelos, no perfiles ni respuestas de APIs. El estado y los modelos subidos se guardan en el almacenamiento local del navegador y no se comparten automáticamente entre dispositivos. En equipos compartidos, si creas un perfil, evita introducir información que identifique a menores. Borrar los datos del sitio elimina perfiles, modelos subidos y preferencias locales de ese navegador.
