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

## Prerequisites

- Python 3.12 or higher
- MySQL database
- FastAPI
- Uvicorn

