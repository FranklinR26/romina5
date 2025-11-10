import os
import cloudinary
from dotenv import load_dotenv

# Carga el archivo .env si estás en local
load_dotenv()

# Configura Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

# Flask secret key (para sesiones seguras)
from flask import Flask
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET')
