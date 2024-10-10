# Dockerfile
FROM golang:1.23 as builder
WORKDIR /app
COPY . .
RUN go build -o /user-service
EXPOSE 8081
CMD ["/user-service"]
