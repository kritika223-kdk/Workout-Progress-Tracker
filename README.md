# Workout Progress Tracker

## About the Project

Workout Progress Tracker is a small Python project I made to record my workout details.

It allows me to enter the exercise name, weight, sets and repetitions and save them for later. I can also check my previous workouts and view my progress.

The workout data is stored in a JSON file, so I don't need a separate database.

---

## Features

* Add workout details
* Save workout records
* View workout history
* View workout progress
* Check invalid weight input
* Store data in JSON
* Works offline

---

## Technologies Used

* Python
* Tkinter
* JSON
* VS Code

---

## Project Files

```text
Workout_progress/
│
├── main.py
├── function.py
├── workout_data.json
├── README.md
└── statement.md
```

* **main.py** – Main window of the application
* **function.py** – Functions used in the project
* **workout_data.json** – Stores workout details
* **README.md** – Project information
* **statement.md** – Project statement

---

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

```text
python main.py
```

4. Press Enter and the application will open.

---

## How to Use

### Add Workout

Click **Add Workout** and enter the exercise name, weight, sets and repetitions. Then save the workout.

### Workout History

Click **Workout History** to see the saved workouts in a table.

### Workout Progress

Click **Workout Progress** to check the progress from the saved workout data.

---

## Data Storage

The workout records are saved in `workout_data.json`.

The saved details are:

* Date
* Exercise
* Weight
* Sets
* Repetitions

---

## Testing

I tested the project by:

* Adding workout records
* Checking the saved JSON data
* Checking the workout history table
* Entering an incorrect weight
* Checking the error message
* Checking the workout progress
* Reopening the application to check if the saved data was still there

---

## Future Improvements

Some features I can add later are:

* Progress graphs
* Exercise search
* Edit and delete options
* More workout statistics
* Better interface

---

## Conclusion

This project helped me learn how to make a basic GUI using Tkinter, store data using JSON and connect different Python files.

It also gave me practice with taking user input, displaying data in a table and handling basic errors.

---

## Author

**Kritika Goyal**

**Project:** Workout Progress Tracker
