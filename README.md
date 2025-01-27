# Home Assistant MQTT Client

**hamqttc** is a Python-based MQTT client designed to allow users to execute custom scripts based on Home Assistant MQTT messages.

*note:* this package was designed to run with mosquitto broker installed on home assistant, but as it is a simple mqtt client, it will run on any mqtt broker, with or without home assistant.

## Features

- **Config file based**: Easily maintain and track your config files to deploy on any machine.
- **Lightweight**: Minimal dependencies ensure quick setup and efficient performance.

## Installation

Clone the project:
```bash
git clone git@github.com:adriencarbonaro/hamqttc.git
```

`cd` inside the project:
```bash
cd hamqttc
```

Create virtual environment:
```bash
python -m venv .venv
```

Activate virtual env:
```bash
source .venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Build the project
```bash
python -m build
```

Now that the wheel is built, you can install it inside the venv or globally (check which pip you are using):
```bash
pip install --force-reinstall --upgrade dist/hamqttc-[version]-py3-none-any.whl
```
