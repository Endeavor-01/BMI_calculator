############################ COMPLETED THE BEGINNER TASK AND TRIED ADVANCE TASK BUT NOT FULLY COMPLETED#########################################

from tkinter import *
from PIL import Image, ImageTk


# here we calculate the BMI of the user based on height and weight which is in cm and kg
def calculate_bmi():
    weight = int(weight_entry.get())
    height_cm = int(height_entry.get())
    height_m = height_cm / 100  # convert cm to meters
    bmi = weight / (height_m * height_m)
    bmi = round(bmi, 1)
    bmi_category(bmi)

# here we determine if the user is in whuch category
def bmi_category(bmi):
    if bmi < 18.5:
        result_text = f'BMI = {bmi} is Underweight'
    elif 18.5 <= bmi < 24.9:
        result_text = f'BMI = {bmi} is Normal'
    elif 24.9 <= bmi < 29.9:
        result_text = f'BMI = {bmi} is Overweight'
    elif bmi >= 29.9:
        result_text = f'BMI = {bmi} is Obesity'
    else:
        result_text = 'Something went wrong!'
    result.config(text=result_text)

# Main window setup
root = Tk()
root.title('BMI Calculator')
root.geometry('800x800')
root.config(bg='#a8e6cf')

# Heading
heading = Label(root, text="BMI Calculator", fg="#390099", bg="#a8e6cf", font=("Helvetica", 26, "bold"))
heading.pack(pady=25)

# Placeholder for image (optional)
image_frame = Frame(root, bg="#a8e6cf")
image_frame.pack(pady=15)

# Load and display the image
try:
    image = Image.open("images.png")
    image = image.resize((500, 200))  # Increased image size while maintaining aspect ratio
    photo = ImageTk.PhotoImage(image)
    image_label = Label(image_frame, image=photo)
    image_label.image = photo
    image_label.pack()
except IOError:
    error_label = Label(image_frame, text="Image not found", fg="#390099", bg="#a8e6cf", font=("Helvetica", 12))
    error_label.pack()

# Description
description = Label(root, text="This calculator helps you determine your Body Mass Index (BMI).\n"
                                     "Please enter your height in centimeters and weight in kilograms.\n"
                                     "BMI is a measure of body fat based on height and weight.",
                          fg="#390099", bg="#a8e6cf", font=("Helvetica", 14))
description.pack(pady=15)  # Reduced the padding

# Main frame
main_frame = Frame(root, padx=10, pady=10, bg="#a8e6cf")
main_frame.pack(expand=True)

# Input frames
input_frame = Frame(main_frame, bg="#a8e6cf")
input_frame.grid(row=0, column=0, pady=2)  # Reduced the gap

# Height Label and Entry
Label(input_frame, text="Enter Height in (cm):", fg="#390099", bg="#a8e6cf", font=("Helvetica", 12, "bold")).grid(row=0, column=0, pady=5)
height_entry = Entry(input_frame, font=("Helvetica", 12))
height_entry.grid(row=0, column=1, pady=5, ipadx=10, ipady=5)

# Weight Label and Entry
Label(input_frame, text="Enter Weight in (kg):", fg="#390099", bg="#a8e6cf", font=("Helvetica", 12, "bold")).grid(row=1, column=0, pady=5)
weight_entry = Entry(input_frame, font=("Helvetica", 12))
weight_entry.grid(row=1, column=1, pady=25, ipadx=10, ipady=5)

# Button frame
button = Frame(main_frame, bg="#a8e6cf")
button.grid(row=1, column=0, pady=5)  # Reduced the gap

# Calculate Button
calculate_button = Button(button, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 12, "bold"), bg="#390099", fg="#a8e6cf")
calculate_button.pack()

# Result Label (initially empty)
result = Label(main_frame, text="", fg="#390099", bg="#a8e6cf", font=("Helvetica", 14, "bold"))
result.grid(row=2, column=0, pady=5)  # Reduced the gap

root.mainloop()
