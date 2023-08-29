import asyncio
import os
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError

load_dotenv(".env")

client = WebClient(
    token=os.environ['BOT_TOKEN'],
    run_async=True
)
future = client.chat_postMessage(
    channel='bot-test',
    text="Zdarova, epta"
)

loop = asyncio.get_event_loop()
try:
    # run_until_complete returns the Future's result, or raise its exception.
    response = loop.run_until_complete(future)
    assert response["message"]["text"] == "Zdarova, epta"
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
finally:
    loop.close()
