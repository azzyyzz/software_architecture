# Dockerfile
FROM golang:1.23 as builder
WORKDIR /app
COPY . .
RUN go build -o /like-service
EXPOSE 8083
CMD ["/like-service"]
