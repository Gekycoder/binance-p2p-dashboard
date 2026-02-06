# Binance P2P Arbitrage Dashboard & Bridge 🚀

Una terminal de arbitraje para el mercado P2P de Binance, optimizada para **VES (Bolívares)** y **USD (Dólares)** con precisión quirúrgica y analítica en tiempo real.

## ✨ Características Principales

-   **Analítica de Precisión**: Hasta **3 decimales** para el mercado USD, permitiendo capturar spreads mínimos con exactitud.
-   **Multi-Fiat**: Soporte completo para VES y USD con etiquetas dinámicas (BCV, Paridad Base).
-   **Terminal Bridge**: Puente en Python que extrae datos directamente de Binance, evitando bloqueos de CORS.
-   **PWA (Progressive Web App)**: Instalable en tu teléfono móvil como una aplicación nativa.
-   **Layout Estabilizado**: Actualizaciones silenciosas cada 5 segundos sin saltos de pantalla (Zero Layout Shift).
-   **Calculadora en Vivo**: Simulación de compra/venta con tasas reales y cálculo de rentabilidad instantáneo.

## 🏗️ Arquitectura Técnica

El proyecto se divide en dos componentes:
1.  **Backend (bridge.py)**: Servidor ligero en Python que actúa como puente API y servidor de archivos estáticos.
2.  **Frontend (dashboard_arbitraje.html)**: Interfaz de usuario construida con TailwindCSS, Vanilla JS y Chart.js.

## 🛠️ Instalación y Uso Local

1. Asegúrate de tener **Python 3** instalado.
2. Descarga los archivos del proyecto.
3. Ejecuta el puente:
   ```bash
   python bridge.py
   ```
4. Abre tu navegador en: `http://localhost:5001/dashboard_arbitraje.html`

## ☁️ Despliegue en la Nube (Móvil)

Este proyecto está preparado para ser desplegado en **Render.com** (o servicios similares) para que puedas usarlo en tu teléfono desde cualquier lugar.

Consulta la [GUIA_NUBE.md](./GUIA_NUBE.md) para ver los pasos detallados de cómo subirlo a GitHub y conectarlo a internet 24/7.

## 📁 Archivos del Proyecto
- `bridge.py`: El motor que busca los precios.
- `dashboard_arbitraje.html`: La pantalla de control.
- `manifest.json` & `sw.js`: Archivos necesarios para convertirlo en aplicación móvil.
- `requirements.txt`: Configuración para despliegue en la nube.

## ⚠️ Descargo de Responsabilidad
Este software es una herramienta de visualización y análisis. El trading de criptomonedas y las operaciones P2P conllevan riesgos financieros. El autor no se hace responsable por pérdidas derivadas del uso de esta herramienta.
