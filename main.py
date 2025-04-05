from chat_logger.logger import ChatLogger

def start_chat():
    logger = ChatLogger()

    # Simulating a chat session
    while True:
        user_input = input("Your input: ")
        if user_input.lower() == "exit":
            print("Ending chat.")
            break
        
        # Log user message
        logger.log_message(user_input, sender="User")
        
        # Simulating a response from the chatbot
        chatbot_response = "This is a chatbot response."
        logger.log_message(chatbot_response, sender="Chatbot")
        print(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    start_chat()

