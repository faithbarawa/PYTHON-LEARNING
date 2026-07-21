Temperature = float(input("Enter the temperature in Celsius: "))

if Temperature <0:
    print("Fridge is too cold")
elif Temperature <4:
    print("Fridge ok")
elif Temperature <6:
    print("Fridge too warm")
else:
    print("Fridge broken")

 # or
temperature = float(input("Enter the temperature in Celsius: "))

STATUS_BROKEN="Fridge broken"
STATUS_OK = "Fridge ok"
STATUS_COLD="Fridge is too cold"
STATUS_WARM="Fridge too warm"

status= STATUS_BROKEN


if temperature < 0:
    status = STATUS_COLD
elif temperature < 4:
    status = STATUS_OK
elif temperature < 6:
    status = STATUS_WARM
print(status)