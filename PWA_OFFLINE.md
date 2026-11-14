# FaunaXR sin conexión

FaunaXR es una PWA estática. El shell usa la caché `faunaxr-offline-v41`; los modelos descargados a petición se guardan por separado en `faunaxr-models-v1` y sobreviven a una actualización del shell.

## Preparación

Abre la app una vez con conexión bajo HTTPS o `localhost`. En la instalación, el service worker intenta guardar por separado la página, manifiesto, JSON educativo, iconos, miniaturas, bibliotecas locales, fuente A-Frame y decodificador Draco. Usa `Promise.allSettled`, de modo que un recurso aislado que falte no cancele la instalación.

No se precargan los 21 GLB ni los binarios/tarea de MediaPipe en el shell. MediaPipe se descarga y cachea oportunistamente cuando se usa por primera vez; sus errores no impiden navegar. Los GLB solo se guardan al pulsar **Descargar para uso sin conexión**, uno por uno. El progreso y el estado por animal aparecen en la galería como **Offline listo** o **Solo en línea**. Abrir un modelo mientras hay conexión no añade en secreto su GLB a la caché offline.

La descarga completa actual es de alrededor de **12,5 MiB** (21 archivos). El panel calcula el total desde los GLB incluidos y muestra la estimación de espacio disponible que expone el navegador, si la hay. Son cifras aproximadas: el navegador puede imponer cuota o eliminar almacenamiento bajo presión. Los modelos que fallen se enumeran para que puedas volver a intentar la descarga. Los GLB propios siguen guardados en IndexedDB y no forman parte de este botón.

## Estrategia

La navegación es de red primero con una copia cacheada de respaldo. Los recursos estáticos se sirven desde caché primero y se añaden al shell cuando se usan en línea. Las peticiones GET a GLB consultan solo `faunaxr-models-v1`; sin una copia descargada y sin red devuelven un mensaje 503 específico. Las respuestas parciales y de terceros no se cachean. Ya no existe lógica especial de `HEAD`/206 para audio de misiones.

El modo offline necesita que el service worker se haya registrado bajo HTTPS o `localhost`. Borrar datos del sitio elimina la caché y el almacenamiento local. La RA nativa necesita además soporte del dispositivo; la sala RV visible en pantalla no equivale a verificar WebXR inmersivo con visor físico.

## Preparación de hosting HTTPS (todavía no publicado)

Publica manualmente el contenido del ZIP conservando las rutas relativas y `service-worker.js` junto a la página. Comprueba por HTTPS la galería, el manifiesto, iconos, los archivos de `assets/vendor/draco/` y la consola del navegador. Abre la app con conexión, descarga los modelos y verifica una recarga sin red. No se ha creado ni publicado hosting en este trabajo.
