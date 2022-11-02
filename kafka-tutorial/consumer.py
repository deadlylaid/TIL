from json import loads
from kafka import KafkaConsumer
from pymongo import MongoClient

"""
commit / offset

consumer는 poll 호출마다 producer로부터 읽지 않은 메시지를 당겨옴

읽지 않은 메시지가 어디서부터인지 알 수 있는 이유는 메시지를 어디까지 가져왔는지 알수 있기 때문이다.
consumer 그룹의 consumer들은 각자 자기가 읽은 메시지의 위치정보인 offset을 갖고 있다.
한마디로 offset에는 메시지를 어디까지 읽었는지에 대한 정보가 담겨있는 것이다.

그리고 각 파티션에 대해서 현재 offset을 저장하는 행동을 commit이라고 한다.

각각의 파티션 별로 offset 정보를 저장할 저장소가 필요하다.
옛날 버전의 kafka는 이를 주키퍼에 저장했지만, 새 버전에서는 성능 문제로 독자적인 토픽을 만들어서 저장한다.
"""
my_consumer = KafkaConsumer(
    'testnum',
    api_version=(0, 11, 5),
    bootstrap_servers=['localhost : 9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

my_client = MongoClient('localhost:27017')
my_collection = my_client.testnum.testnum

for message in my_consumer:
    message = message.value
    my_collection.insert_one(message)
    print(message + " added to " + my_collection)
