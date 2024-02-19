from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging

def login(service_account_file):
    creds = service_account.Credentials.from_service_account_file(service_account_file)
    service = build('sheets', 'v4', credentials=creds)
    return service
