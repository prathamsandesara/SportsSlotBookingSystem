import smtplib
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox

#simple mail transfer protocol
#Multipurpose Internet Mail Extensions (MIME)

class EmailManagement:
#defining a function to send an email for confirmation
    def send_email(self, email, au_id, sport, selected_date, selected_time):
        sender_email = "slotbookingau@gmail.com"
        sender_password = "kyud byyw sxjw abvy"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = "Slot Booking Confirmation "
        body = f"Dear {au_id},\n\nYour slot for {sport}  has been booked successfully on {selected_date} at {selected_time}.\n\n Enjoy Playing!!"
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, message.as_string())
                messagebox.showinfo("Success","Email sent successfully!")
        



    