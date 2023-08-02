import tkinter as tk
from datetime import date

def calculate_age():
    birth_date = entry_date.get()
    try:
        year, month, day = map(int, birth_date.split('-'))
        birth_date = date(year, month, day)
        current_date = date.today()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age}")
    except ValueError:
        result_label.config(text="Invalid date format. Please use YYYY-MM-DD.")

root = tk.Tk()
root.title("Age Calculator")
label_date = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
entry_date = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
result_label = tk.Label(root, text="Your age will be shown here.")
label_date.grid(row=0, column=0, padx=5, pady=5)
entry_date.grid(row=0, column=1, padx=5, pady=5)
calculate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()
