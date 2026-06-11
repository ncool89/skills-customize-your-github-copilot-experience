# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Use FastAPI to build a REST API for managing a simple item collection, including CRUD operations, request validation, and clear JSON responses.

## 📝 Tasks

### 🛠️ Set up the FastAPI application

#### Description
Create a FastAPI app and add endpoints to list items and retrieve a specific item by ID.

#### Requirements
Completed program should:

- Create a FastAPI app instance and run it with Uvicorn
- Add a `GET /items` endpoint that returns a list of items
- Add a `GET /items/{item_id}` endpoint that returns a single item by ID
- Return JSON responses with appropriate status codes

### 🛠️ Implement create and update endpoints

#### Description
Add endpoints for creating new items and updating existing items using request bodies.

#### Requirements
Completed program should:

- Add a `POST /items` endpoint that accepts item data in the request body
- Add a `PUT /items/{item_id}` endpoint that updates an existing item
- Return the created or updated item in the response
- Use Pydantic models to validate input data

### 🛠️ Add validation and error handling

#### Description
Use FastAPI validation and error handling to ensure inputs are correct and missing items return a proper error.

#### Requirements
Completed program should:

- Define a Pydantic model for item payloads with fields such as `name`, `description`, and `price`
- Automatically validate request data and return validation errors for invalid input
- Return a `404` response when an item is not found
- Include example request/response behavior in comments or documentation
