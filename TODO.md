This project launches a mqtt client that subscribes to mqtt server and executes scripts accroing to received messages.
When installed:
  - the module creates a $HOME/.config/hamqttc directory containing a config file and a script directory.
  - it launches a simple tui program that asks user for the hostname, adding that it can be changed later
The progam is launched with an executable installed alongside the module, called `hamqttc`


```yaml
config:
  host: "ip_addr:port"
  script_dir: "scripts/"
  messages:
    message_1: script_1
    ...
```

- Add logs to monitor errors
