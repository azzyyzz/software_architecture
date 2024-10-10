# Software Architecure A5

A simple Twitter-like system implemented in Go using Gin and PostgreSQL. Users can register, post messages, read messages, and like them.

## Features

- User registration
- Posting messages
- Reading the latest 10 messages
- Liking messages


## Requirements

- Docker
- PostgreSQL

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/azzyyzz/software_architecture.git
   cd software_architecture/A5
2. **Build and Run the Service**
   ```bash
   docker-compose up --build

## API Endpoints

### User Service (Port 8081)

- **POST /register**
  - Request Body: `{"username": "testuser"}`
  - Registers a new user.

- **GET /user/:username**
  - Retrieves user information.

### Message Service (Port 8082)

- **POST /message**
  - Request Body: `{"username": "testuser", "content": "Hello, world!"}`
  - Posts a new message.

- **GET /messages**
  - Retrieves the latest 10 messages, including the like count.

### Like Service (Port 8083)

- **POST /like**
  - Request Body: `{"username": "testuser", "message_id": 1}`
  - Likes a message.

- **GET /likes/:message_id**
  - Retrieves the count of likes for a specific message.
