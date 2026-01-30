from src.gmail_service import GmailService
from src.auth import authenticate_with_google
from src.llm_handler import get_classification_chain
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def email_manager(chain, gmail_service, next_page_token):
    messages, next_page_token = gmail_service.list_inbox_messages(max_results=50)
    emails_list = []
    for message in messages:
        emails_list.append(gmail_service.get_message_details(message["id"]))
    logging.info("Total messages retrieved : %s", len(emails_list))

    for email in emails_list:
        logging.info("Invoking chain for message ID : %s", email["Id"])
        result = chain.invoke(
            {
                "sender": email.get("From"),
                "subject": email.get("Subject"),
                "body": email.get("Body"),
            }
        )
        logging.info(
            "\n\nClassification: %s\nReason: %s\nConfidence: %s\nCategory: %s\n\n",
            result["classification"],
            result["reasoning"],
            result["confidence_score"],
            result["category"],
        )
        if result["classification"] == "remove" and result["confidence_score"] > 0.8:
            if gmail_service.trash_message(email["Id"]):
                logging.info("Email moved to trash successfully!")
            else:
                logging.info("Failed to move the email to trash")

def main():
    # Initiate authentication
    credentials = authenticate_with_google()
    logging.info("Authentication successful!")

    # Instantiate Gmail Service
    gmail_service = GmailService(credentials=credentials)

    # Get LLM chain
    chain = get_classification_chain()
    logging.info("Chain created successfully")

    page_token = None
    while True:
        user_input = input("Do you want to continue? (Y/N): ")
        if user_input.lower() == "y":
            next_page_token = email_manager(chain, gmail_service, page_token)
            page_token = next_page_token
        elif user_input.lower() == "n":
            logging.info("Exiting...")
            break
        else:
            logging.info("Incorrect input! try again")


   
        


if __name__ == "__main__":
    main()
