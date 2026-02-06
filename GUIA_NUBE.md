# Guía de Despliegue en la Nube (GitHub + Render)

Para que tu terminal funcione 24/7 en tu teléfono, sigue estos pasos:

## Paso 1: Subir a GitHub
1. Crea un repositorio **Público o Privado** en tu GitHub llamado `binance-p2p-dashboard`.
2. Sube estos archivos únicamente:
   - `bridge.py`
   - `dashboard_arbitraje.html`
   - `manifest.json`
   - `sw.js`
   - `requirements.txt`

## Paso 2: Desplegar en Render
1. Ve a [Render.com](https://render.com) y crea una cuenta.
2. Dale a **"New +"** -> **"Web Service"**.
3. Conecta tu repositorio de GitHub.
4. Configuración técnica:
   - **Runtime:** `Python 3`
   - **Build Command:** (Déjalo vacío o usa `pip install -r requirements.txt`)
   - **Start Command:** `python bridge.py`
   - **Instance Type:** `Free` (Gratis)

## Paso 3: Abrir en el Teléfono
1. Una vez que Render te dé tu URL (ejemplo: `https://p2p-bridge.onrender.com`), ábrela en el navegador de tu teléfono.
2. Dale a **"Añadir a pantalla de inicio"**.
3. ¡LISTO! Ya tienes tu app profesional funcionando en la calle.

> [!IMPORTANT]
> La primera vez que abras la app en el día, Render puede tardar unos 30 segundos en "despertar" el servidor si usas el plan gratis. Después de eso, será instantáneo.
