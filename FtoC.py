import sys


def tocelcius(temp_fahr):
    temp_celc = []
    for index in range(len(temp_fahr)):
        temp_celc.append((temp_fahr[index] - 32) * 5 / 9)
    return temp_celc

def tofahrenheit(temp_celc):
    temp_fahr = []
    for index in range(len(temp_celc)):
        temp_fahr.append((temp_celc[index]* 5 / 9) + 32)
    return list(temp_fahr)

attempts = 0
while attempts < 3:
    try:
        unit = input("Please specify the unit of temperature measure (C)elcius or in (F)ahrenheit").lower()

        if unit == "celcius" or unit == "c":
            input_arr = input("Provide a temperature value in Celcius").split(' ');
            temps = [float(i) for i in input_arr]
            temps_fahrs = tofahrenheit(temps)
            for i in range(len(temps_fahrs)):
                print(f"{temps[i]} in Celcius is {temps_fahrs[i]} in Fahrenheit")
            # elif isinstance(temp, float):
        elif unit == "fahrenheit" or unit == "f":
            input_arr = input(f"Provide a temperature value in Fahrenheit").split(' ')
            temps = [float(i) for i in input_arr]
            temps_celcs = tocelcius(temps)
            # if isinstance(temp, float):
            for i in range(len(temps_celcs)):
                print(f"{temps[i]} in Fahrenheit is {temps_celcs[i]} in Celcius ")
        else:
            print("Incorrect data entered. \
                  Please specify the unit of temperature measure (Celcius or in Fahrenheit)")
        attempts = attempts + 1
    except ValueError:
        print("You've entered wrong value. Try again!")
    finally:
        print("bye")
