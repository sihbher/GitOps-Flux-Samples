import os
import time
import pika
import asyncio

#TOTAL = 100
#SLEEP = 1
#HOST = '192.168.4.165'
TOTAL = 1000
SLEEP = 1
CLIMEWORKS_RABBITMQ_SERVICE_HOST = "10.0.0.4"
RABBITMQ_USER = "guest"
RABBITMQ_PASSWORD = "guest"
PORT = 5672

async def main():
    #TOTAL = int(os.environ['TOTAL'])
    #SLEEP = int(os.environ['SLEEP'])
    #CLIMEWORKS_RABBITMQ_SERVICE_HOST = os.environ['CLIMEWORKS_RABBITMQ_SERVICE_HOST']
    #RABBITMQ_USER = os.environ['RABBITMQ_USER']
    #RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']
    #PORT = int(os.environ['PORT'])

    print("TOTAL MESSAGES: " + str(TOTAL))
    print("TIME TO SLEEP: " + str(SLEEP))
    print("CLIMEWORKS_RABBITMQ_SERVICE_HOST: " + CLIMEWORKS_RABBITMQ_SERVICE_HOST)
    print("RABBITMQ_USER: " + RABBITMQ_USER)
    print("RABBITMQ_PASSWORD: " + RABBITMQ_PASSWORD)
    print("PORT: " + str(PORT))

    #connection = pika.BlockingConnection(
    #    pika.ConnectionParameters(host=HOST))
    #if RABBITMQ_USER == "":
    #    parameters = pika.ConnectionParameters(host=CLIMEWORKS_RABBITMQ_SERVICE_HOST)
    #else:
        
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(CLIMEWORKS_RABBITMQ_SERVICE_HOST, PORT, '/', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='ads')


    for current in range (1, TOTAL):
        msg = "{'temp':34.5,'hum':69,'vibration':32}'}"
        channel.basic_publish(exchange='', routing_key='ads', body= msg)
        print(" [" + str(current) +"] Sent: '"+ msg +"'")
        time.sleep(SLEEP)


    connection.close()
    

if __name__ == "__main__":
    asyncio.run(main())