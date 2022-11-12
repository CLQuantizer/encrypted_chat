I should have a server in the middle

- Ezio generates a String with limit size
- Encrypts the String with key
- Sends encypted String over to a message queue
- Bob subscribes to the message queue
- Bob decrypts with the same