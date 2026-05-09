# 🚗 Vehicle Service Tracker

# Project Overview
A simple, efficient, and user-friendly desktop application built with Python and Tkinter. This application helps car owners track their vehicle's maintenance schedule by calculating the next required service mileage based on current readings, and securely saving the records locally.

#  Team Members & Contributions
This project was developed collaboratively using Git and GitHub.

1. **Mohamed Hossam Ramzy | ID: 24040411 (Team Leader)**
   - Initialized the repository, set up the main Tkinter GUI window, and managed project architecture.
2. **Yousef Mohamed Awadain | ID: 24040456**
   - Designed and implemented the user input fields (Labels and Entries) within the UI.
3. **Mohamed Ehab Ahmed | ID: 24040406**
   - Implemented the file handling functionality to securely save user inputs into a text file (`car_data.txt`).
4. **Khaled Mohamed Abdelbast | ID: 24040346**
   - Developed the core logic and calculation functions, including error handling.
5. **Mohamed Badawi | ID: 24040408**
6. **Muhannad Rabie | ID: 24040440**

# Technologies & Libraries Used
* **Python 3**
* **Tkinter** (Standard Python GUI Library)
* **Git & GitHub** (For Version Control and Collaboration)

# How to Install and Run
1. Clone this repository to your local machine:
   `git clone https://github.com/MHossam66/Vehicle-Service-Tracker.git`
2. Ensure you have Python installed on your system.
3. Navigate to the project directory in your terminal.
4. Run the application using the following command:
   `python main.py`

# Screenshots


# Known Limitations & Future Improvements
* **Current Limitation:** The application currently tracks a fixed +10,000 km service interval for general maintenance.
* **Future Improvements:** - Add specific tracking for multiple car parts (e.g., Battery life, Tire pressure, Oil change).
  - Implement a database (like SQLite) instead of a simple text file for advanced data querying.
  - Add a feature to view previously saved records directly inside the GUI.