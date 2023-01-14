from flask import Flask
from . import file

app = Flask(__name__)
app.register_blueprint(file.file)