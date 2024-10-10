package main

import (
	"database/sql"

	_ "github.com/lib/pq"
)

var db *sql.DB

func init() {
	var err error
	db, err = sql.Open("postgres", "user=user password=password dbname=twitter_db host=postgres sslmode=disable")
	if err != nil {
		panic(err)
	}
	createTableSQL := `
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL
    );`

	_, err = db.Exec(createTableSQL)
	if err != nil {
		panic(err)
	}
	createMessagesTableSQL := `
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        content VARCHAR(400) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );`

	_, err = db.Exec(createMessagesTableSQL)
	if err != nil {
		panic(err)
	}
	createLikesTableSQL := `
    CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        message_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (user_id, message_id),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (message_id) REFERENCES messages(id) ON DELETE CASCADE
    );`

	_, err = db.Exec(createLikesTableSQL)
	if err != nil {
		panic(err)
	}
}

func InsertUser(username string) (int, error) {
	var id int
	err := db.QueryRow("INSERT INTO users (username) VALUES ($1) RETURNING id", username).Scan(&id)
	return id, err
}

func FetchUser(username string) (User, error) {
	var user User
	err := db.QueryRow("SELECT id, username FROM users WHERE username = $1", username).Scan(&user.ID, &user.Username)
	return user, err
}
