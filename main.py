import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

def add_task():
    task = simpledialog.askstring("Input", "Please enter your task:")
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

def list_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

root.mainloop()