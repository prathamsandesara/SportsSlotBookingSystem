import gspread
from google.auth import exceptions
from google.oauth2.service_account import Credentials

class DataManagement:
    def __init__(self, credentials_path, spreadsheet_name):
        try:
            self.gc = gspread.service_account(filename=credentials_path) 
            #using a service account for google spreadsheets
            self.spreadsheet_name = spreadsheet_name
            self.worksheet = self.gc.open(spreadsheet_name).sheet1
        except exceptions.GoogleAuthError as e:
            print(f"Google Authentication Error: {e}")
    
    def save_to_google_sheets(self, data):
        try:
            self.worksheet.append_row(list(data.values()))
            print("Data saved to Google Sheets successfully!")
        except gspread.exceptions.APIError as e:
            print(f"Error saving to Google Sheets: {e}")
    def authorize(self):
        try:
            credentials = Credentials.from_service_account_file(self.credentials_path, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
            return gspread.authorize(credentials)
        except exceptions.GoogleAuthError as e:
            print(f"Google Auth Error: {e}")
            return None


    def user_has_booked(self, au_id, selected_date, sport):
        try:
            existing_booking = self.worksheet.findall(selected_date)
            for booking in existing_booking:
                if self.worksheet.cell(booking.row, 1).value == au_id and self.worksheet.cell(booking.row, 3).value == sport:
                    return True
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def is_time_slot_booked(self, selected_date, selected_time):
        try:
           worksheet = self.gc.open(self.spreadsheet_name).sheet1
           existing_booking = worksheet.findall(selected_date)
           for booking in existing_booking:
             if worksheet.cell(booking.row, 5).value == selected_time:
                return True
           return False

        except Exception as e:
           print(f"Error: {e}") # I have written exception error to find out details about the error
           return False

        
    def save_to_google_sheets(self, data):
        try:
            worksheet = self.gc.open(self.spreadsheet_name).sheet1 
            worksheet.append_row([data['au_id'], data['email'], data['sport'], data['selected_date'], data['selected_time']])
            print("Data saved to Google Sheets.")
        except Exception as e:
            print(f"Error: {e}") # I have written exception error to find out details about the error

if __name__ == "__main__":
    credentials_path = 'credentials.json' 
    spreadsheet_name = 'Data'
    data_manager = DataManagement(credentials_path, spreadsheet_name)
    #EXAMPLe for storing data
    data = {
        'au_id': '123',
        'email': 'example@example.com',
        'sport': 'Badminton',
        'selected_date': '2022-02-14',
        'selected_time': '10:00'
    }
    data_manager.save_to_google_sheets(data)
