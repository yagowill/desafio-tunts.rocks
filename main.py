from authentication import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from logic import average, situation, is_failed_for_absence

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1W4yVT1mnWXM-IfUwjBuwA4YoGjOweaacCgZNFB1zJB0"
SAMPLE_RANGE_NAME = "engenharia_de_software!A4:H27"


def main():
  creds = auth()
  if creds:
    print("Authenticated successfully")
  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    if result != None:
      print("Spreadsheet accessed successfully")
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return
    
    for row in values:
      absences = int(row[2])
      avg = average((row[3]), row[4], row[5])
      student_situation = situation(avg, absences)
      if student_situation == "Exame Final":
        print(avg)
    
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()