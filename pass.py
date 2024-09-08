import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def create_password():
    try:
        # Get the password length from the input field
        length = int(entry_length.get())

        # Validate if length is positive
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
        
        # Characters to use for generating password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Create password by randomly selecting characters
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Show the generated password in the output label
        label_password.config(text=f"Generated Password: {password}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to clear input and output
def clear_input():
    entry_length.delete(0, tk.END)
    label_password.config(text="Generated Password: ")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")
window.config(padx=20, pady=20)

# Label for password length input
label_length = tk.Label(window, text="Enter Password Length:", font=("Arial", 12))
label_length.pack(pady=10)

# Input field for password length
entry_length = tk.Entry(window, font=("Arial", 12), width=10)
entry_length.pack()

# Button to generate password
button_generate = tk.Button(window, text="Generate Password", command=create_password, font=("Arial", 12))
button_generate.pack(pady=10)

# Label to display generated password
label_password = tk.Label(window, text="Generated Password: ", font=("Arial", 12))
label_password.pack(pady=10)

# Button to clear the input and output
button_clear = tk.Button(window, text="Clear", command=clear_input, font=("Arial", 12))
button_clear.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
