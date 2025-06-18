# FastAPI Task Management API

This is a simple RESTful API written using the FastAPI framework that allows for managing tasks.

## Data Model

The Task data model is defined using the Pydantic library and includes the following fields:

- `id` (int): The unique identifier for the task.
- `title` (str): The title of the task.
- `description` (str): The description of the task.
- `done` (bool): The state of the task. `True` if the task is completed and `False` otherwise.

## API Endpoints

### `POST /tasks/`

Create a new task.

**Parameters:**

- `task` (Task): The task object to be created.

**Example of usage:**

```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Buy milk and eggs",
    "done": False
}
```

**Returns:**

The created task object.

### `GET /tasks/`

Retrieve all tasks.

**Parameters:**

None

**Example of usage:**

```python
GET /tasks/
```

**Returns:**

A list of all tasks.

### `GET /tasks/{task_id}`

Retrieve a specific task by its id.

**Parameters:**

- `task_id` (int): The unique identifier of the task to be retrieved.

**Example of usage:**

```python
GET /tasks/1
```

**Returns:**

The task object if found. If not, it raises a `404 HTTPException` with the detail "Task not found".

### `PUT /tasks/{task_id}`

Update a specific task by its id.

**Parameters:**

- `task_id` (int): The unique identifier of the task to be updated.
- `task` (Task): The task object with updated fields.

**Example of usage:**

```python
PUT /tasks/1
{
    "title": "Buy groceries",
    "description": "Buy milk, eggs and bread",
    "done": True
}
```

**Returns:**

The updated task object if found. If not, it raises a `404 HTTPException` with the detail "Task not found".

### `DELETE /tasks/{task_id}`

Delete a specific task by its id.

**Parameters:**

- `task_id` (int): The unique identifier of the task to be deleted.

**Example of usage:**

```python
DELETE /tasks/1
```

**Returns:**

A message "Task has been deleted successfully!" if the task is found and deleted. If not, it raises a `404 HTTPException` with the detail "Task not found".

## Important Notes

All the endpoints that require a `task_id` will raise a `404 HTTPException` with the detail "Task not found" if there is no task with the provided id.

## Dependencies

This API requires the following libraries:

- FastAPI
- Pydantic
- typing
- HTTPException from FastAPI