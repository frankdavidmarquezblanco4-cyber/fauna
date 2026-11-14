# Plan de FaunaXR

## Alcance actual

Mantener una PWA estática de aprendizaje animal que funcione en navegador moderno y pueda usar caché offline. El catálogo contiene 21 animales; los quizzes siguen en `assets/data/fauna-learning.es.json` y cada pregunta debe preservar su respuesta, explicación y fuente al barajar opciones en presentación.

La ficha educativa muestra diez preguntas autocorregibles con tres alternativas. Los modelos de la galería se comparten entre vista 3D, RA, RV y control gestual; las cargas GLB de cada persona permanecen en el navegador. El CTA de RA pasa al modo de cámara si no hay soporte nativo, y el mismo flujo de video da servicio a MediaPipe y a las vistas RA/RV en pantalla tras el consentimiento. No hay backend ni sincronización externa.

## Implementaciones incluidas

El quiz aplica Fisher–Yates al render y calcula el índice correcto en el objeto presentado sin editar el JSON. La sala virtual mantiene una instancia de cada ID del placeholder/salida y etiqueta la textura de suelo como decorativa. El zorro enumera y reproduce Survey, Walk y Run uno a uno, como solicita su ficha oficial.

Pato y zorro se verificaron contra las fichas primarias del repositorio Khronos glTF Sample Assets. Sus autorías, licencias, atribuciones y enlaces se muestran en catálogo/archivo local/README. El origen y licencia del GLB Scratch Cat no se encontraron en el ZIP; se documenta la incertidumbre y el riesgo de marca, sin presentar los términos generales de Scratch como licencia del GLB.

Los siete modelos grandes se optimizaron con glTF Transform, compresión Draco, texturas WebP a un máximo de 1024 px y validación glTF. Los decodificadores son locales. La versión `faunaxr-offline-v43` separa el shell tolerante a fallos de `faunaxr-models-v1`; el usuario decide descargar los 21 modelos, con progreso, estimación de espacio y distintivo por animal. MediaPipe se carga bajo demanda. La limpieza elimina referencias obsoletas de audio y servicios legacy de este paquete.

## Experiencia de inicio

La portada adopta la paleta azul/cian y la composición inmersiva de la referencia del usuario. El arte panorámico y la hoja `assets/landing.css` son recursos locales; el service worker los incluye en el shell para conservar la portada offline. La guía explica galería 3D, aprendizaje, RA, RV, gestos, modelos GLB y descarga offline. La sección «Acerca del creador» muestra la biografía proporcionada para Frank Marquez. Los botones del hero siguen abriendo las mismas pestañas existentes.

## Verificación

Las pruebas Playwright usan Chromium/SwiftShader y cámara simulada. Cubren portada, guía, biografía, galería, perfiles, subida GLB, apertura de modelos Draco, las tres animaciones Fox, operación del quiz, unicidad de IDs, registro/caché del service worker, carga offline y RA por cámara con seguimiento compartido de manos en RA/RV en pantalla. No verifican RA nativa ni sesión WebXR de visor físico.

## Dependencias, límites y siguientes pasos

Se mantienen recursos locales en `assets/vendor/`; no se añadió backend, servicio externo, ni dependencia de runtime por npm. El paquete está publicado en GitHub Pages desde `main`: https://frankdavidmarquezblanco4-cyber.github.io/fauna/galeria-xr.html#hands. Quedan pendientes las pruebas físicas de RA nativa y WebXR.

El puma queda pendiente hasta hallar un GLB con licencia verificable. La sustitución del gato Scratch por el candidato genérico CC0 se recomienda para redistribución pública/comercial, pero no se aplicó sin revisar el cambio visual. Las pruebas de hardware real quedan pendientes.
