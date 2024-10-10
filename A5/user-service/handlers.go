package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func RegisterUser(c *gin.Context) {
	var user User
	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	var existingID int
	err := db.QueryRow("SELECT id FROM users WHERE username = $1", user.Username).Scan(&existingID)
	if err == nil {
		c.JSON(http.StatusOK, gin.H{"user_id": existingID})
		return
	}

	id, err := InsertUser(user.Username)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not register"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"user_id": id})
}

func GetUser(c *gin.Context) {
	username := c.Param("username")

	user, err := FetchUser(username)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "User not found"})
		return
	}

	c.JSON(http.StatusOK, user)
}
