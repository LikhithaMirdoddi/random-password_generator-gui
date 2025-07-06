import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    user_input = entry_length.get()
    if not user_input.strip():
        messagebox.showerror("Error", "Please enter the password length.")
        return

    try:
        length = int(user_input)
        if length <= 0:
            raise ValueError

        char_values = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(char_values) for _ in range(length))
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
root.resizable(False, False)

label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root, width=10, justify="center")
entry_length.pack()

btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack(pady=10)

entry_result = tk.Entry(root, width=40, justify="center")
entry_result.pack(pady=10)

root.mainloop()
