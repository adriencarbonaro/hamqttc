import os
import subprocess

from config import Config
from log import Log
import paho.mqtt.client as mqtt

logger = Log()

def onMessage(client, userdata, msg):
    config = userdata
    scripts_dir = config.get('scripts_dir')
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    logger.log(f"Received message on topic: {topic}")
    topics_scripts = config.get('topics_scripts')
    for topic_script in topics_scripts:
        if topic_script['topic'] == topic:
            script_path = os.path.join(scripts_dir, topic_script['script'])
            if os.path.exists(script_path):
                logger.log(f"Executing script: {os.path.basename(script_path)} with payload: {payload}")
                subprocess.run([script_path, topic, payload])
            else:
                logger.log(f"Script not found: {script_path}")

def mqttConnect(client, config):
    try:
        mqtt_config = config.get('mqtt_config')
        mqtt_host = mqtt_config.get('host')
        mqtt_port = int(mqtt_config.get('port'))
        mqtt_username = mqtt_config.get('username')
        mqtt_password = mqtt_config.get('password')
    except Exception as e:
        logger.log(f"Error getting config: {e}")
        return 1

    try:
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(mqtt_host, mqtt_port, 60)
    except Exception as e:
        logger.log(f"Failed to connect to MQTT broker: {e}")
        return 1
    logger.log(f"Connected to MQTT broker at {mqtt_host}:{mqtt_port}")
    return 0

def main():
    logger.log("Starting hamqttc")
    config = Config(logger)
    config_file = os.path.expanduser("~/.config/hamqttc/config.yml")
    config.check(config_file)
    config_dict = config.load(config_file)
    logger.setup(config_dict['log_file'])
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata=config_dict)
    client.on_message = onMessage
    if mqttConnect(client, config_dict) != 0:
        return

    try:
        topics = []
        topics_scripts = config_dict.get('topics_scripts')
        if topics_scripts == None:
            raise Exception("Config key not found: topics_scripts")
        for topic_script in topics_scripts:
            topic = topic_script['topic']
            if (topic not in topics):
                topics.append(topic)
        logger.log(f"Subscribing to {len(topics)} topics : {topics}")
        for topic in topics:
            client.subscribe(topic)
        client.loop_forever()
    except Exception as e:
        logger.log(f"MQTT Error: {e}")

if __name__ == "__main__":
    main()
