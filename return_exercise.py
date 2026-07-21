

def get_user_details():
    weight=input("Enter your weight: ")
    height=input("Enter your height: ")

    weight=float(weight)
    height=float(height)
    bmi=weight/(height*height)


    return bmi,weight,height

def main():
   weight,height,bmi=get_user_details()
   print("Your BMI is: ", bmi)
   print("Your weight is: ", weight)
   print("Your height is: ", height)
main()