from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from utils import get_bigtalks
import random

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        input = turn_context.activity.text
        if input == "bigtalk" :
            output = random.choice(get_bigtalks())
            await turn_context.send_activity(f"Your question: { output }")