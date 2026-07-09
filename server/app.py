from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from datetime import datetime
from models import db, Exercise, Workout, WorkoutExercise
from schemas import (
    ExerciseSchema,
    WorkoutSchema,
    WorkoutExerciseSchema,
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Workout API is running!"
        }
    )


@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return workouts_schema.dump(workouts), 200


@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return workout_schema.dump(workout), 200


@app.route("/workouts", methods=["POST"])
def create_workout():

    data = request.get_json()

    errors = workout_schema.validate(data)

    if errors:
        return jsonify(errors), 400

    workout = Workout(
    date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
    duration_minutes=data["duration_minutes"],
    notes=data.get("notes")
)

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):

    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify(
        {
            "message": "Workout deleted successfully."
        }
    ), 200

 
if __name__ == "__main__":
    app.run(port=5555, debug=True)