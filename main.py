import tkinter as tk
from function import add_workout, show_history, show_progress
# Main Window
root=tk.Tk()
root.title(" Workout Progress Tracker")  
root.geometry("800x500")
root.configure(bg="#0B0B0B")

# Title
title_label=tk.Label (
    root, text="Workout Progress Tracker", 
    font=("Helvetica", 24, "bold"),
    bg="#0B0B0B", 
    fg="#6B7D32")
title_label.pack(pady=30)

# Subtitle
subtitle_label = tk.Label(
    root,
    text="Never gonna stop. Grinding!! Tearing!!",
    font=("Helvetica",16),
    bg=("#0B0B0B"),
    fg="#BDBDBD",)
subtitle_label.pack(pady=5)

# Workout button
add_button= tk.Button(
    root,
    text=("Add Workout"),
    font=("Arial",12,),
    width=20,
    height=2,
    bg="#6B7D32",
    fg="white",
    activebackground="#4F5D25",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda: add_workout(root))
add_button.pack(pady=15)

# Workout history button
history_button= tk.Button(
    root,
    text="Workout History",
    font= ("Arial",12),
    width=20,
    height=2,
    bg="#6B7D32",
    fg="white",
    activebackground="#4F5D25",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda: show_history(root))
history_button.pack(pady=15)

# Workout Progress Button
progress_button=tk.Button(
    root,
    text="Workout Progress",
    font=("Arial",12),
    width=20,
    height=2,
    bg="#6B7D32",
    fg="white",
    activebackground="#4F5D25",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=lambda:show_progress(root),)
progress_button.pack(pady=15)

root.mainloop()