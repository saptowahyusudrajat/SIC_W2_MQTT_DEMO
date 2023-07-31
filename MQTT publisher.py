import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "broker.hivemq.com"  # Replace with your MQTT broker address
broker_port = 1883  # Default MQTT port

# Create an MQTT client
client = mqtt.Client("publisher")

# Connect to the broker
client.connect(broker_address, broker_port)

while True:
    message = input("Enter your message: ")
    if message.lower() == "exit":
        break

    # Topic to publish the message
    topic = "topicSIC/MQTTdemo"  # Replace with the topic you want to use for the chat

    # Publish the message
    client.publish(topic, message)

# Disconnect from the broker
client.disconnect()