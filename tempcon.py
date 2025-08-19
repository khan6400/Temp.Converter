#history related stuff
def log_history(result):
    with open("history.txt", "a+") as history_file:
        history_file.write(result)
def view_history():
    with open("history.txt", "r") as history_file:
        history_data = history_file.read().strip()
    print(f"Your history: \n{history_data}")
def del_history():
    with open("history.txt", "w") as history_file:
        history_file.write("")
        print("History Deleted")

#temp conversion and logging
def temp_converters(select, usr_inp):
    select = int(select)
    if select == 1:
        result = f"{usr_inp} Celius = {((usr_inp*9)/5)+32:.2f} Fahrenheit"
    elif select == 2:
        result = f"{usr_inp} Fahrenheit = {(((usr_inp-32))*5)/9:.2f} Celsius"
    elif select == 3:
        result = f"{usr_inp} Celsius = {usr_inp + 273.15:.2f} Kelvin"
    elif select == 4:
        result = f"{usr_inp} Fahrenheit = {(((usr_inp-32)*5)/9)+273.15:.2f} Kelvin"
    elif select == 5:
        result = f"{usr_inp} Kelvin = {usr_inp - 273.15:.2f} Celsius"
    elif select == 6:
        result = f"{usr_inp} Kelvin = {(((usr_inp-273.15)*9)/5)+32:.2f} Fahrenheit"
    print(result)
    log_history(str(result)+"\n")

#main program
def main_prog():
    while True:
        try:
            select = input("Press:\n 1 for Celsius to Fahrenheit \n 2 for Fahrenheit to Celsius \n 3 for Celsius to Kelvin \n 4 for Fahreheit to kelvin \n 5 for Kelvin to Celsius \n 6 for Kelvin to Fahrenheit \n or 'v' to view history or 'q' to quit or 'd' to delete history: ")
            if select == "q":
                break
            elif select == "d":
                del_history()
                continue
            elif select == "v":
                view_history()
                continue
            elif int(select) not in range(1,7):
                print("Invalid Selection!")
                continue
            usr_inp = float(input("Enter to convert: "))
            temp_converters(select, usr_inp)
        except ValueError:
            print("Please Enter only numbers")
