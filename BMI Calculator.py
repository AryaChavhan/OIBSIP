import tkinter as tk
from tkinter import messagebox
import csv

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if height <= 0 or weight <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        bmi = weight / (height ** 2)
        category = categorize_bmi(bmi)

        result_label.config(text=f"Your BMI: {bmi:.2f} - {category}")
        save_data(weight, height, bmi, category)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def save_data(weight, height, bmi, category):
    with open('bmi_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([weight, height, bmi, category])


root = tk.Tk()
root.title("BMI Calculator")


tk.Label(root, text="Enter your weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Enter your height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
