# Flask REST API Project

This project is a Flask-based REST API designed to manage items using basic CRUD (Create, Read, Update, Delete) operations. It is implemented with a minimal in-memory data store and includes a single-page web interface built directly into the application.

---

## Features

### REST API Endpoints

1. **GET /items**
   - Fetch all items in the system.
   - **Response**:
     ```json
     {
         "1": {"id": "1", "name": "Item 1"},
         "2": {"id": "2", "name": "Item 2"}
     }
     ```

2. **GET /items/<item_id>**
   - Fetch a specific item by its unique ID.
   - **Response** (if the item exists):
     ```json
     {"id": "1", "name": "Item 1"}
     ```

3. **PUT /items/<item_id>**
   - Add or update an item with the specified ID.
   - **Request Body**:
     ```json
     {"name": "New Item Name"}
     ```
   - **Response**:
     ```json
     {
         "message": "Item added/updated",
         "item": {"id": "1", "name": "New Item Name"}
     }
     ```

4. **DELETE /items/<item_id>**
   - Delete an item by its unique ID.
   - **Response**:
     ```json
     {
         "message": "Item deleted",
         "item": {"id": "1", "name": "Item 1"}
     }
     ```

---

### Single-Page Web Interface

The application also serves a basic single-page interface with the following features:

- **Add Items**: Input a name and click "Add Item" to create a new item.
- **Update Items**: Click "Update" next to an item to change its name.
- **Delete Items**: Click "Delete" next to an item to remove it.

---

## Installation and Setup

1. **Environment Setup**:
   - Ensure Python 3.7 or higher is installed.
   - Install Flask:
     ```bash
     pip install flask
     ```

2. **Run the Application**:
   - Start the application:
     ```bash
     python app.py
     ```
   - Open your browser and navigate to:
     ```
     http://127.0.0.1:8080/
     ```

---

## Project Structure

```plaintext
.
├── app/
│   ├── __init__.py      # Initializes the Flask app
│   ├── routes.py        # Defines API routes
│   ├── models.py        # In-memory data store and logic
├── tests/
│   ├── test_routes.py   # Unit tests for the API
├── config.py            # Application configuration
├── run.py               # Entry point for the application
├── README.md            # Project documentation
├── requirements.txt     # List of dependencies
