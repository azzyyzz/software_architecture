import json
import pika


stop_words = ["bird-watching", "ailurophobia", "mango"]

def callback(ch, method, properties, body):
    message = json.loads(body)
    if not any(word in message['message'] for word in stop_words):
        ch.basic_publish(exchange='', routing_key='filtered_queue', body=body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='message_queue')
channel.queue_declare(queue='filtered_queue')

channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
