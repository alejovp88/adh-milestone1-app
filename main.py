# import os.path
#
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
#
# SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
#
# SPREADSHEET_ID = "1tramso68YqQeJC4IVHHC4rOCZQ3Y7UbgJMHRytnGnZw"
#
# def main():
#     credentials = None
#     if os.path.exists("token.json"):
#         credentials = credentials.from_authorized_user_file("token.json", SCOPES)
#     if not credentials or not credentials.valid:
#         if credentials and credentials.expired and credentials.refresh_token:
#             credentials.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file("ahd-milestone-creds.json", SCOPES)
#             credentials = flow.run_local_server(port=0)
#         with open("token.json", "w") as token:
#             token.write(credentials.to_json())
#
#     try:
#         service = build("sheets", "v4", credentials=credentials)
#         sheets = service.spreadsheets()
#
#         for row in range(2, sheets.count()):
#             num1 = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Form Responses 1!A{row}").execute().get("values")[0][0]
#     except HttpError as error:
#         print(error)
#
#
# if __name__ == '__main__':
#     main()
import time
import gspread

service_account = gspread.service_account(filename="ahd-milestone-creds.json")
sheet = service_account.open("PDF Task")
workSheet = sheet.worksheet("Form Responses 1")
rowCount = int(workSheet.acell("CL1").value)
rowValues = workSheet.row_values(rowCount)
count = 0

while True:
    try:
        while rowValues:
            print(rowValues)
            rowCount = rowCount + 1
            rowValues = workSheet.row_values(rowCount)
            workSheet.update("CL1", rowCount)
    except:
        print("Something went wrong")

    time.sleep(10)#checks every 10 seconds
    count = count + 1
    if count == 2:
        break

