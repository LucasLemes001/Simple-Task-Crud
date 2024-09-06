# The mission hare is make the fucking CRUD DATABASE MODELS:
# Create, Read, Update, Delete
# Just imagine that we are creating some tasks us to make.
from db import db
class TaskModel(db.Model):
    __tablename__ = "tasks_to_do"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300))
    when_created = db.Column(db.String(20), nullable=False)
    timelimit = db.Column(db.String(80), nullable=False)
    

class CompletedTasks(db.Model):
    __tablename__= "completed_tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300))
    when_created = db.Column(db.DateTime, nullable=False)
    when_finished = db.Column(db.DateTime, nullable=False)




    

