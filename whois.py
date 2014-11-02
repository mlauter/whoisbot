import zulip
import sys

# Keyword arguments 'email' and 'api_key' are not required if you are using ~/.zuliprc
client = zulip.Client(email="othello-bot@example.com",
                      api_key="a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5")

# Send a stream message
client.send_message({
    "type": "stream",
    "to": "Denmark",
    "subject": "Castle",
    "content": "Something is rotten in the state of Denmark."
})
# Send a private message
client.send_message({
    "type": "private",
    "to": "hamlet@example.com",
    "content": "I come not, friends, to steal away your hearts."
})

# Print each message the user receives
# This is a blocking call that will run forever
client.call_on_each_message(lambda msg: sys.stdout.write(str(msg) + "\n"))

# Print every event relevant to the user
# This is a blocking call that will run forever
# This will never be reached unless you comment out the previous line
client.call_on_each_event(lambda msg: sys.stdout.write(str(msg) + "\n"))