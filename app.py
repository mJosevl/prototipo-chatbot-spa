import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

engine = create_engine('sqlite:///chatbot_db.sqlite')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Mensaje(Base):
    __tablename__ = 'mensajes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    opcion = Column(String(10))
    respuesta = Column(String(255))
    fecha = Column(DateTime, default=datetime.utcnow)

class HistorialInteracciones(Base):
    __tablename__ = 'historial_interacciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(50))
    mensaje = Column(String(255))
    respuesta = Column(String(255))
    fecha = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(ACCOUNT_SID, AUTH_TOKEN)

MENU = (
    "Hola! ¿Cómo puedo ayudarte hoy?\n"
    "1. Horario de atención\n"
    "2. Ubicación\n"
    "3. Productos o servicios\n"
    "4. Contacto\n"
    "5. Hablar con un agente"
)

@app.route("/bot", methods=['POST'])
def bot():
    try:
        incoming_msg = request.values.get('Body', '').lower()
        usuario = request.values.get('From', '').lower()
        resp = MessagingResponse()
        msg = resp.message()

        nuevo_historial = HistorialInteracciones(usuario=usuario, mensaje=incoming_msg)
        session.add(nuevo_historial)
        session.commit()

        if any(p in incoming_msg for p in ['hola', 'inicio', 'menu', 'menú', 'ayuda', 'start']):
            respuesta_texto = MENU
            opcion = 'hola'
        elif incoming_msg == '1':
            respuesta_texto = 'Nuestro horario de atención es de lunes a viernes de 9 a 18 horas.'
            opcion = '1'
        elif incoming_msg == '2':
            respuesta_texto = 'Estamos ubicados en Villa Rucahue 600.'
            opcion = '2'
        elif incoming_msg == '3':
            respuesta_texto = 'Ofrecemos una amplia gama de productos y servicios. Visita nuestro sitio web para más información.'
            opcion = '3'
        elif incoming_msg == '4':
            respuesta_texto = 'Puedes contactarnos al teléfono 555-1234 o al correo comercialaustralroad@gmail.com.'
            opcion = '4'
        elif incoming_msg == '5':
            respuesta_texto = 'Por favor, espera un momento mientras te conectamos con un agente.'
            opcion = '5'
        elif 'feedback' in incoming_msg:
            respuesta_texto = 'Por favor, proporciona tu feedback sobre el chatbot.'
            opcion = 'feedback'
        else:
            respuesta_texto = 'Lo siento, no entiendo tu solicitud. Por favor elige una opción del menú.'
            opcion = 'otro'

        msg.body(respuesta_texto)
        session.add(Mensaje(opcion=opcion, respuesta=respuesta_texto))
        session.commit()

        msg.body(
            "\n¿Hay algo más en lo que pueda ayudarte?\n"
            "1. Horario de atención\n"
            "2. Ubicación\n"
            "3. Productos o servicios\n"
            "4. Contacto\n"
            "5. Hablar con un agente"
        )

        return str(resp)

    except SQLAlchemyError as e:
        print("Error en la base de datos:", e)
        return str(MessagingResponse().message("Ha ocurrido un error interno en la base de datos."))
    except Exception as e:
        print("Error desconocido:", e)
        return str(MessagingResponse().message("Ha ocurrido un error inesperado."))

@app.route("/")
def index():
    return "Chatbot Austral Road SPA activo ✅"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
