import json
import pika

def callback(ch, method, properties, body):
    message = json.loads(body)
    message['message'] = message['message'].upper()
    ch.basic_publish(exchange='', routing_key='publish_queue', body=json.dumps(message))

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='filtered_queue')
channel.queue_declare(queue='publish_queue')

channel.basic_consume(queue='filtered_queue', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
