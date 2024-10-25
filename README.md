# Flask Todo App with Database and Authentication

This project is a simple Flask-based Todo app with authentication and database integration. Users can create an account, log in, and manage their personal todo lists. The app features user-specific tasks, authentication via Flask-Login, and database storage using SQLAlchemy.

## Features

- User registration and authentication
- Create, view, and complete tasks
- Remove tasks from the todo list (you will add this)
- Set and see task priorities (Low, Medium, High)

## Getting Started

### Prerequisites

To run this app locally, you'll need the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

### Installation

1. **Clone the repository** from GitHub:
    ```bash
    git clone https://github.com/nalmadi/Flask-todo-db-auth.git
    cd Flask-todo-db-auth
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```


4. **Run the app**:
    ```bash
    flask run
    ```
    or 
    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://localhost:5000`.


6. Add a feature to remove a task from the todo list, this involves the following steps:
    - Modify todo.html to add a link to remove (similar to check)
    - Modify views.html to add a view for removing a task (similar to check)

7. When finished, modify the database to add a priority column that stores a string like low, medium, or high.  Add the necessary code to allow users to set priority and see the priority of each task the todo list.
