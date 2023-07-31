import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "broker.hivemq.com"  # Replace with your MQTT broker address
broker_port = 1883  # Default MQTT port

# Callback when a message is received from the broker
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")

# Create an MQTT client
client = mqtt.Client("subscriber")

# Set the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port)

# Subscribe to the chat topic
topic = "topicSIC/MQTTdemo"  # Replace with the topic used for the chat
client.subscribe(topic)

# Start the MQTT loop to receive messages
client.loop_forever()