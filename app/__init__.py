from config import Config
from flask import Flask

appInstance = Flask(__name__)
appInstance.config.from_object(Config)

from app import routes