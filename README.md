# send_message_from_telegram_bot

**Title:** Telegram Bot (🤖) for Sending Messages to Multiple Channels/Users

**Description:**

This Python script provides a simple Telegram bot that allows you to send messages to multiple pre-configured channels or individual users. 
Of course, just for Fan 😜🤖.

**Features:**

- Supports sending messages to both channels and individual users.
- User-friendly interface for selecting chat and bot.
- Input validation for chat and bot selection.
- Error handling for potential network issues and unexpected exceptions.
- Clean code structure for readability and maintainability.

**Installation:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/M2007Taha/telegram-bot-sender.git
   ```

2. **Install dependencies:**

   ```bash
   pip install requests
   ```

**Usage:**

1. **Replace placeholders:**

   - Update the `self.chats` dictionary with the Telegram chat IDs and names of channels or users you want to send messages to .
   - Replace `"YOUR_BOT_TOKEN_1"`, `"YOUR_BOT_TOKEN_2"`, etc. in the `self.bots` dictionary with your actual Telegram bot tokens (obtained from @BotFather).

2. **Run the script:**

   ```bash
   python telegram_bot_sender.py
   ```

3. **Select chat and bot:**

   - The script will prompt you to choose a chat (channel or user) and a bot (identified by its username).

4. **Send messages:**

   - Type your message and press Enter.
   - You can continue sending messages until you type "!exit" to quit.

**Important Notes:**

- **Telegram Bot Tokens:** Ensure you replace the placeholders in `self.bots` with your actual bot tokens.
- **API Rate Limits:** Be mindful of Telegram's API rate limits to avoid exceeding your quota. You can find more information in the Telegram Bot API documentation ([https://core.telegram.org/](https://core.telegram.org/)).
- **Security:** This script stores bot tokens directly in the code. For production use, consider storing tokens securely in environment variables or a configuration file.

**Additional Considerations:**

- **Command-line arguments:** Enhance the script by accepting chat and bot IDs as command-line arguments for more flexibility.
- **Logging:** Implement logging to track user interactions, errors, and successful messages.
- **Configuration file:** Consider storing chat and bot information in a separate configuration file to avoid modifying the code directly.

**Getting Chat ID:**
To find the chat ID for a channel or user, you can use the [@RawDataBot](You can use @RawDataBot bot to get chat ID). Simply send a message to this bot and it will respond with your chat ID information.

By following these steps and incorporating the suggestions, you can effectively use this Telegram bot to send messages to your desired channels and users.
