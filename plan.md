# Plan — FaunaXR: aprendizaje, RA y RV

## Alcance

En el repositorio público independiente `frankdavidmarquezblanco4-cyber/fauna`, ampliar la experiencia instalada existente. `scratchxr-lab` queda fuera de alcance. La sala RV debe listar todos los animales y los GLB subidos en el selector de pantalla completa; el modo RA por cámara debe permitir elegir cualquiera de esos modelos y evitar notificaciones que tapen la proyección; el apartado educativo debe ofrecer teoría breve y al menos un quiz por cada animal de catálogo. La ficha del león añadirá datos curiosos con fuentes y un quiz de varias preguntas autocorregible.

## Implementación y estructura

- `galeria-xr.html` conserva la PWA estática y su navegación por pestañas. Añadir una pestaña educativa con fichas seleccionables, teoría, referencia consultada y quiz autocorregible de tres alternativas. Los 21 IDs nativos siguen alineados con `MODELS`.
- `assets/data/fauna-learning.es.json` mantiene el contenido educativo separado del markup y apto para precarga offline; en el león guarda curiosidades con fuente por hecho y seis preguntas con explicación.
- `service-worker.js` precarga el JSON y aumenta la versión de caché para que los clientes instalados reciban los cambios.
- El selector RA y la lista del visor usan `allModels()`, que combina animales incluidos y GLB personales guardados en IndexedDB. La RA por cámara recibe su propia lista compacta dentro del visor; notificaciones globales se silencian mientras la proyección está activa.
- `README-GALERIA-XR.md` describe las limitaciones de RA por cámara y el uso del apartado educativo.

## Diseño

Se reutiliza la identidad actual FaunaXR: museo natural-científico con acentos turquesa/cian, tarjetas claras, tipografía y controles existentes. Las fichas educativas priorizan lectura breve y respuestas grandes para móvil. El panel de cámara permanece visualmente limpio; controles compactos quedan en bordes para no cubrir el modelo.

## Dependencias y restricciones

No se agrega backend ni servicio externo. La teoría usa fuentes institucionales enlazadas y viaja con la PWA para uso offline. El modo de RA superpuesto necesita permiso de cámara y contexto HTTPS; no hace anclaje espacial, a diferencia de RA nativa compatible. Los archivos GLB de usuario siguen siendo locales al navegador. La publicación del código se limita a `fauna`.
