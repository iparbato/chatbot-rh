# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from openai import OpenAI
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    def __init__(self):
        # Initialize the OpenAI client from OpenRouter
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )

    async def on_message_activity(self, turn_context: TurnContext):
        # Get the user's message
        user_message = turn_context.activity.text

        # Add the user's message to the conversation history
        self.conversation_history.append({"role": "user", "content": user_message})

        # Use the OpenRouter Gemma 2 model to generate a response
        completion = self.client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
            },
            model="openai/gpt-3.5-turbo",
            messages=self.conversation_history
        )

        # Add the generated response to the conversation history
        self.conversation_history.append({"role": "assistant", "content": completion.choices[0].message.content})

        # Send the generated response back to the user
        await turn_context.send_activity(completion.choices[0].message.content)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
                # Reset the conversation history for the new user
                self.conversation_history = []