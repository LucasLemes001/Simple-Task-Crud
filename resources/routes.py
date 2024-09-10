from flask_smorest import Blueprint, abort
from flask.views import MethodView
from datetime import datetime


from models.schemas import TaskSchema, UpdateTaskSchema
from models.tasks import TaskModel
from db import db

blp = Blueprint("tasks", __name__, description="Operations on tasks!")


@blp.route("/tasks")   #http://127.0.0.1:5000/tasks
class ListAllTasks(MethodView):
    ''' This Endpoint is used for show all tasks, completed or not.'''
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskModel.query.all()
    
    
@blp.route("/uncompletedtasks")   #http://127.0.0.1:5000/uncompletetasks
class ListUncompletedTasks(MethodView):
    '''This class is used for show all uncompleted tasks listed on the database.'''
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskModel.query.filter_by(completed=False)


@blp.route("/completedtasks")   #http://127.0.0.1:5000/completetasks
class ListCompletedTasks(MethodView):
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        '''This Endpoint is used for show all completed tasks listed on the database.'''
        
        return TaskModel.query.filter_by(completed=True)
    

@blp.route("/tasks/<int:task_id>")   #http://127.0.0.1:5000/tasks/1
class ListSingleTaks(MethodView):
    @blp.response(200, TaskSchema)
    def get(self, task_id):
        '''This Endpoint is used for show a specific task listed on the database.
        The task will be searched by its id.
        '''
        task = TaskModel.query.get_or_404(task_id)
        return task





@blp.route("/newtask")   #http://127.0.0.1:5000/newtask
class CreateNewTask(MethodView):
    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self, task_data):
        '''This Endpoint is used for create a new task on the database.
        The task will be created with the given parameters.
        '''
        create_time = datetime.now()
        when_created = create_time.strftime("%d/%m/%Y %H:%M:%S")
        task = TaskModel(**task_data, when_created=when_created)
        db.session.add(task)
        db.session.commit()
        return task
    
@blp.route("/removetask/<int:task_id>")   #http://127.0.0.1:5000/removetask/1
class DeleteTask(MethodView):
    @blp.response(200, TaskSchema)
    def delete(self, task_id):
        '''This Endpoint is used for delete a specific task from the database.
        The task will be searched by its id.
        '''
        task = TaskModel.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {"Message: Task Deleted!"}, 200
    


@blp.route("/update/<int:task_id>")   #http://127.0.0.1:5000/update/1
class UpdateTask(MethodView):
    @blp.arguments(UpdateTaskSchema)
    @blp.response(200, UpdateTaskSchema)
    def put(self, inc_data, task_id):
        
        '''This Endpoint is used for update a specific task on the database.
        The task will be searched by its id.
        The task will be updated with the given parameters.
        '''
        task = TaskModel.query.get(task_id)
        try:
            task.title = inc_data["title"]
            task.description = inc_data["description"]
            task.timelimit = inc_data["timelimit"] 
            task.completed = inc_data["completed"]
            task.when_completed = inc_data["when_completed"]
            db.session.add(task)
            db.session.commit()
            return task
        except:
            abort(404, message="Something went wrong. Task not found.")


@blp.route("/complete/<int:task_id>")   #http://127.0.0.1:5000/complete/1
class CompleteATask(MethodView):
    @blp.response(200, TaskSchema)
    def put(self, task_id):
        '''This Endpoint is used for mark a specific task as completed on the database.
        The task will be searched by its id.
        The task will be updated with the given parameters.
        '''
        task = TaskModel.query.get(task_id)
        task.completed = True
        task.when_completed = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.session.add(task)
        db.session.commit()
        return task