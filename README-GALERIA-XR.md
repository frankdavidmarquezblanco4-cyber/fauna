# FaunaXR · Galería de animales 3D

FaunaXR es una aplicación web progresiva instalable para explorar animales domésticos y salvajes. Abre directamente sin registro; los perfiles locales son opcionales. Incluye favoritos, búsqueda, visores 3D, realidad aumentada, sala de RV, controles gestuales opcionales con cámara y carga de modelos GLB personales.

## Instalación como app

Sirve o publica la carpeta completa en HTTPS. En computadora, pulsa **Instalar app** en el encabezado si el navegador ofrece instalación. En Android, Chrome → menú ⋮ → **Instalar app** o **Agregar a pantalla principal**. En iPhone/iPad, abre FaunaXR en Safari → Compartir → **Agregar a pantalla de inicio**. Para probar en local, ejecuta `python3 -m http.server 8000` y abre `http://localhost:8000/`.

## Colección y permisos

La colección incorpora animales de casa y granja además de 13 especies salvajes: león, tigre blanco, lobo, elefante, jirafa, rinoceronte, panda, tiburón blanco, oso, cocodrilo, gorila, cebra y guepardo. Los nuevos modelos se redistribuyen bajo CC0 1.0; la lista de fuentes figura en `assets/models/WILD-MODELS-LICENSES.txt`. No se incluyó puma porque no quedó confirmada una descarga GLB redistribuible con licencia verificable.

## Controles de RV

En **Sala RV**, al entrar en **Pantalla completa**, usa los controles integrados: **Anterior**, el selector **Animal al frente** y **Siguiente**. También aparecen si el navegador no permite la pantalla completa nativa y se ajustan a pantallas estrechas. Cambiar de animal elimina los avisos superpuestos; además, no aparecen avisos durante la pantalla completa ni las sesiones inmersivas. En visor WebXR, los botones virtuales **ANTERIOR** y **SIGUIENTE** están frente a la cámara; apunta y pulsa con el controlador. Los pedestales también se pueden seleccionar con el puntero/control.

El selector incluye las 21 especies de la galería y los diseños GLB cargados en **Mis modelos**. Si agregas o borras un GLB, la sala se reconstruye con la colección actual al volver a ella.

## Aprende

La pestaña **Aprende** contiene teoría, fuentes enlazadas y un quiz autocorregible de diez preguntas para cada uno de los 21 animales. Cada pregunta ofrece tres opciones, explicación al responder y un enlace a su fuente. La ficha del león añade cinco datos curiosos. El contenido está guardado en `assets/data/fauna-learning.es.json` y se incluye en la caché offline.

## Realidad aumentada con cámara

Desde una tarjeta de la galería o un modelo propio, pulsa **RA** para abrir la cámara y proyectar el diseño seleccionado. El selector dentro de la vista permite cambiar entre animales y GLB propios mientras la cámara está activa. En móviles, la vista en vivo ocupa más altura para que el modelo se vea con mayor claridad; los avisos se silencian. Al salir de RA, cambiar de pestaña o enviar la app a segundo plano, la cámara se detiene. Este modo superpone el diseño a la imagen de cámara, pero no lo ancla espacialmente; requiere permiso de cámara y HTTPS o `localhost`.

## Modelos propios y privacidad

En **Mis modelos**, sube GLB de hasta 60 MB; la página valida el archivo y guarda sus datos en IndexedDB del mismo navegador. Puedes explorar y guardar favoritos sin crear perfil; los perfiles y datos locales no se suben ni sincronizan. La cámara requiere HTTPS o localhost y permiso del navegador; el video de control gestual se procesa localmente.

## Licencias y estructura

Los modelos salvajes descargados de Grab3D tienen licencia CC0 1.0, indicada en sus páginas y catalogada en `assets/models/WILD-MODELS-LICENSES.txt`. Se conserva la atribución por trazabilidad. El pato y el zorro que ya venían en el ZIP tienen origen/licencia por verificar antes de redistribuirse por separado; sus fichas lo indican. El gato conserva sus términos de uso originales. El proyecto incluye bibliotecas locales A-Frame, model-viewer y MediaPipe con sus avisos de licencia.
