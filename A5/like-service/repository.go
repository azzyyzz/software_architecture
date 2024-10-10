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

func InsertLike(userID, messageID int) error {
	_, err := db.Exec("INSERT INTO likes (user_id, message_id) VALUES ($1, $2)", userID, messageID)
	return err
}

func FetchLikeCount(messageID int) (int, error) {
	var count int
	err := db.QueryRow("SELECT COUNT(*) FROM likes WHERE message_id = $1", messageID).Scan(&count)
	return count, err
}

func GetUserIDByUsername(username string) (int, error) {
	var userID int
	err := db.QueryRow("SELECT id FROM users WHERE username = $1", username).Scan(&userID)
	return userID, err
}
