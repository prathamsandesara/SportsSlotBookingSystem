# Sports Slot Booking System 🏀🎾⚽🏐

A user-friendly platform for Ahmedabad University students to book sports slots with ease. This system ensures fairness, transparency, and convenience while providing features like booking constraints, secure data storage, and automated email notifications.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Features
- **Streamlined Booking Process**: Students can book sports slots using their college email ID and AU ID.
- **Booking Constraints**:
  - Slots limited to two days in advance (today and tomorrow).
  - One slot per AU ID per day for the same sport.
- **Multiple Sports Options**: Supports sports like Badminton, Table Tennis, Football, and Volleyball.
- **Secure Data Storage**: Uses Google Sheets API for saving booking data securely.
- **Automated Email Notifications**: Sends confirmation emails for successful bookings.
- **User-Friendly Interface**: Designed with Tkinter for an intuitive GUI.

---

## Technology Stack
- **Programming Language**: Python
- **Libraries and Tools**:
  - `Tkinter`: GUI development
  - `gspread`: Google Sheets integration
  - `google-auth`: Google Cloud authentication
  - `SMTP` and `MIME`: Email management
  - `datetime`: Date and time management

---

## Installation

### Prerequisites
- Python 3.x installed
- Google Cloud Platform (GCP) account with API credentials
- Required Python libraries: `tkinter`, `gspread`, `google-auth`, `smtplib`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SportsSlotBookingSystem.git
   cd SportsSlotBookingSystem
2. Install dependencies:
   ```bash
   pip install gspread google-auth smtplib
3. Set up Google Cloud API credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the **Google Sheets API** and **Google Drive API** for your project.
   - Create a service account and download the `credentials.json` file.
   - Place the `credentials.json` file in the root directory of your project.

4. Configure the Google Sheets:
   - Open the Google Sheets file where you will store the booking data.
   - Share the Google Sheets file with the service account email (from `credentials.json`), granting **Editor** permissions.

## Usage

### Run the Application

Execute the main Python script to start the application:

```bash
python main.py


## Future Enhancements

- **Expanded Sport Options**: Support additional sports such as Basketball, Cricket, etc.
- **Enhanced User Interface**: Further improve the GUI with additional features like a calendar view for slot selection.
- **Mobile App Integration**: Allow students to book sports slots through a mobile app interface.
- **Automated Reminders**: Send reminders to users about their upcoming bookings.


