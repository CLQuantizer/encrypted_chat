I should have a server in the middle

- Ezio generates a String with limited size
- Encrypts the String with rsa key
- Sends encypted String over to redis
- Bob subscribes to the message queue
- Bob decrypts with the same