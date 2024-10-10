# Dockerfile
FROM golang:1.23 as builder
WORKDIR /app
COPY . .
RUN go build -o /message-service
EXPOSE 8082
CMD ["/message-service"]
