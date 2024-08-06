import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("BMI Calculator")
window.config(padx=90, pady=90)

def calculate_bmi():
    height = heightInput.get()
    weight = weightInput.get()
    if weight == "" or height == "":
        resultLabel.config(text="Enter both weight and height")
    else:
        try:
            height = float(height)
            weight = float(weight)
            bmi = weight / ((height / 100) ** 2)
            resultString = writeResult(bmi)
            resultLabel.config(text=resultString)
        except ValueError:
            resultLabel.config(text="Enter a valid number!")
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for weight and height.")

# UI
weightInputLabel = tk.Label(text="Enter your weight (kg)")
weightInputLabel.pack()
weightInput = tk.Entry(width=10)
weightInput.pack()

heightInputLabel = tk.Label(text="Enter your height (cm)")
heightInputLabel.pack()
heightInput = tk.Entry(width=10)
heightInput.pack()

calculateButton = tk.Button(text="Calculate", command=calculate_bmi)
calculateButton.pack()

resultLabel = tk.Label()
resultLabel.pack()

def writeResult(bmi):
    resultString = f"Your BMI is {round(bmi, 2)}, You are "
    if bmi <= 16:
        resultString += "severely thin"
    elif 16 < bmi <= 17:
        resultString += "moderately thin"
    elif 17 < bmi <= 18.5:
        resultString += "mildly thin"
    elif 18.5 < bmi <= 25:
        resultString += "normal weight"
    elif 25 < bmi <= 30:
        resultString += "overweight"
    elif 30 < bmi <= 35:
        resultString += "obese class 1"
    elif 35 < bmi <= 40:
        resultString += "obese class 2"
    else:
        resultString += "obese class 3"
    return resultString

window.mainloop()
