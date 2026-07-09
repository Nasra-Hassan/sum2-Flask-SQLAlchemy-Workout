from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = "exercises"

    __table_args__ = (
        CheckConstraint("length(name) > 0", name="check_exercise_name"),
        CheckConstraint("length(category) > 0", name="check_exercise_category"),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(100), nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    workouts = db.relationship(
        "Workout",
        secondary="workout_exercises",
        back_populates="exercises",
        viewonly=True
    )

    @validates("name")
    def validate_name(self, key, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("Exercise name must contain at least 2 characters.")
        return value.strip()

    @validates("category")
    def validate_category(self, key, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("Category is required.")
        return value.strip()


class Workout(db.Model):
    __tablename__ = "workouts"

    __table_args__ = (
        CheckConstraint("duration_minutes > 0", name="check_duration"),
    )

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    exercises = db.relationship(
        "Exercise",
        secondary="workout_exercises",
        back_populates="workouts",
        viewonly=True
    )

    @validates("duration_minutes")
    def validate_duration(self, key, value):
        if value <= 0:
            raise ValueError("Workout duration must be greater than zero.")
        return value


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    __table_args__ = (
        CheckConstraint("reps >= 0", name="check_reps"),
        CheckConstraint("sets >= 0", name="check_sets"),
        CheckConstraint("duration_seconds >= 0", name="check_duration_seconds"),
    )

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    reps = db.Column(db.Integer, default=0)
    sets = db.Column(db.Integer, default=0)
    duration_seconds = db.Column(db.Integer, default=0)

    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )

    @validates("reps")
    def validate_reps(self, key, value):
        if value < 0:
            raise ValueError("Reps cannot be negative.")
        return value

    @validates("sets")
    def validate_sets(self, key, value):
        if value < 0:
            raise ValueError("Sets cannot be negative.")
        return value

    @validates("duration_seconds")
    def validate_duration_seconds(self, key, value):
        if value < 0:
            raise ValueError("Duration cannot be negative.")
        return value