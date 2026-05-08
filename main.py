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

# Start the GUI event loop
root.mainloop()