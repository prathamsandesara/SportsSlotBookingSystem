import csv
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from datetime import datetime, timedelta

from data_management import DataManagement
from email_management import EmailManagement

class SportsBookingGUI:
    
    def __init__(self, root, data_manager, email_manager):
        self.data_manager = data_manager
        self.email_manager = email_manager
        self.root = root
        self.root.title("Sports Booking App")

        #for background colour
        root.configure(bg="#282828")

        logo_path = "AUlogo.png"  
        try:
             logo_img = PhotoImage(file=logo_path)
             logo_label = tk.Label(root, image=logo_img, bg="#282828")  
             # #282828 is the dark theme or dark colour 

             logo_label.image = logo_img 
             logo_label.pack(pady=10)
        except tk.TclError:
             print("Logo not found or unsupported format.") # if logo is set to jpeg or jpg it will show error only png format is allowed

        self.email_label = tk.Label(root, text="Enter College Email:", bg="#282828", fg="white")
        self.email_entry = tk.Entry(root, bg="white", fg="black")

        self.id_label = tk.Label(root, text="Enter AU ID:", bg="#282828", fg="white")
        self.id_entry = tk.Entry(root, bg="white", fg="black")

        self.date_label = tk.Label(root, text="Select Date:", bg="#282828", fg="white")
        self.date_picker = ttk.Combobox(root, values=self.get_dates(), state="readonly", style="TCombobox", background="white")

        self.time_label = tk.Label(root, text="Select Time:", bg="#282828", fg="white")
        self.time_picker = ttk.Combobox(root, values=self.get_time_slots(), state="readonly", style="TCombobox", background="white")

        self.sports_label = tk.Label(root, text="Select Sport:", bg="#282828", fg="white")
        self.sports_var = tk.StringVar(root)
        self.sports_var.set("Badminton")
        self.sports_menu = tk.OptionMenu(root, self.sports_var, "Badminton", "Table Tennis", "Football", "Volleyball")

        # ttk style is only used for green colour button 
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Green.TButton", background="#4CAF50", foreground="white")
        self.book_button = ttk.Button(root, text="Book Slot", command=self.book_slot, style="Green.TButton")
        

        #Spacing between the labels 
        
        self.email_label.pack(pady=7)
        self.email_entry.pack(pady=7)
        self.id_label.pack(pady=7)
        self.id_entry.pack(pady=7)
        self.date_label.pack(pady=7)
        self.date_picker.pack(pady=7)
        self.time_label.pack(pady=7)
        self.time_picker.pack(pady=7)
        self.sports_label.pack(pady=7)
        self.sports_menu.pack(pady=7)
        self.book_button.pack(pady=12)

 
 # defining functins -:
        
    def get_dates(self):
        today = datetime.now()
        dates = [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(2)]  
        return dates

    def get_time_slots(self):
        time_slots = []
        start_time = datetime.strptime("9:00", "%H:%M")
        end_time = datetime.strptime("19:00", "%H:%M")
        interval = timedelta(hours=1)

        while start_time < end_time:
            end_time_slot = start_time + interval
            time_slot_str = f"{start_time.strftime('%H:%M')}-{end_time_slot.strftime('%H:%M')}"
            time_slots.append(time_slot_str)
            start_time = end_time_slot
        return time_slots
    
    def user_has_booked(self, au_id, selected_date,selected_sport):
        return self.data_manager.user_has_booked(au_id, selected_date,selected_sport)
    
    def is_valid_email(self,email):
         return "@ahduni.edu.in" in email   
    def is_valid_roll_number(self, au_id):
         return au_id.startswith("AU") and len(au_id) > 2

    def book_slot(self):
      email = self.email_entry.get()
      au_id = self.id_entry.get()
      sport = self.sports_var.get()
      selected_date = self.date_picker.get()
      selected_time = self.time_picker.get()

    # ERROR checking Statements-:
      
      if not self.is_valid_email(email):
        messagebox.showerror("Error", "Please enter a valid College Mail id.")
        return
      if not self.is_valid_roll_number(au_id):
        messagebox.showerror("Error", "Please enter a valid College Roll No.")
        return

      if not email or not au_id or not selected_date or not selected_time:
        messagebox.showerror("Error", "Please fill in all details.")
        return

      if self.data_manager.is_time_slot_booked(selected_date, selected_time):
        messagebox.showerror("Error", "The selected time slot is already booked. Please choose another time.")
        return

      if self.user_has_booked(au_id, selected_date, sport):
        messagebox.showerror("Error", "You have already booked a slot for this date and sport.")
        return

      booking_date = datetime.strptime(selected_date, "%Y-%m-%d")
      today = datetime.now()
      max_advance_date = today + timedelta(days=2)  # Changed to allow booking up to 2 days in advance

    #booking for 2 days advance only
      if booking_date > max_advance_date:
        messagebox.showerror("Error", "Booking allowed only up to 2 days in advance.")
        return

    #saving data to google sheets 
      self.data_manager.save_to_google_sheets({
        'au_id': au_id,
        'email': email,
        'sport': sport,
        'selected_date': selected_date,
        'selected_time': selected_time
      })

      messagebox.showinfo("Success", f"Slot booked for {sport} on {selected_date} at {selected_time}. "
                                   f"Booking details saved to Google Sheets.")

      self.email_manager.send_email(email, au_id, sport, selected_date, selected_time)
    
    
    
if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=800, height=600) 
    credentials_path = "credentials.json"
    spreadsheet_name = "Data"
    data_manager = DataManagement(credentials_path, spreadsheet_name)
    email_manager = EmailManagement()  
    app = SportsBookingGUI(root, data_manager, email_manager)
    root.mainloop()


