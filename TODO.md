# Estado de FaunaXR

## Entregado
- [x] La página principal y el inicio PWA abren la Galería de animales; la marca visible y el manifiesto se llaman FaunaXR.
- [x] Iconos de instalación FaunaXR en tamaños 192 y 512 px, incluido icono maskable.
- [x] Catálogo ampliado a 21 animales; agrega 13 salvajes: león, tigre blanco, lobo, elefante, jirafa, rinoceronte, panda, tiburón blanco, oso, cocodrilo, gorila, cebra y guepardo.
- [x] Licencias CC0 1.0 y fuentes de modelos identificadas en las fichas y en `assets/models/WILD-MODELS-LICENSES.txt`.
- [x] La sección Mis modelos acepta GLB de hasta 60 MB y los guarda localmente.
- [x] La sala RV lista los 21 animales y los GLB propios; el selector de pantalla completa enfoca la estación seleccionada.
- [x] La RA por cámara deja seleccionar cualquier animal de la galería o GLB propio, y silencia los avisos superpuestos mientras proyecta el modelo.
- [x] La pestaña Aprende tiene teoría y fuentes enlazadas para cada animal del catálogo.
- [x] El JSON de aprendizaje está incluido en el app shell de la PWA para lectura offline.
- [x] La teoría del león africano incluye cinco datos curiosos, cada uno con fuente enlazada.

## Pendiente en esta actualización
- [ ] Cada uno de los 21 animales tiene exactamente diez preguntas autocorregibles, con tres opciones, explicación y fuente por pregunta. El lote de investigación aprobado solo completó cinco especies antes de detenerse por falta de créditos; no publicar el requisito como completo hasta cubrir las 21.
- [x] En RA móvil, ampliar la vista en vivo; mantener ocultas las notificaciones mientras la cámara está activa; detener la cámara al salir de RA y al pasar la página a segundo plano.
- [x] En RV, esperar a que la sala esté lista antes de habilitar la entrada, ocultar notificaciones durante pantalla completa, y conservar el selector completo usable en pantallas estrechas.

## Pendientes previos
- [ ] Añadir un puma/cougar si aparece un GLB redistribuible con licencia verificable.
- [ ] Publicar como sitio en hosting HTTPS; aún no hay despliegue web. HTTPS es necesario para cámara fuera de localhost.
- [ ] Probar la sesión WebXR inmersiva con un visor físico; el hardware no estuvo disponible para esta verificación.

## Privacidad
Los perfiles, favoritos y modelos propios persisten en el navegador/dispositivo local. El control de manos/cámara es opcional, requiere permiso del navegador y procesa video en el dispositivo.
