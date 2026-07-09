#!/usr/bin/env python3

from datetime import date

from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Clearing existing data...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    db.session.commit()

    print("Creating exercises...")

    pushups = Exercise(
        name="Push Ups",
        category="Strength",
        equipment_needed=False
    )

    squats = Exercise(
        name="Squats",
        category="Strength",
        equipment_needed=False
    )

    treadmill = Exercise(
        name="Treadmill Run",
        category="Cardio",
        equipment_needed=True
    )

    db.session.add_all([pushups, squats, treadmill])
    db.session.commit()

    print("Creating workouts...")

    workout1 = Workout(
        date=date(2026, 7, 9),
        duration_minutes=45,
        notes="Morning workout"
    )

    workout2 = Workout(
        date=date(2026, 7, 10),
        duration_minutes=60,
        notes="Leg day"
    )

    db.session.add_all([workout1, workout2])
    db.session.commit()

    print("Linking workouts and exercises...")

    we1 = WorkoutExercise(
        workout=workout1,
        exercise=pushups,
        reps=15,
        sets=3,
        duration_seconds=0
    )

    we2 = WorkoutExercise(
        workout=workout1,
        exercise=treadmill,
        reps=0,
        sets=0,
        duration_seconds=1200
    )

    we3 = WorkoutExercise(
        workout=workout2,
        exercise=squats,
        reps=12,
        sets=4,
        duration_seconds=0
    )

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Database seeded successfully!")