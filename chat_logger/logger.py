import datetime
import os

class ChatLogger:
    def __init__(self, log_file="logs/chat_log.txt"):
        self.log_file = log_file

        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    def log_message(self, message, sender="User"):
        # Get the current date and time for timestamp
        timestamp = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

        # Format the message
        log_entry = f"{timestamp} - {sender}: {message}\n"

        # Write the log entry to the file
        with open(self.log_file, "a") as file:
            file.write(log_entry)

    def show_logs(self):
        with open(self.log_file, "r") as file:
            print(file.read())

# Example usage:
if __name__ == "__main__":
    logger = ChatLogger()

    # Log some messages
    logger.log_message("Hello, chatbot!", sender="User")
    logger.log_message("Hi, how can I help you today?", sender="Chatbot")

    # Print out the logs
    logger.show_logs()
