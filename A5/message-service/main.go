package main

import (
	"log"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.POST("/message", PostMessage)
	r.GET("/messages", GetMessages)

	log.Fatal(r.Run(":8082"))
}
