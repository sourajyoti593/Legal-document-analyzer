from slack_bolt import App
from slackbot.handlers import handle_query
import os

app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

@app.event("app_mention")
def message_handler(body, say):
    user = body["event"]["user"]
    text = body["event"]["text"]
    query = text.split(">")[-1].strip()  # After @botname
    response = handle_query(query)
    say(f"<@{user}> {response}")

if __name__ == "__main__":
    app.start(port=3000)
