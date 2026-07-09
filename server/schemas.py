from marshmallow import Schema, fields, validate, validates, ValidationError


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=2)
    )
    category = fields.Str(
        required=True,
        validate=validate.Length(min=2)
    )
    equipment_needed = fields.Bool(required=True)

    @validates("name")
    def validate_name(self, value, **kwargs):
        if value.strip() == "":
            raise ValidationError("Exercise name cannot be blank.")


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    @validates("duration_minutes")
    def validate_duration(self, value, **kwargs):
        if value <= 0:
            raise ValidationError("Duration must be greater than zero.")


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    reps = fields.Int(required=True)
    sets = fields.Int(required=True)
    duration_seconds = fields.Int(required=True)