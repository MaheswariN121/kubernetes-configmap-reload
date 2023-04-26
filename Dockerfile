# Use a Python 3 base image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install -r requirements.txt

# Set the environment variable for the Telegram bot token
ENV BOT_TOKEN=6227110303:AAGQxtr1OCXC_iddfxrorR08K0LmhXHF3Zw

# Run the command to start the bot
CMD [ "python", "bot.py" ]
