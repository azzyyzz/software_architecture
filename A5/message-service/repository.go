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

}

func GetUserIDByUsername(username string) (int, error) {
	var userID int
	err := db.QueryRow("SELECT id FROM users WHERE username = $1", username).Scan(&userID)
	return userID, err
}

func InsertMessage(userID int, content string) (int, error) {
	var msgID int
	err := db.QueryRow("INSERT INTO messages (user_id, content) VALUES ($1, $2) RETURNING id", userID, content).Scan(&msgID)
	return msgID, err
}

func FetchLastMessages() ([]Message, error) {
	rows, err := db.Query(`
        SELECT messages.id, messages.content, messages.created_at, users.username,
		COALESCE((SELECT COUNT(*) FROM likes WHERE message_id = messages.id), 0) AS like_count 
        FROM messages
        JOIN users ON messages.user_id = users.id
        ORDER BY messages.created_at DESC
        LIMIT 10;
    `)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var messages []Message
	for rows.Next() {
		var message Message
		if err := rows.Scan(&message.ID, &message.Content, &message.CreatedAt, &message.Username, &message.LikeCount); err != nil {
			return nil, err
		}
		messages = append(messages, message)
	}
	return messages, nil
}
