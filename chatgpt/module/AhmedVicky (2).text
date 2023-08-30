from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Create a Pyrogram Client instance
app = Client(
    "my_bot",
    api_id= 29698700,  # Replace with your API ID
    api_hash="c08d5af866792c7f96e2de2b35ad5a34"  # Replace with your API hash
)

# Define the channel username that users need to subscribe to
channel_username = "solotreee"

# Define the handler for incoming private messages
@app.on_message(filters.incoming & filters.private)
async def private_message_handler(client, message):
    # Check if the user is subscribed to the channel
    is_subscribed = await client.get_chat_member(channel_username, message.from_user.id)
    if is_subscribed.status == "member" or is_subscribed.status == "administrator" or is_subscribed.status == "creator":
        # User is subscribed, proceed with handling the message
        await client.send_message(message.chat.id, "Thank you for subscribing! You can continue chatting.")
    else:
        # User is not subscribed, send a message with a subscription button
        await client.send_message(
            message.chat.id,
            f"Please subscribe to @{channel_username} to access this chat.",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("Subscribe Now", url=f"https://t.me/{channel_username}")
                ]]
            )
        )

# Start the Pyrogram Client
app.run()
