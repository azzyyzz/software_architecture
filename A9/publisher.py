import smtplib
import json
import pika

def send_email(user, message):
    sender = "email@gmail.com"
    password = "password"
    recipient = ["targetemail@gmail.com"]

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        subject = f"Message from {user}"
        body = f"From user: {user}\nMessage: {message}\n"
        email_message = f"Subject: {subject}\n\n{body}"
        print(subject, body, email_message)
        server.sendmail(sender, recipient, email_message)
        print("here")

def callback(ch, method, properties, body):
    message = json.loads(body)
    send_email(message['alias'], message['message'])

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='publish_queue')

channel.basic_consume(queue='publish_queue', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
