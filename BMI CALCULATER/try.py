from tkinter import *
from PIL import Image, ImageTk

# Function to calculate BMI
def calculate_bmi():
    weight = int(weight_entry.get())
    height_cm = int(height_entry.get())
    height_m = height_cm / 100  # convert cm to meters
    bmi = weight / (height_m * height_m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

# Function to display BMI category
def bmi_index(bmi):
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
    result_label.config(text=result_text)

# Function to convert feet and inches to cm
def convert_to_cm():
    feet = int(feet_entry.get())
    inches = int(inches_entry.get())
    total_inches = (feet * 12) + inches
    cm = total_inches * 2.54
    conversion_result_label.config(text=f'{feet} feet {inches} inches = {round(cm, 2)} cm')

# Main window setup
root = Tk()
root.title('BMI Calculator')
root.geometry('800x600')
root.config(bg='black')

# Heading
heading = Label(root, text="BMI Calculator", fg="green", bg="black", font=("Helvetica", 26, "bold"))
heading.pack(pady=25)

# Placeholder for image (optional)
image_frame = Frame(root, bg="black")
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
    error_label = Label(image_frame, text="Image not found", fg="white", bg="black", font=("Helvetica", 12))
    error_label.pack()

# Description
description_label = Label(root, text="This calculator helps you determine your Body Mass Index (BMI).\n"
                                     "Please enter your height in centimeters and weight in kilograms.\n"
                                     "BMI is a measure of body fat based on height and weight.",
                          fg="green", bg="black", font=("Helvetica", 14))
description_label.pack(pady=15)

# Main frame
main_frame = Frame(root, bg="black")
main_frame.pack(expand=True)

# BMI Calculator frame
bmi_frame = Frame(main_frame, bg="black")
bmi_frame.grid(row=0, column=0, padx=10, pady=10)

# Height Label and Entry
Label(bmi_frame, text="Enter Height (cm):", fg="green", bg="black", font=("Helvetica", 12, "bold")).grid(row=0, column=0, pady=5)
height_entry = Entry(bmi_frame, font=("Helvetica", 12))
height_entry.grid(row=0, column=1, pady=5, ipadx=10, ipady=5)

# Weight Label and Entry
Label(bmi_frame, text="Enter Weight (kg):", fg="green", bg="black", font=("Helvetica", 12, "bold")).grid(row=1, column=0, pady=5)
weight_entry = Entry(bmi_frame, font=("Helvetica", 12))
weight_entry.grid(row=1, column=1, pady=5, ipadx=10, ipady=5)

# Calculate Button
calculate_button = Button(bmi_frame, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 12, "bold"), bg="green", fg="white")
calculate_button.grid(row=2, columnspan=2, pady=10)

# Result Label (initially empty)
result_label = Label(bmi_frame, text="", fg="white", bg="black", font=("Helvetica", 14, "bold"))
result_label.grid(row=3, columnspan=2, pady=5)

# Feet to cm converter frame
converter_frame = Frame(main_frame, bg="black")
converter_frame.grid(row=0, column=1, padx=50, pady=10, sticky=N)

# Converter Heading
converter_heading_label = Label(converter_frame, text="Feet/Inches to CM Converter", fg="green", bg="black", font=("Helvetica", 16, "bold"))
converter_heading_label.grid(row=0, columnspan=2, pady=10)

# Feet Label and Entry
Label(converter_frame, text="Feet:", fg="green", bg="black", font=("Helvetica", 12, "bold")).grid(row=1, column=0, pady=5)
feet_entry = Entry(converter_frame, font=("Helvetica", 12))
feet_entry.grid(row=1, column=1, pady=5, ipadx=10, ipady=5)

# Inches Label and Entry
Label(converter_frame, text="Inches:", fg="green", bg="black", font=("Helvetica", 12, "bold")).grid(row=2, column=0, pady=5)
inches_entry = Entry(converter_frame, font=("Helvetica", 12))
inches_entry.grid(row=2, column=1, pady=5, ipadx=10, ipady=5)

# Convert Button
convert_button = Button(converter_frame, text="Convert to CM", command=convert_to_cm, font=("Helvetica", 12, "bold"), bg="green", fg="white")
convert_button.grid(row=3, columnspan=2, pady=10)

# Conversion Result Label (initially empty)
conversion_result_label = Label(converter_frame, text="", fg="white", bg="black", font=("Helvetica", 14, "bold"))
conversion_result_label.grid(row=4, columnspan=2, pady=5)

root.mainloop()
