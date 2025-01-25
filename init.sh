#!/bin/bash

CONFIG_FILE=\"$HOME/.config/hamqttc/config.yaml\"

echo \"Enter your MQTT broker hostname (default: localhost):\"
read MQTT_HOST
MQTT_HOST=${MQTT_HOST:-localhost}

if [ ! -f \"$CONFIG_FILE\" ]; then
    python3 -m hamqttc.main --init
fi

sed -i \"s/mqtt_host:.*/mqtt_host: $MQTT_HOST/\" \"$CONFIG_FILE\"
echo \"MQTT hostname updated to $MQTT_HOST\"
