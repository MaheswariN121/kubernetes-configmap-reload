# Use the official Python image as the parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python modules
RUN pip install telebot requests

# Set the environment variable for the bot token
ENV BOT_TOKEN="6227110303:AAGQxtr1OCXC_iddfxrorR08K0LmhXHF3Zw"

# Run the command to start the bot
CMD [ "python", "bot.py" ]
