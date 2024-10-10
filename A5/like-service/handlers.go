package main

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"strconv"
)

func LikeMessage(c *gin.Context) {
	var like Like
	if err := c.ShouldBindJSON(&like); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	userID, err := GetUserIDByUsername(like.Username)
	if err != nil {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "User not registered"})
		return
	}

	err = InsertLike(userID, like.MessageID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not like message"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "Liked successfully"})
}

func GetLikes(c *gin.Context) {
	messageIDStr := c.Param("message_id")

	messageID, err := strconv.Atoi(messageIDStr)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid message ID"})
		return
	}

	likeCount, err := FetchLikeCount(messageID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not retrieve like count"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"messageID": messageID, "likeCount": likeCount})
}
