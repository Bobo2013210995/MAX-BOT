from max import MaxClient as Client
from filters import filters
from classes import Message
import time

client = Client()
client.auth("+79258933314")  # Replace with your phone number
print(client.auth_token)  # Prints the obtained token
client.run()