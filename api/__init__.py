from flask_restful import Api
from app import flaskAppInstance
from .Task import Task
from .Another import Another
restServer = Api(flaskAppInstance)
restServer.add_resource(Task,"/api/encrypt")
restServer.add_resource(Another,"/api/decrypt")