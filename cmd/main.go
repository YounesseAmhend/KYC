package main

import (
	"gin/views"
	"github.com/gin-gonic/gin"
)

func main() {

	router := gin.Default()

    router.LoadHTMLGlob("templates/*")

	// router 
	router.GET("/ping", views.Ping)
	router.GET("/", views.Index)
	router.GET("/:name", views.Name)

	router.Run("127.0.0.1:8080") // http://127.0.0.1:8080

}
