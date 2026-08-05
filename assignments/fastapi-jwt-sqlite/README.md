# 📘 Assignment: FastAPI Auth with JWT and SQLite

## 🎯 Objective

Build a secure FastAPI REST API with user registration, login using JWT tokens, and protected CRUD endpoints persisted in SQLite.

## 📝 Tasks

### 🛠️ Bootstrap Auth Endpoints

#### Description
Set up a FastAPI app with endpoints for user signup and login. Implement password hashing and token generation so users can authenticate safely.

#### Requirements
The completed program must:

- Create `POST /auth/signup` to register users with unique email
- Create `POST /auth/login` to validate credentials and return a JWT access token
- Hash passwords before saving to the database
- Return clear HTTP errors for invalid credentials or duplicate users

### 🛠️ Persist Data with SQLite

#### Description
Replace in-memory storage with SQLite tables for users and notes/tasks. Create database models and connect your API to persistent storage.

#### Requirements
The completed program must:

- Define SQLite models for users and at least one resource owned by users (example: notes)
- Create database tables automatically on application startup
- Save and query data using database sessions
- Keep business logic separated from route handlers where possible

### 🛠️ Protect User Resources

#### Description
Implement dependency-based authentication so only authenticated users can access protected endpoints and only manipulate their own data.

#### Requirements
The completed program must:

- Create protected endpoints for CRUD operations (example: `/notes`)
- Read and validate JWT token from `Authorization: Bearer <token>`
- Associate created records with the authenticated user
- Prevent one user from reading, updating, or deleting another user’s records

### 🛠️ Improve Reliability and API Quality

#### Description
Harden your API with validation and error handling, then verify behavior in Swagger UI and with at least a few manual test scenarios.

#### Requirements
The completed program must:

- Add Pydantic validation rules for request payloads
- Return consistent HTTP status codes (`201`, `200`, `401`, `403`, `404`, `422`)
- Document at least 3 manual test scenarios (happy path + failure cases) in code comments or a short note
- Keep endpoints organized and readable for maintainability
