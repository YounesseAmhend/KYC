.PHONY: main

main:
	go build cmd/main.go
	./main

init:
	go mod init gin
	go mod tidy
	go get github.com/gin-gonic/gin