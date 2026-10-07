from src.gmail_client import get_gmail_service

service = get_gmail_service()
profile = service.users().getProfile(userId="me").execute()

print("Connected as:", profile["emailAddress"])
print("Total messages:", profile["messagesTotal"])