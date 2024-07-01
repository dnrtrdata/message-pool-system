
from datetime import datetime

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()

class MessagePool:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages
