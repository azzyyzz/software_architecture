# Assignment 2 - Anonymous Chat Application

This repository contains a simple **client-server chat application** where users can send anonymous messages. The application also exposes an endpoint to count the total number of messages sent, and getting all messages. The main focus is on **time behavior**, **recoverability**, and **maintainability**.
- [Demo Video](https://youtu.be/3h-jmV_pTlk)

## Project Structure

```
├── client.py               # Client node
├── server.py               # Server node
├── fitness_functions/                  # Fitness functionsand server
│   ├── test_maintainability.py
│   └── test_recoverability.py
│   └── test_time_behaviour.py
├── tests/                  # Unit tests for both client and server
│   ├── test_server.py
│   └── test_client.py
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Running the Server

1. Navigate to the project directory.
2. Run the server:

```bash
python3 server.py
```

3. The server will start and listen on `http://localhost:5000`.

### Running the Client

1. Open a new terminal window or tab.
2. Run the client:

```bash
python3 client.py
```

3. Follow the prompts to:
   - **Send a message** to the chat.
   - **View all messages**.
   - **Check the total number of messages** via `/messages/count`.

---

## Quality Attributes

### Time Behavior
- The server must process messages and respond to `/messages/count` requests within 100ms under normal load.
- Fitness function: Provides response time.

### Recoverability
- The system should recover from server crashes without losing previously received messages.
- Fitness function: Simulates crashes and tests recovery of messages and reconnection of clients.

### Maintainability
- The code follows **PEP8** standards and maintains low complexity. Test coverage is above 80%.
- Fitness function: Checks code quality and test coverage using `pylint` and `coverage.py`.

---

## Testing

Unit tests and fitness functions for the application are located in the `tests/` and `fitness_function` folders. 

---

## Repository Structure

- **`client.py`**: Contains the client-side logic.
- **`server.py`**: Implements the server-side logic, handling incoming messages and providing the `/messages/count` endpoint.
- **`fitness_functions/`**: Includes fitness functions.
- **`tests/`**: Includes unit tests to validate the functionality.
- **`requirements.txt`**: Specifies the dependencies.

---
