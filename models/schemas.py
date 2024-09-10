from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=False)
    when_created = fields.Str(dump_only=True)
    when_completed = fields.Str(dump_only=True)
    timelimit = fields.Str(required=True)
    completed = fields.Bool(dump_only=True) #If  FALSE means the tasks is not completed.



class UpdateTaskSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=False)
    when_created = fields.Str(required= True)
    when_completed = fields.Str(required=False, allow_none=True)
    timelimit = fields.Str(required=True)
    completed = fields.Bool(required=True)