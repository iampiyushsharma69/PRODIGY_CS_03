
import tkinter as tk
import re

def check_password_strength(event=None):
    password = entry.get()
    strength = "Weak"
    color = "red"

    length_error = len(password) < 8
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, upper_error, lower_error, digit_error, special_error]
    score = errors.count(False)

    if score == 5:
        strength = "Strong"
        color = "green"
    elif score >= 3:
        strength = "Moderate"
        color = "orange"
    
    label_result.config(text=f"Strength: {strength}", fg="green")

# Create the GUI window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x200")
root.configure(bg="#8B0000")  # dark red background

label = tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="#8B0000", fg="green")
label.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack()
entry.bind("<KeyRelease>", check_password_strength)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#8B0000", fg="green")
label_result.pack(pady=20)

root.mainloop()
