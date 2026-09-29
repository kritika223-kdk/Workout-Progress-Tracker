import tkinter as tk
import json
from tkinter import ttk, messagebox
from datetime import date
def add_workout(root):
    workout_window=tk.Toplevel(root)
    workout_window.title("Add Workout")
    workout_window.geometry("500x450")
    workout_window.configure(bg="#0b0b0b")

    exercise_label=tk.Label(
        workout_window,
        text="Exercise Name",
        font=("arial",12),
        bg="#0b0b0b",
        fg="#bdbdbd"
    )
    exercise_label.pack(pady=6)

    exercise_entry=tk.Entry(
        workout_window,
        font=("arial",12),
        width=25,
        justify="center",
        bg="#2b2b2b",
        fg="white",
        insertbackground="#6b7d32",
    )
    exercise_entry.pack(pady=3)

    weight_label=tk.Label(
        workout_window,
        text="Weight (kg)",
        font=("arial",12),
        bg="#0b0b0b",
        fg="#bdbdbd"
    )
    weight_label.pack(pady=6)

    weight_entry=tk.Entry(
        workout_window,
        font=("arial",12),
        width=25,
        justify="center",
        bg="#2b2b2b",
        fg="white",
        insertbackground="#6b7d32",
    )
    weight_entry.pack(pady=3)


    set_label=tk.Label(
        workout_window,
        text="Number of sets",
        font=("arial",12),
        bg="#0b0b0b",
        fg="#bdbdbd"
    )
    set_label.pack(pady=6)

    set_entry=tk.Entry(
        workout_window,
        font=("arial",12),
        width=25,
        justify="center",
        bg="#2b2b2b",
        fg="white",
        insertbackground="#6b7d32",
    )
    set_entry.pack(pady=3)

    rep_label=tk.Label(
        workout_window,
        text="Number of Reps",
        font=("arial",12),
        bg="#0b0b0b",
        fg="#bdbdbd",)
    rep_label.pack(pady=6)

    rep_entry=tk.Entry(
        workout_window,
        font=("arial",12),
        width=25,
        justify="center",
        bg="#2b2b2b",
        fg="white",
        insertbackground="#6b7d32",
    )
    rep_entry.pack(pady=3)

    def save_workout():
        print("Save button clicked")
        exercise = exercise_entry.get()
        weight = weight_entry.get()
        sets= set_entry.get()
        reps = rep_entry.get()

        if not exercise or not weight or not sets or not reps :
            messagebox.showerror("Missing Information.","please fill all the fields")
            return
        try:
            float(weight)
        except ValueError:
            messagebox.showerror("Invalid Weight","Weight must be a number")
            return
        if float(weight)<0:
            messagebox.showerror("Invalid Weight","Weight must be greater than or equal to 0")
            return
        
        try:
            int(sets)
        except ValueError:
            messagebox.showerror("Invalid Sets","Sets must be a whole number")
            return
        if int(sets)<=0:
            messagebox.showerror("Invalid Sets","Sets must be greater than 0")
            return
        
        try:
            int(reps)
        except ValueError:
            messagebox.showerror("Invalid Reps","Reps must be a whole number") 
            return           
        if int(reps)<=0:
            messagebox.showerror("Invalid Reps","Reps must be greater than 0")
            return
            

        workout_date= date.today().strftime("%d-%m-%Y")
        workout={
            "date":workout_date,
            "exercise":exercise,
            "weight":weight,
            "sets":sets,
            "reps":reps
        }
        try:
            with open ("workout_data.json", "r") as file:
                workouts= json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            workouts=[] 
            
        workouts.append(workout)
        with open("workout_data.json","w") as file:
            json.dump(workouts,file,indent=4)
        messagebox.showinfo("Success","Workout saved successfully")
        workout_window.destroy()

    save_button=tk.Button(
        workout_window,
        text="Save Workout",
        font=("Arial",12),
        width=(20),
        height=2,
        bg="#6b7d32",
        fg="white",
        activebackground="#4f5d25",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=save_workout)
    save_button.pack(pady=10)

def show_history(root):
    history_window=tk.Toplevel(root)
    history_window.title("Workout History")
    history_window.geometry("800x400")
    history_window.configure(bg="#0b0b0b")

    history_label=tk.Label(
        history_window,
        text=("Workout History"),
        font=("arial",22,"bold"),
        bg=("#0b0b0b"),
        fg=("#6b7d32")
    )
    history_label.pack(pady=20)
    try:
        with open ("workout_data.json","r") as file:
            workouts=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        workouts=[]

    if not workouts:
        no_data_label=tk.Label(
            history_window,
            text="No workouts Avialable,\n Add a wrokout first!",
            font=("Arial",14,"bold"),
            bg="#0b0b0b",
            fg="#6b7d32",
        )
        no_data_label.pack(pady=20)
        return
    
    headers=[
        ("Date",12),
        ("Exercise",20),
        ("Weight",20),
        ("Sets",10),
        ("Reps",10),
        ]

    table_frame=tk.Frame(
        history_window,
        bg="#1e1e1e")
    table_frame.pack(pady=10)

    for column, (header,width) in enumerate(headers):
        label=tk.Label(
            table_frame,
            text=header,
            bg="#6b7d32",
            fg="White",
            font=("Arial",13,"bold"),
            width=width,
            highlightthickness=1,
            highlightbackground="#0b0b0b"
        )
        label.grid(row=0, column=column, padx=0,pady=0,sticky="ew")

    for row,workout in enumerate(workouts, start=1):
        values=[
        workout["date"],
        workout["exercise"],
        workout["weight"],
        workout["sets"],
        workout["reps"],
        ]

        for column, value in enumerate(values):
            width=headers[column][1]
            label=tk.Label(
                table_frame,
                text=value,
                bg="#2B2B2B",
                fg="white",
                width=width,
                highlightthickness=1,
                highlightbackground="#0b0b0b",
            )
            label.grid(row=row, column=column,padx=0,pady=0,sticky="ew")

