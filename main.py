height=float(input("insert height in cm: "))
weight=float(input("insert weight in kg: "))

BMI=weight/(height/100)**2

if BMI<=18.4:
    print("You are underweight!!")
elif BMI<=   24.9:
    print("You are healthy!!")
elif BMI<=29.9:
        print("You are overweight!!")
elif BMI<=34.9:
    print("You are severely obese!!")
else: 
    print("You are severly obese!!")