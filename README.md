# sum2-Flask-SQLAlchemy-Workout

## Description

Workout API is a Flask-based REST API designed to manage workout records. The application uses Flask-SQLAlchemy for database management, Flask-Migrate for database migrations, and Marshmallow schemas for request validation and serialization.

The API allows users to create, retrieve, and delete workout records while maintaining a structured database relationship between workouts and exercises.

---

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Marshmallow
* SQLite
* SQLAlchemy ORM

---

## Project Structure

```
sum2-Flask-SQLAlchemy-Workout/

│
├── app.py                  # Flask application and API routes
├── models.py               # Database models and relationships
├── schemas.py              # Marshmallow schemas and validation
├── migrations/             # Database migration files
├── instance/
│   └── app.db              # SQLite database
└── README.md               # Project documentation
```

---

# Database Models

The application contains three database models:

## Exercise Model

Stores available exercises.

Fields:

| Field            | Type    | Description                   |
| ---------------- | ------- | ----------------------------- |
| id               | Integer | Primary key                   |
| name             | String  | Exercise name (unique)        |
| category         | String  | Exercise category             |
| equipment_needed | Boolean | Whether equipment is required |

Validation rules:

* Exercise name must contain at least 2 characters.
* Category must contain at least 2 characters.
* Exercise names must be unique.

---

## Workout Model

Stores workout sessions.

Fields:

| Field            | Type    | Description            |
| ---------------- | ------- | ---------------------- |
| id               | Integer | Primary key            |
| date             | Date    | Workout date           |
| duration_minutes | Integer | Length of workout      |
| notes            | Text    | Optional workout notes |

Validation rules:

* Workout duration must be greater than zero.

---

## WorkoutExercise Model

This is the association table connecting workouts and exercises.

Fields:

| Field            | Type    | Description             |
| ---------------- | ------- | ----------------------- |
| id               | Integer | Primary key             |
| workout_id       | Integer | Foreign key to Workout  |
| exercise_id      | Integer | Foreign key to Exercise |
| reps             | Integer | Number of repetitions   |
| sets             | Integer | Number of sets          |
| duration_seconds | Integer | Exercise duration       |

Validation rules:

* Reps cannot be negative.
* Sets cannot be negative.
* Duration cannot be negative.

---

# Database Relationships

The application implements a many-to-many relationship:

```
Workout
   |
   |
WorkoutExercise
   |
   |
Exercise
```

A workout can contain multiple exercises, and an exercise can belong to multiple workouts.

The relationship is managed using the `WorkoutExercise` association table.

---

# API Endpoints

## Home Route

### GET `/`

Checks whether the API is running.

Response:

```json
{
    "message": "Workout API is running!"
}
```

---

# Workouts

## Get All Workouts

### GET `/workouts`

Returns all workout records.

Response:

```json
[
    {
        "id": 1,
        "date": "2026-07-09",
        "duration_minutes": 45,
        "notes": "Morning workout"
    }
]
```

---

## Get Single Workout

### GET `/workouts/<id>`

Returns a specific workout by ID.

Example:

```
GET /workouts/1
```

---

## Create Workout

### POST `/workouts`

Creates a new workout.

Request body:

```json
{
    "date": "2026-07-09",
    "duration_minutes": 45,
    "notes": "Morning workout"
}
```

Successful response:

* Status Code: `201 Created`

---

## Delete Workout

### DELETE `/workouts/<id>`

Deletes a workout by ID.

Example:

```
DELETE /workouts/1
```

Response:

```json
{
    "message": "Workout deleted successfully."
}
```

---

# Installation and Setup

## 1. Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd sum2-Flask-SQLAlchemy-Workout
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install flask flask-sqlalchemy flask-migrate marshmallow
```

---

# Database Migration

Initialize migrations:

```bash
flask --app app db init
```

Create migration:

```bash
flask --app app db migrate -m "Create workout tables"
```

Apply migration:

```bash
flask --app app db upgrade
```

---

# Running the Application

Start the Flask server:

```bash
python app.py
```

The API will run on:

```
http://127.0.0.1:5555
```

---

# Testing with Postman

The API can be tested using Postman.

Example workflow:

1. Start Flask server.
2. Send requests to available endpoints.
3. Verify JSON responses and status codes.

---

# Validation

The application uses validation at two levels:

## Database Validation

Implemented using SQLAlchemy:

* Check constraints
* Required fields
* Unique fields

## Schema Validation

Implemented using Marshmallow:

* Required request fields
* String length validation
* Numeric validation

---

# Future Improvements

Possible future additions:

* Add full CRUD operations for exercises.
* Add endpoints for managing workout exercises.
* Add authentication and user accounts.
* Add automated pytest test coverage.
* Add pagination for large workout collections.

---

# Author

Created as part of the Flask SQLAlchemy Workout API summative project.
