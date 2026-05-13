# prototipo-chatbot-spa
Prototipo de chatbot conversacional para la atencion al cliente en Austral Road SPA via Twilio WhatsApp Sandbox

Chatbot Conversacional - Austral Road SPA
Prototipo de chatbot conversacional desarrollado para optimizar la atencion al cliente en Austral Road SPA. Permite automatizar respuestas a consultas frecuentes a traves de WhatsApp utilizando Twilio Sandbox.
Descripcion
Este proyecto fue desarrollado como parte del examen de titulo de Tecnico de Nivel Superior en Analisis y Programacion Computacional en IACC. El chatbot maneja un menu de opciones predefinidas y registra cada interaccion en una base de datos local SQLite.
Stack tecnologico

Python 3
Flask
Twilio WhatsApp Sandbox
SQLAlchemy + SQLite
Render (deploy)
python-dotenv

Requisitos

Python 3.10 o superior
Cuenta Twilio (gratuita con Sandbox)
Cuenta Render para el deploy

Instalacion local
Clonar el repositorio:
git clone https://github.com/tuusuario/chatbot-austral-road.git
cd chatbot-austral-road
Instalar dependencias:
pip install flask==3.0.3 twilio==9.3.2 sqlalchemy==2.0.36 python-dotenv==1.0.1
Crear archivo .env en la raiz del proyecto:
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Ejecutar el servidor:
python app.py
Variables de entorno
VariableDescripcionTWILIO_ACCOUNT_SIDAccount SID de la consola TwilioTWILIO_AUTH_TOKENAuth Token de la consola Twilio
Configuracion del webhook en Twilio
Una vez desplegado en Render, copiar la URL publica y configurarla en Twilio Sandbox Settings:
https://tu-app.onrender.com/bot
Opciones del chatbot

Horario de atencion
Ubicacion
Productos o servicios
Contacto
Hablar con un agente
