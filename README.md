# hw_5 Project

This is a Django project named `hw_5` which includes a `todos` application for managing to-do items.

## Project Structure

```
hw_5/
├── hw_5/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── todos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hw_5
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- The `todos` application allows users to manage their to-do items.
- Endpoints include:
  - `GET /login/` - Display login form
  - `POST /login/` - Process login
  - `GET /logout/` - Log out the user
  - `GET /todos/` - List all to-do items
  - `GET /todos/<id>/` - Retrieve a specific to-do item
  - `POST /todos/` - Create a new to-do item
  - `DELETE /todos/<id>/delete` - Delete a specific to-do item

## Templates and Static Files

- Templates are organized in the `templates/` directory:
  - `templates/base.html` - Main template for pages
  - `templates/header.html` - Header template for pages

- Static files are stored in the `static/` directory, including CSS and JavaScript files, such as Bootstrap.