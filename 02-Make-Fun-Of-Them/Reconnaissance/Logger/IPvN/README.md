# IPvN
This tool is a simple php web script. We will be using port forwarding services, or, you can host the script into a webhosting service.

## Running The Server Locally
Prerequisite:
 - PHP CLI
 - SSH (or any port-forwarding sofware)

1. Initialize built-in php server
```sh
# Here, we use the port 8080
php -S localhost:8080
```
2. Register a port forwarding
```sh
# Using localhost.run (recommended)
ssh -R 80:localhost:8080 anyone@localhost.run
# Contributor, please add
# your preferred port-forwarding service.
# Because i never use any other lol
```
3. Done

## Paths
### /
Will echo visitor's public IP
### /json.php
Will return more detailed visitor's data
