# The mission hare is make the fucking CRUD DATABASE MODELS:
# Create, Read, Update, Delete
# Just imagine that we are creating some tasks us to make.
from db import db
class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    when_created = db.Column(db.String(20), nullable=False)
    timelimit = db.Column(db.String(80), nullable=False)
    when_completed = db.Column(db.String(20), nullable=True, default="Not Completed Yet")
    completed = db.Column(db.Boolean, default=False)
    


    

