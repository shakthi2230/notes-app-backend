# Notes Application API

This is a simple REST API for managing users and notes built using **FastAPI**. The application allows users to register, authenticate, and create, retrieve, update, and delete notes.

## Project Structure

- **`authentication.py`**: Contains the authentication logic for handling password hashing, token generation, and user validation.
- **`models`**: Contains the models used to interact with the database (e.g., `UserModel`, `NotesModel`).
- **`routers`**: Contains the API route handlers (e.g., `user.py`, `notes.py`).
- **`schema`**: Contains the request and response schemas for API validation (e.g., `user.py`, `notes.py`).
- **`core/config.py`**: Stores application configuration such as the secret key and algorithm used for JWT encoding.

## Features

- User registration and login
- JWT-based authentication
- Create, retrieve, update, and delete notes for authenticated users

## Tech Stack

- Backend Framework: FastAPI
- Database: MySQL
- Authentication: JWT (via python-jose)
- Password Hashing: bcrypt (via passlib)
- Environment Configuration: .env file (via python-dotenv)

## Installation

### Prerequisites

- Python 3.12 or higher
- MySQL database
- FastAPI
- Uvicorn

### steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/notes-app-api.git
   cd notes-app-api

   ```

2. **Set up a Virtual Environment:**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

   ```

3. **Install Dependencies:**:

   ```bash
   pip install -r requirements.txt

   ```

4. **Set Up the Database: Create a MySQL database::**:

   ```bash
     mysql -u root -p
    CREATE DATABASE db_name;
   ```

- Update the .env file with your database credentials:

  ```bash
  DB_HOST=localhost
  DB_USER=root
  DB_PASSWORD=yourpassword
  DB_DATABASE=db_name
  DB_PORT=3306
  ```

5. **Run Database Migrations (if any): Use the provided database connection file to initialize tables:**:

   ```bash
   python initialize_db.py


   ```

## Running the Application:

```bash
uvicorn main:app --reload

```



## API Endpoints

#### Users
| Method | Endpoint       | Description                   | Sample Request Body                      | Sample Response                                      |
|--------|----------------|-------------------------------|------------------------------------------|-----------------------------------------------------|
| POST   | `/user/signup` | Register a new user           | `{ "user_name": "John Doe", "user_email": "john@example.com", "password": "secure123" }` | `{ "user_id": "12345", "message": "User registered successfully" }` |
| POST   | `/user/login`  | Authenticate and get a token  | `{ "email": "john@example.com", "password": "secure123" }` | `{ "access_token": "eyJhbGciOiJIUzI1...", "token_type": "bearer" }` |

---

#### Notes
| Method | Endpoint           | Description                      | Sample Request Body                       | Sample Response                                      |
|--------|--------------------|----------------------------------|-------------------------------------------|-----------------------------------------------------|
| POST   | `/notes/`          | Create a new note               | `{ "note_title": "Meeting Notes", "note_content": "Discuss project roadmap" }` | `{ "note_id": "abc123", "message": "Note created successfully" }` |
| GET    | `/notes/`          | Retrieve all notes for the user | None                                      | `{ "notes": [{ "note_id": "abc123", "note_title": "Meeting Notes", "note_content": "Discuss project roadmap", "last_update": "2024-11-26T12:34:56", "created_on": "2024-11-25T11:00:00" }] }` |
| PUT    | `/notes/`          | Update an existing note         | `{ "note_id": "abc123", "note_title": "Updated Meeting Notes", "note_content": "Updated content" }` | `{ "message": "Note updated successfully" }` |
| DELETE | `/notes/{note_id}` | Delete a note by its ID         | None                                      | `{ "message": "Note deleted successfully" }` |

---

### Notes
- **Authentication**: All endpoints except `/user/signup` and `/user/login` require a valid JWT token in the `Authorization` header:

