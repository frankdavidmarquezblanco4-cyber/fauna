/* FaunaXR · PWA offline — shell v42, modelos bajo demanda */
'use strict';

const CACHE_NAME = 'faunaxr-offline-v42';
const MODEL_CACHE_NAME = 'faunaxr-models-v1';

// Shell pequeño y necesario para abrir la app. Cada recurso se intenta por separado:
// una imagen o recurso faltante no debe dejar la PWA sin instalar.
const APP_SHELL_CRITICAL = [
  './',
  './index.html',
  './galeria-xr.html',
  './manifest.webmanifest',
  './assets/data/fauna-learning.es.json',
  './assets/pwa/icon-192.png',
  './assets/pwa/icon-512.png',
  './assets/pwa/icon-maskable-512.png',
  './assets/vendor/model-viewer-4.0.0.min.js',
  './assets/vendor/aframe-1.7.0.min.js',
  './assets/vendor/aframe/fonts/Roboto-msdf.json',
  './assets/vendor/aframe/fonts/Roboto-msdf.png',
  './assets/vendor/draco/draco_decoder.js',
  './assets/vendor/draco/draco_wasm_wrapper.js',
  './assets/vendor/draco/draco_decoder.wasm',
  './assets/models/scratch-cat.webp',
  './assets/models/dog.webp',
  './assets/models/rabbit.webp',
  './assets/models/chicken.webp',
  './assets/models/cow.webp',
  './assets/models/horse.webp',
  './assets/models/duck.webp',
  './assets/models/fox.webp',
  './assets/models/wild-lion.webp',
  './assets/models/wild-tiger.webp',
  './assets/models/wild-wolf.webp',
  './assets/models/wild-elephant.webp',
  './assets/models/wild-giraffe.webp',
  './assets/models/wild-rhino.webp',
  './assets/models/wild-panda.webp',
  './assets/models/wild-shark.webp',
  './assets/models/wild-bear.webp',
  './assets/models/wild-crocodile.webp',
  './assets/models/wild-gorilla.webp',
  './assets/models/wild-zebra.webp',
  './assets/models/wild-cheetah.webp'
];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await Promise.allSettled(APP_SHELL_CRITICAL.map((url) => cache.add(url)));
    // MediaPipe WASM/task and the 21 GLB are deliberately not installed here.
    // MediaPipe is fetched/cached on first use; animal GLBs use the explicit download button.
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names
      .filter((name) => (name.startsWith('scratchxr-offline-') || name.startsWith('faunaxr-offline-')) && name !== CACHE_NAME)
      .map((name) => caches.delete(name)));
    // Keep MODEL_CACHE_NAME across shell updates so user-downloaded models persist.
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  const isModel = /\/assets\/models\/[^/]+\.glb$/i.test(url.pathname);
  if (isModel) {
    event.respondWith((async () => {
      const modelCache = await caches.open(MODEL_CACHE_NAME);
      const cached = await modelCache.match(request);
      if (cached) return cached;
      try { return await fetch(request); }
      catch (_) {
        return new Response('Este modelo todavía no se descargó para uso sin conexión.', {
          status: 503,
          headers: { 'Content-Type': 'text/plain; charset=utf-8' }
        });
      }
    })());
    return;
  }

  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_NAME);
      try {
        const response = await fetch(request);
        if (response.ok) {
          try { await cache.put(request, response.clone()); } catch (_) { /* No bloquear la navegación. */ }
        }
        return response;
      } catch (_) {
        const isGallery = url.pathname.endsWith('/galeria-xr.html');
        const fallbackPage = isGallery ? './galeria-xr.html' : './index.html';
        return (await cache.match(request))
          || (await cache.match(new URL(fallbackPage, self.registration.scope).href))
          || new Response('FaunaXR todavía no se abrió con conexión para preparar el modo sin conexión.', {
            status: 503,
            headers: { 'Content-Type': 'text/plain; charset=utf-8' }
          });
      }
    })());
    return;
  }

  event.respondWith((async () => {
    const cache = await caches.open(CACHE_NAME);
    const cached = await cache.match(request);
    if (cached) return cached;
    try {
      const response = await fetch(request);
      // Heavy, optional resources (MediaPipe task/WASM) are cached on first use,
      // never as part of installation. Range/partial and opaque responses are skipped.
      if (response.status === 200 && response.type === 'basic') {
        try { await cache.put(request, response.clone()); } catch (_) { /* Quota/API errors do not break online use. */ }
      }
      return response;
    } catch (_) {
      return new Response('Este recurso no se ha descargado en este dispositivo todavía.', {
        status: 503,
        headers: { 'Content-Type': 'text/plain; charset=utf-8' }
      });
    }
  })());
});
