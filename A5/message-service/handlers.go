package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func PostMessage(c *gin.Context) {
	var message Message
	if err := c.ShouldBindJSON(&message); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	userID, err := GetUserIDByUsername(message.Username)
	if err != nil {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "User not registered"})
		return
	}

	msgID, err := InsertMessage(userID, message.Content)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not post message"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message_id": msgID})
}

func GetMessages(c *gin.Context) {
	messages, err := FetchLastMessages()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not fetch messages"})
		return
	}

	c.JSON(http.StatusOK, messages)
}
