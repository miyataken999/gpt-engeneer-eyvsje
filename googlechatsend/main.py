import sys
from googlechatsend.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SPACE_ID
from googlechatsend.auth import Authenticator
from googlechatsend.client import GoogleChatClient

def main():
    config = {
        'CLIENT_ID': CLIENT_ID,
        'CLIENT_SECRET': CLIENT_SECRET,
        'REDIRECT_URI': REDIRECT_URI,
        'SPACE_ID': SPACE_ID,
        'TOKEN_FILE': 'token.json'
    }
    auth = Authenticator(config)
    auth.authenticate()
    client = GoogleChatClient(config, auth)
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
        client.send_message(message)
    else:
        print('Usage: python main.py <message>')

if __name__ == '__main__':
    main()