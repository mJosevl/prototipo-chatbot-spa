# Chatbot Austral Road SPA

Prototipo de chatbot conversacional para WhatsApp via Twilio Sandbox.

## Stack
- Python + Flask
- Twilio WhatsApp Sandbox
- SQLite (registro de interacciones)
- Render (deploy)

## Variables de entorno requeridas (en Render)
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`

## Endpoint webhook
`POST /bot`

Configura esta URL en Twilio Sandbox:
`https://TU-URL-RENDER.onrender.com/bot`
