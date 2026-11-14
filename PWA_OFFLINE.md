# FaunaXR sin conexión

FaunaXR es una PWA estática. El shell usa la caché `faunaxr-offline-v43`; los modelos descargados a petición se guardan por separado en `faunaxr-models-v1` y sobreviven a una actualización del shell.

## Preparación

Abre la app una vez con conexión bajo HTTPS o `localhost`. En la instalación, el service worker intenta guardar por separado la página, manifiesto, JSON educativo, iconos, miniaturas, hoja de estilos e ilustración de portada, bibliotecas locales, fuente A-Frame y decodificador Draco. Usa `Promise.allSettled`, de modo que un recurso aislado que falte no cancele la instalación.

No se precargan los 21 GLB ni los binarios/tarea de MediaPipe en el shell. MediaPipe se descarga y cachea oportunistamente cuando se usa por primera vez; sus errores no impiden navegar. Los GLB solo se guardan al pulsar **Descargar para uso sin conexión**, uno por uno. El progreso y el estado por animal aparecen en la galería como **Offline listo** o **Solo en línea**. Abrir un modelo mientras hay conexión no añade en secreto su GLB a la caché offline.

La descarga completa actual es de alrededor de **12,5 MiB** (21 archivos). El panel calcula el total desde los GLB incluidos y muestra la estimación de espacio disponible que expone el navegador, si la hay. Son cifras aproximadas: el navegador puede imponer cuota o eliminar almacenamiento bajo presión. Los modelos que fallen se enumeran para que puedas volver a intentar la descarga. Los GLB propios siguen guardados en IndexedDB y no forman parte de este botón.

## Estrategia

La navegación es de red primero con una copia cacheada de respaldo. Los recursos estáticos se sirven desde caché primero y se añaden al shell cuando se usan en línea. Las peticiones GET a GLB consultan solo `faunaxr-models-v1`; sin una copia descargada y sin red devuelven un mensaje 503 específico. Las respuestas parciales y de terceros no se cachean. Ya no existe lógica especial de `HEAD`/206 para audio de misiones.

El modo offline necesita que el service worker se haya registrado bajo HTTPS o `localhost`. Borrar datos del sitio elimina la caché y el almacenamiento local. El botón principal de RA ofrece superposición de cámara cuando no hay RA nativa; esta no ancla el modelo. El seguimiento de manos comparte el flujo de cámara con las vistas AR/RV en pantalla y se apaga al salir de esos modos o al ocultar la página. La sala RV visible en pantalla no equivale a verificar WebXR inmersivo con visor físico.

## Publicación HTTPS

La página está publicada en [GitHub Pages](https://frankdavidmarquezblanco4-cyber.github.io/fauna/galeria-xr.html#hands) desde la rama `main`. Después de actualizaciones del shell se usa `faunaxr-offline-v43`; al abrir la app en línea el navegador instala la caché nueva y conserva por separado los modelos ya descargados. Para verificar el modo sin conexión, abre la app con conexión, completa **Descargar para uso sin conexión** y prueba una recarga sin red.
