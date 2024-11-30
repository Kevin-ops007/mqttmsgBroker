import os
import paho.mqtt.client as mqtt
import json
from rules_engine.rules_engine import calculate_supplement


def on_subscribe(client, userdata, properties, reason_code_list):
    if reason_code_list == 128:
        print(f"Broker rejected your subscription with reason code: {reason_code_list}")
    else:
        print(f"Broker granted QoS: {reason_code_list}")


def on_message(client, userdata, message):
    data = json.loads(message.payload.decode("utf-8"))

    result = calculate_supplement(data)
    mqtt_topic = os.getenv("MQTT_TOPIC_ID")
    print(result)
    topic_output = f"BRE/calculateWinterSupplementOutput/{mqtt_topic}"
    client.publish(topic_output, json.dumps(result))


def connect_and_listen(topic_input):
    broker = "test.mosquitto.org"
    port = 1883

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            client.publish(topic_input, "aisjdij")
            client.subscribe(topic_input)
        else:
            print(f"Connection failed with code {rc}")

    client = mqtt.Client()
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_connect = on_connect
    client.connect(broker, port)

    client.loop_forever()
