

import time
import gspread

service_account = gspread.service_account(filename="ahd-milestone-creds.json")
sheet = service_account.open("PDF Task")
workSheet = sheet.worksheet("Form Responses 1")
lastRowChecked = int(workSheet.acell("CL1").value)
rowToCheck = lastRowChecked + 1
rowValues = workSheet.row_values(rowToCheck)
count = 0

while True:
    try:
        while rowValues:
            print(rowValues)

            workSheet.update_acell('CL1', rowToCheck)
            rowToCheck = rowToCheck + 1
            rowValues = workSheet.row_values(rowToCheck)
    except IOError as error:
        print(error)

    time.sleep(10)#checks every 10 seconds

