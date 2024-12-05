# Anonymous Chat Application

Python code for an event-driven system. It uses Python with RabbitMQ. It takes message as input, then `Filter Service` checks if the message contains the stop words - `[mango, ailurophobia, mango]`. If there are not stop words, the message is then collected by `Screaming Service` which makes all letters UPPERCASE. Finally, the message is sent to the specified email by `Publisher Service`.
- [Demo Video](https://youtu.be/3h-jmV_pTlk)

## Project Structure

```
├── rest_api.py
├── filter.py
├── screaming.py
├── publish.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- These python libraries - `[pika, fastapi, uvicord]`

### Running the Server

1. Navigate to the project directory.
2. Run the services:

```bash
python3 rest_api.py
python3 filter.py
python3 screaming.py
python3 publisher.py
```

3. The server will start and listen on `http://localhost:8000`.

### API Endpoints

- **POST /submit**
  - Request Body: `{"alias": "username", "message": "message"}`
  - Send message with this structure to email specified in code:
  ```
  From user: username
  Message: MESSAGE
  ```

## Repository Structure

- **`res_api.py`**: Contains REST API server logic.
- **`filter.py`**: Contains Filter Service logic
- **`screaming.pg`**: Contains Screaming Service logic.
- **`publish.py`**: Contains Publish Server logic.
- **`requirements.txt`**: Specifies the dependencies.

---
