# Task CLI Application

A simple command-line task management application that allows you to add, list, update, delete, and track the status of tasks.

## Features

- **Add tasks**: Create new tasks with descriptions
- **List tasks**: View all tasks or filter by status (todo, in-progress, done)
- **Update tasks**: Modify task descriptions
- **Delete tasks**: Remove tasks from your list
- **Track status**: Mark tasks as "in-progress" or "done"
- **Persistent storage**: Tasks are saved to a JSON file and loaded on startup

## Installation

1. Ensure you have Python 3.x installed
2. Clone or download this repository
3. No additional dependencies required beyond Python's standard library

## Usage

Run the application with:
```
python task_cli.py
```

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <description>` | Add a new task | `add Finish project report` |
| `list [status]` | List all tasks (optionally filter by status) | `list in-progress` |
| `update <id> <new_description>` | Update a task's description | `update 1 Revised project report` |
| `delete <id>` | Delete a task | `delete 1` |
| `mark-in-progress <id>` | Mark task as in-progress | `mark-in-progress 1` |
| `mark-done <id>` | Mark task as done | `mark-done 1` |
| `exit` | Exit the application | `exit` |

### Task Statuses

- `todo`: Task has not been started (default status)
- `in-progress`: Task is being worked on
- `done`: Task has been completed

## Data Storage

Tasks are automatically saved to `tasks.json` in the same directory as the script. The file is updated after each modification.

## Task Structure

Each task contains:
- Unique ID (auto-incremented)
- Description
- Status
- Creation timestamp
- Last update timestamp

## Error Handling

The application provides helpful error messages for:
- Invalid commands
- Missing parameters
- Non-existent task IDs
- Invalid ID formats
