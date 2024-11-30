import os
from dotenv import load_dotenv
from rules_engine.broker import connect_and_listen


def main():
    load_dotenv()
    topic_input_base = "BRE/calculateWinterSupplementInput"
    topic_id = os.getenv("MQTT_TOPIC_ID")

    if not topic_id:
        raise ValueError("Environment variable 'MQTT_TOPIC_ID' is not set or invalid")

    topic_input = f"{topic_input_base}/{topic_id}"
    print(f"Listening on topic: {topic_input}")

    connect_and_listen(topic_input)


if __name__ == "__main__":
    main()
