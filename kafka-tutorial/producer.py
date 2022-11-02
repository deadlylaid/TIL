# importing the required libraries
from time import sleep
from json import dumps
from kafka import KafkaProducer

# initailzing kafka
my_producer = KafkaProducer(
    api_version=(0, 11, 5),
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# generating the numbers ranging from 1 to 500
for n in range(500):
    my_data = {'num': n}
    print('send ', n)
    my_producer.send('testnum', value=my_data)
    print('done ', n)
    sleep(5)
