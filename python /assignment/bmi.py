weight_pounds = float(input("Enter weight in pounds: "))
height_inches = float(input("Enter height in inches: "))

weight_kg = weight_pounds * 0.45359237
height_meters = height_inches * 0.0254

bmi = weight_kg / (height_meters ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
else:
    if bmi < 25.0:
        print("Normal")
    else:
        if bmi < 30.0:
            print("Overweight")
        else:
            print("Obese")