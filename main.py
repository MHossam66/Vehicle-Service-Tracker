import tkinter as tk
from tkinter import messagebox

# the main application window
# --- Mohamed Hossam | 24040411 ---
root = tk.Tk()
root.title("Vehicle Service Tracker")
root.geometry("450x550")
root.configure(bg="#f4f4f4")

# Main title label for the application
title_label = tk.Label(root, text="🚗 Vehicle Service Tracker", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=20)

# Frame to hold all user input fields
frame_inputs = tk.Frame(root, bg="#f4f4f4")
frame_inputs.pack(pady=10)

# --- youssef mohamed awadain | 24040456 ---
# Car Name
tk.Label(frame_inputs, text="Car Name (e.g., Kia Soul):", bg="#f4f4f4").grid(row=0, column=0, pady=5, padx=5, sticky="e")
car_name_entry = tk.Entry(frame_inputs, width=25)
car_name_entry.grid(row=0, column=1, pady=5, padx=5)

# Current Mileage
tk.Label(frame_inputs, text="Current Mileage (km):", bg="#f4f4f4").grid(row=1, column=0, pady=5, padx=5, sticky="e")
mileage_entry = tk.Entry(frame_inputs, width=25)
mileage_entry.grid(row=1, column=1, pady=5, padx=5)

# Last Service Date
tk.Label(frame_inputs, text="Last Service Date (YYYY-MM-DD):", bg="#f4f4f4").grid(row=2, column=0, pady=5, padx=5, sticky="e")
last_service_entry = tk.Entry(frame_inputs, width=25)
last_service_entry.grid(row=2, column=1, pady=5, padx=5)

# Start the GUI event loop
root.mainloop()