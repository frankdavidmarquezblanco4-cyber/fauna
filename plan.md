# Plan — FaunaXR: aprendizaje, RA y RV

## Alcance

En el repositorio público independiente `frankdavidmarquezblanco4-cyber/fauna`, ampliar la experiencia instalada existente. `scratchxr-lab` queda fuera de alcance. Cada animal del catálogo debe tener un quiz autocorregible de exactamente diez preguntas, con tres opciones, explicación y fuente. Para las 16 fichas restantes, redactar preguntas solo a partir de su teoría, hechos curiosos, pregunta existente y fuente ya incluida; no añadir afirmaciones externas ni hacer pasar el fallback por investigación independiente. En RA, dar más espacio al modelo proyectado en móviles, ocultar notificaciones mientras está activa la cámara y liberar la cámara al salir o al ocultar la página. En RV, conservar el selector de diseños en pantalla completa, ocultar toasts durante pantalla completa o sesión inmersiva y hacer que los controles se acomoden al viewport.

## Implementación y estructura

- `galeria-xr.html` conserva la PWA estática y su navegación por pestañas. La pestaña educativa presenta fichas seleccionables, teoría, referencias y exactamente diez preguntas autocorregibles de tres alternativas por animal; cada respuesta incluye explicación y una fuente enlazada. Los 21 IDs nativos siguen alineados con `MODELS`.
- `assets/data/fauna-learning.es.json` mantiene el contenido educativo separado del markup y apto para precarga offline; cada uno de los 21 animales lleva diez preguntas. Las cinco fichas ya investigadas conservan sus fuentes individuales; las restantes solo citan la fuente ya asociada a su teoría. El león conserva cinco curiosidades con sus fuentes.
- `service-worker.js` precarga el JSON y aumenta la versión de caché para que los clientes instalados reciban los cambios.
- El selector RA y la lista del visor usan `allModels()`, que combina animales incluidos y GLB personales guardados en IndexedDB. La RA por cámara recibe su propia lista compacta; la vista en vivo aprovecha más alto de pantalla en móvil, no muestra toasts y detiene el stream al abandonar la vista o pasar la app a segundo plano. RV mantiene su lista desplegable, oculta toasts mientras está inmersiva o a pantalla completa y ajusta los controles a móviles.
- `README-GALERIA-XR.md` describe las limitaciones de RA por cámara y el uso del apartado educativo.

## Diseño

Se reutiliza la identidad actual FaunaXR: museo natural-científico con acentos turquesa/cian, tarjetas claras, tipografía y controles existentes. Las fichas educativas priorizan lectura breve y respuestas grandes para móvil. El panel de cámara permanece visualmente limpio; controles compactos quedan en bordes para no cubrir el modelo.

## Dependencias y restricciones

No se agrega backend ni servicio externo. La teoría usa fuentes institucionales enlazadas y viaja con la PWA para uso offline. El modo de RA superpuesto necesita permiso de cámara y contexto HTTPS; no hace anclaje espacial, a diferencia de RA nativa compatible. Los archivos GLB de usuario siguen siendo locales al navegador. La publicación del código se limita a `fauna`.