def show_progress(root):
    progress_window=tk.Toplevel(root)
    progress_window.title("Workout Progress")
    progress_window.geometry("800x550")
    progress_window.configure(bg="#0b0b0b")
    try:
        with open ("workout_data.json","r") as file:
            workouts=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        workouts=[]

    exercises=[]
    for workout in workouts:
        if workout["exercise"] not in exercises:
            exercises.append(workout["exercise"])

    exercise_var=tk.StringVar()
    exercise_dropdown=ttk.Combobox(
        progress_window,
        textvariable=exercise_var,
        values=exercises,
        state="readonly"
    )
    exercise_dropdown.pack(pady=10)

    results_frame= tk.Frame(progress_window,bg="#0b0b0b")
    results_frame.pack()
    if exercises:
        exercise_dropdown.current(0)
    else:
        no_data_label=tk.Label(
            progress_window,
            text=("No workouts available.\n Add a workout first!!"),
            font=("Arial",14),
            bg="#0b0b0b",
            fg="white",
        )
        no_data_label.pack(pady=20)
        
    def calculate_progress():
        selected_exercise=exercise_var.get()
        exercise_workouts=[]
        for workout in workouts:
            if workout["exercise"]==selected_exercise:
                exercise_workouts.append(workout)

        if len(exercise_workouts)<2:

            tk.Label(
                results_frame,
                text="Not Enough Data to Calculate",
                font=("Arial",14),
                bg="#2b2b2b",
                fg="White"
            ).pack(pady=10)
            return

        else:
            previous_workout=exercise_workouts[-2]
            latest_workout=exercise_workouts[-1]
            previous_weight=float(previous_workout["weight"])
            latest_weight=float(latest_workout["weight"])

            previous_sets=int(previous_workout["sets"])
            latest_sets=int(latest_workout["sets"])

            previous_reps=int(previous_workout["reps"])
            latest_reps=int(latest_workout["reps"])

            previous_volume=previous_weight*previous_sets*previous_reps
            latest_volume=latest_weight*latest_sets*latest_reps

            sets_progress=latest_sets-previous_sets
            reps_progress=latest_reps-previous_reps
            weight_progress=latest_weight-previous_weight
            volume_progress=latest_volume-previous_volume

            if sets_progress>0:
                sets_text=(f"Increased by {sets_progress}")
            elif sets_progress<0:
                sets_text=(f"decreased by {abs(sets_progress)}")
            else:
                sets_text=("No change")

            if reps_progress>0:
                reps_text=(f"Increased by {reps_progress}")
            elif reps_progress<0:
                reps_text=(f"decreased by {abs(reps_progress)}")
            else:
                reps_text=("No change")

            if weight_progress>0:
                progress_text=(f"Increased by {weight_progress:g} kg")
            elif weight_progress<0:
                progress_text=(f"decreased by {abs(weight_progress):g} kg")
            else:
                progress_text=("No change")

            if volume_progress>0:
                volume_text=(f"Increased by {volume_progress:g} kg")
            elif volume_progress<0:
                volume_text=(f"Decreased by {abs(volume_progress):g} kg")
            else:
                volume_text=("No Change")

            for widget in results_frame.winfo_children():
                widget.destroy()

            exercise_label=tk.Label(
                results_frame,                    
                text=f"Exercise: {selected_exercise}",
                font=("Arial",20,"bold"),
                bg="#0b0b0b",
                fg="#6b7d32"
            )
            exercise_label.pack(pady=20)
            previous_label=tk.Label(
                results_frame,
                text=(f"Previous : {previous_weight:g} kg| {previous_sets} sets x {previous_reps} reps"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="white"
            )
            previous_label.pack(pady=10)
            
            latest_label=tk.Label(
                results_frame,
                text=(f"Latest : {latest_weight:g} kg| {latest_sets} sets x {latest_reps} reps"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="white"
            )
            latest_label.pack(pady=10)
            
            progress_label=tk.Label(
                results_frame,
                text=(f"Weight Progress: {progress_text}"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="white"
            )
            progress_label.pack(pady=15)

            set_label=tk.Label(
                results_frame,
                text=(f"Sets Progress: {sets_text}"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="white",
            )
            set_label.pack(pady=10)

            reps_label=tk.Label(
                results_frame,
                text=(f"Reps Progress: {reps_text}"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="white",
            )
            reps_label.pack(pady=10)

            previous_volume_label=tk.Label(
                results_frame,
                text=(f"Previous Volume: {previous_volume:g} kg"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="white",
            )
            previous_volume_label.pack(pady=10)

            latest_volume_label=tk.Label(
                results_frame,
                text=(f"Latest Volume: {latest_volume:g} kg"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="White",
            )
            latest_volume_label.pack(pady=10)

            volume_label=tk.Label(
                results_frame,
                text=(f"Total Progress: {volume_text}"),
                font=("Arial",14),
                bg="#2b2b2b",
                fg="white"
            )
            volume_label.pack(pady=10)

    progress_button=tk.Button(
        progress_window,
        text="Show Progress",
        width=20,
        height=2,
        state= "normal" if exercises else "disabled",
        bg="#6b7d32",
        fg="white",
        activebackground="#4f5d25",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=calculate_progress
    )
    progress_button.pack(pady=10)

    
  

    