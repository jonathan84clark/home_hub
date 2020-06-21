from __future__ import print_function
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import os
import threading
import pickle
import os.path
import base64
from urllib2 import HTTPError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText

move_threshold = 50
show_images = True
imageDirectory = "C:\\Users\\jonat\\Desktop\\"
logDirectory = "C:\\Users\\jonat\\Desktop\\"
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'
# If modifying these scopes, delete the file token.pickle.
SCOPES_GMAIL = ['https://mail.google.com/']
   

def upload_file():
	gauth = GoogleAuth()
	# Try to load saved client credentials
	gauth.LoadCredentialsFile("mycreds.txt")
	if gauth.credentials is None:
		# Authenticate if they're not there
		gauth.LocalWebserverAuth()
	elif gauth.access_token_expired:
		# Refresh them if expired
		gauth.Refresh()
	else:
		# Initialize the saved creds
		gauth.Authorize()
	# Save the current credentials to a file
	gauth.SaveCredentialsFile("mycreds.txt")

	drive = GoogleDrive(gauth)
	textfile = drive.CreateFile()
	textfile.SetContentFile("C:\\Users\\jonat\\Desktop\\gpios.txt")
	textfile.Upload()

if __name__ == '__main__':
    upload_file()