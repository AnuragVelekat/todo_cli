#!/usr/bin/env python3

import json
import os
from pathlib import Path
import typer

# Initialize the Typer application
app = typer.Typer(help="A simple command-line todo list application.")

# --- IMPORTANT CHANGE HERE: Fixed path for todo.json ---
# Define the fixed directory for your todo data
# It will now always be saved and loaded from: C:\Users\anura\dev\PythonProjects\todo_cli\
data_dir = Path("C:/Users/anura/dev/PythonProjects/todo_cli")
json_file = data_dir / "todo.json"
# --- END IMPORTANT CHANGE ---

# Ensure the data directory exists
data_dir.mkdir(parents=True, exist_ok=True)


# Initialize todolist. This will be loaded from the file or start as empty.
todolist = []

# Load the todolist from the JSON file if it exists
if json_file.exists():
    try:
        with open(json_file, "r", encoding='utf-8') as f:
            todolist = json.load(f)
    except json.JSONDecodeError:
        typer.echo(f"Warning: '{json_file}' contains invalid JSON. Starting with an empty todo list.")
        todolist = []
    except Exception as e:
        typer.echo(f"Error loading todo list from '{json_file}': {e}. Starting with an empty todo list.")
        todolist = []

def save_todolist():
    """Saves the current state of the todolist to the JSON file."""
    try:
        with open(json_file, "w", encoding='utf-8') as f:
            json.dump(todolist, f, indent=4) # Use indent for pretty-printing
        # typer.echo("Todo list saved successfully.") # Mute for cleaner CLI output
    except Exception as e:
        typer.echo(f"Error saving todo list: {e}")

def _reindex_ids():
    """Helper to reassign sequential IDs after items are removed."""
    for i, todo in enumerate(todolist):
        todo["id"] = i + 1

@app.command(name="add", help="Add a new task to the todo list.")
def add_task(task_name: str = typer.Argument(..., help="The task description (enclose in quotes if it contains spaces).")):
    """Add a task to the todo list."""
    task_obj = {
        "id": len(todolist) + 1, # Assign a new ID
        "task": task_name,
        "completed": False
    }
    todolist.append(task_obj)
    save_todolist()
    typer.echo(f"Task '{task_name}' added.")

@app.command(name="remove", help="Remove a task from the todo list by name or ID.")
def remove_task(task_identifier: str = typer.Argument(..., help="The task name or ID to remove (enclose in quotes if it contains spaces).")):
    """Remove a task from the todo list by name or ID."""
    original_len = len(todolist)
    
    # Try to remove by ID first (if input is numeric)
    try:
        task_id = int(task_identifier)
        todolist[:] = [todo for todo in todolist if todo["id"] != task_id]
    except ValueError:
        # If not an ID, try to remove by task name
        todolist[:] = [todo for todo in todolist if todo["task"] != task_identifier]

    if len(todolist) < original_len:
        _reindex_ids() # Reindex IDs after removal
        save_todolist()
        typer.echo(f"Task '{task_identifier}' removed.")
    else:
        typer.echo(f"Task '{task_identifier}' not found.")

@app.command(name="complete", help="Mark a task as complete by name or ID.")
def mark_complete(task_identifier: str = typer.Argument(..., help="The task name or ID to mark complete (enclose in quotes if it contains spaces).")):
    """Marks a task as complete by name or ID."""
    task_found = False
    for todo in todolist:
        # Try to match by ID first
        try:
            if todo["id"] == int(task_identifier):
                todo["completed"] = True
                task_found = True
                break
        except ValueError:
            # If not an ID, try to match by task name
            if todo["task"] == task_identifier:
                todo["completed"] = True
                task_found = True
                break
    
    if task_found:
        save_todolist()
        typer.echo(f"Task '{task_identifier}' marked as complete.")
    else:
        typer.echo(f"Task '{task_identifier}' not found.")

@app.command(name="view", help="View all tasks in the list.")
def view_list():
    """View the entire todo list."""
    if not todolist:
        typer.echo("Your todo list is empty!")
        return

    typer.echo("\n--- Your Todo List ---")
    for todo in todolist:
        status = "✅ Completed" if todo["completed"] else "❌ Pending"
        typer.echo(f"ID: {todo['id']}: {todo['task']} [{status}]")
    typer.echo("----------------------\n")


# This is the entry point for the Typer application
if __name__ == "__main__":
    app()
