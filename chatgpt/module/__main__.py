from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Create a Pyrogram Client instance
app = Client(
    "my_bot",
    api_id=29698700,  # Replace with your API ID
    api_hash="c08d5af866792c7f96e2de2b35ad5a34"  # Replace with your API hash
)

# Define the channel username that users need to subscribe to
channel_username = "solotreee"

# Define the handler for incoming private messages
@app.on_message(filters.incoming & filters.private)
async def private_message_handler(client, message):
    # ... Your message handling logic ...

# Start the Pyrogram Client
if __name__ == "__main__":
    app.run()
