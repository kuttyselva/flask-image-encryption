from flask import Flask
import logging as logger
from flask_cors import CORS
logger.basicConfig(level="DEBUG")
flaskAppInstance = Flask(__name__)
CORS(flaskAppInstance)
if __name__ == '__main__':

    logger.debug("Starting Flask Server")
    from api import *
    flaskAppInstance.run(port=5000,debug=True,use_reloader=True)