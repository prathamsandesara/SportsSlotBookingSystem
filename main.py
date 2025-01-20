import tkinter as tk
from gui import SportsBookingGUI
from data_management  import DataManagement
from email_management import EmailManagement

if __name__ == "__main__":
    root = tk.Tk()
    credentials_path = 'credentials.json' 
    spreadsheet_name = 'Data'
    data_manager = DataManagement(credentials_path, spreadsheet_name)
    email_manager = EmailManagement()
    app = SportsBookingGUI(root, data_manager, email_manager)
    root.mainloop()

