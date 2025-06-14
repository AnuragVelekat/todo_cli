# 📝 Simple Todo CLI Application

**This is my \*\***first Command-Line Interface (CLI) application** built with Python! It's a simple todo list manager that runs right from your terminal. I used [**Typer\*\*](https://typer.tiangolo.com/ "null"), a powerful and intuitive library that makes building CLIs easy with Python's type hints.

## ✨ Features

- **Add Tasks:** Quickly add new todo items.
- **Remove Tasks:** Delete tasks by name or ID.
- **Mark Complete:** Mark tasks as finished.
- **View List:** See all your tasks and their status.
- **Persistent Storage:** Tasks are saved to `<span class="selected">todo.json</span>` in your home directory, so they're always there.

## 🚀 How to Use

**Once installed, use the **`<span class="selected">todo</span>` command followed by subcommands:

### Main Help

```
todo --help

```

### Add a Task

```
todo add "Buy groceries"

```

### View Tasks

```
todo view

```

## --- Your Todo List ---

ID: 1: Buy groceries [❌ Pending]

````

### Mark a Task as Complete
```bash
todo complete "Buy groceries"
# Or by ID:
todo complete 1

````

### Remove a Task

```
todo remove "Buy groceries"
# Or by ID:
todo remove 1

```

## 🛠️ Installation (Windows)

### Prerequisites

- **Python 3.8+** **: Installed with "Add Python to PATH" checked.**
- **pip** **: Python's package installer.**

### Steps

1. **Get `<span class="selected">todo.py</span>` & Install Typer:**

   - **Create a folder, e.g., **`<span class="selected">C:\my_cli_tools\</span>`. Save `<span class="selected">todo.py</span>` inside it.
   - **Open your command prompt (**`<span class="selected">cd C:\my_cli_tools\</span>`) and run:

     ```
     pip install "typer[all]"

     ```

2. **Create `<span class="selected">todo.bat</span>`:**

   - **In the \*\***same directory\*\* as `<span class="selected">todo.py</span>`, create a file named `<span class="selected">todo.bat</span>`.
   - **Add this line to **`<span class="selected">todo.bat</span>`:

     ```
     @python "%~dp0todo.py" %*

     ```

3. **Add Directory to PATH:**
   - **Search "Environment Variables" in Windows.**
   - **Go to "Environment Variables..." -> "System variables" -> **`<span class="selected">Path</span>` -> "Edit...".
   - **Click "New" and add the full path to your folder (e.g., **`<span class="selected">C:\my_cli_tools\</span>`).
   - **Click "OK" on all windows.**
   - **Crucial:** Close and reopen your Command Prompt or PowerShell for changes to apply.

## 📁 Project Structure

```
your-cli-tools-directory/
├── todo.py
├── todo.bat
└── .todo_app_data/
    └── todo.json

```

**Your **`<span class="selected">todo.json</span>` file will be in `<span class="selected">C:\Users\YourUser\.todo_app_data\todo.json</span>`.

## 💡 Learning & Reflection

**This project was a great introduction to:**

- **Building command-line tools.**
- **Using Typer for clean, type-hinted CLI development.**
- **Managing data persistence with JSON.**
- **Setting up CLI commands on Windows.**

## 🙌 Contributing

**Feel free to fork, open issues, or submit pull requests!**

## 📄 License

**This project is open-source under the **[MIT License](LICENSE "null").
