package main

import (
	"log"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.POST("/like", LikeMessage)
	r.GET("/likes/:message_id", GetLikes)

	log.Fatal(r.Run(":8083"))
}
