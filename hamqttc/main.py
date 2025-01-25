import os
from hamqttc.config import load_config, setup_default_config
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    config = userdata
    script_dir = config.get('scripts_dir')
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    script_path = os.path.join(script_dir, "{}.sh".format(topic))
    if os.path.exists(script_path):
        print(f"Executing script: {script_path} with payload: {payload}")
        os.system(f"{script_path} '{payload}'")
    else:
        print(f"No script found for topic: {topic}")

def main():
    config_file = os.path.expanduser("~/.config/hamqttc/config.yml")
    # Check if config exists, otherwise create it
    if not os.path.exists(config_file):
        setup_default_config(config_file)
        print(f"Default config created at {config_file}. Please update it with your MQTT settings.")
        return
    config = load_config(config_file)
    client = mqtt.Client(userdata=config)
    client.on_message = on_message
    mqtt_host = config.get('mqtt_host', 'localhost')
    mqtt_port = config.get('mqtt_port', 1883)
    mqtt_username = config.get('mqtt_username')
    mqtt_passwd = config.get('mqtt_passwd')
    try:
        client.username_pw_set(mqtt_username, mqtt_passwd)
        client.connect(mqtt_host, mqtt_port, 60)
        client.subscribe("#")
        print(f"Connected to MQTT broker at {mqtt_host}:{mqtt_port}")
        client.loop_forever()
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")

if __name__ == "__main__":
    main()