from authentication import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import webbrowser
from logic import average, situation, approval_grade

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
    
    students_situation = []
    students_approval_grade = []
    
    print("Reading informations...")
    
    for row in values:
      absences = int(row[2])
      avg = average((row[3]), row[4], row[5])
      student_situation = situation(avg, absences)
      
      if student_situation == "Exame Final":
        ap = approval_grade(avg)
      else:
        ap = 0
      
      students_situation.append([student_situation])
      students_approval_grade.append([ap])
    
    print("Writing results...")
    
    fill_situation = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                   range="G4", valueInputOption="USER_ENTERED",
                                   body={'values': students_situation}).execute()
    
    fill_approval_grade = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                   range="H4", valueInputOption="USER_ENTERED",
                                   body={'values': students_approval_grade}).execute()
    
    print("Spreadsheet edited successfully")
    print("Engenharia de Software - Desafio Yago Martins: https://docs.google.com/spreadsheets/d/1W4yVT1mnWXM-IfUwjBuwA4YoGjOweaacCgZNFB1zJB0/edit#gid=0")
      
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()