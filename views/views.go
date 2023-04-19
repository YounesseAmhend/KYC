package views

import (
	"github.com/gin-gonic/gin"
 	"net/http"
	"strings"
)


func Index(context *gin.Context) {
	var joe Client = Client{12, "Joe"}
	context.HTML(http.StatusOK, "index.tmpl", gin.H{
		"title": joe.name ,
	})
}

func Ping(context *gin.Context) {
	context.JSON(200, gin.H{
		"message": "pong",
	})
}
func Name(context *gin.Context) {
	name := context.Params.ByName("name")
	name = strings.Title(name) 
	context.HTML(http.StatusOK, "hello.tmpl", gin.H{
		"name": name,
	})
}