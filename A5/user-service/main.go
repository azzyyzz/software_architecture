package main

import (
	"log"

	"github.com/gin-gonic/gin"
)

func main() {

	r := gin.Default()
	r.POST("/register", RegisterUser)
	r.GET("/user/:username", GetUser)

	log.Fatal(r.Run(":8081"))
}
