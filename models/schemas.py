from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=False)
    when_created = fields.Str(dump_only=True)
    timelimit = fields.Str(required=True)


class CompletedTasksSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=False)
    when_created = fields.Str(required=True)
    when_fineshed = fields.Str(required=True)

