import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to mark a selected task as completed
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, task + " (completed)")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for the task entry and buttons
frame_tasks = tk.Frame(root)
frame_tasks.pack()

# Create the listbox to hold the tasks
listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

# Create the entry widget for adding new tasks
entry_task = tk.Entry(frame_tasks, width=40)
entry_task.pack(side=tk.LEFT)

# Create the add task button
button_add_task = tk.Button(frame_tasks, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT)

# Create the delete task button
button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack()

# Create the mark completed button
button_mark_completed = tk.Button(root, text="Mark Completed", command=mark_completed)
button_mark_completed.pack()

# Start the main event loop
root.mainloop()
