# install Mosquitto: sudo apt-get install mosquitto mosquitto-clients
# Start the Mosquitto service: sudo systemctl start mosquitto
# Enable Mosquitto to start on boot: sudo systemctl enable mosquitto
# Install paho-mqtt on Both Raspberry Pis: pip install paho-mqtt
# In subscriber.py: 
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

broker_address = "192.168.1.100"  # Replace with the IP address of the machine running the MQTT broker
client = mqtt.Client("Subscriber")
client.connect(broker_address)
client.subscribe("test/topic")
client.on_message = on_message

client.loop_forever()
