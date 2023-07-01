import tkinter as tk
from tkinter import messagebox
import subprocess

def run_code():
    try:
        # Execute your Python file
        subprocess.run(["python", "main.py"], check=True)
        messagebox.showinfo("Result", "Code executed successfully!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to execute the code!")

# Create the main window
window = tk.Tk()
window.title("Code Runner")
window.geometry("1000x800")

# Set the background image
bg_image = tk.PhotoImage(file="background.png")
bg_image = tk.PhotoImage(file="C:/Users/codex/Desktop/AITeena/background.png")

background_label = tk.Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label
label = tk.Label(window, text="TEENA AI ASSISTANCE POWERED BY CHATGPT", font=("Arial", 14))
label.pack(pady=20)

# Create a button to run the code
button = tk.Button(window, text="START", font=("Arial", 12), width=10, height=2, command=run_code)
button.pack()

# Run the event loop
window.mainloop()
