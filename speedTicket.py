wantedList =['tomson','kelly','andrew','kei']

def calculateFine(speed_v, speed_l):
    
    over = speed_v - speed_l
    fine = over * 10
    
    if over >= 1 and over <= 50:
        print("$",fine, "fine")
    if over > 50 and over < 80:
        print("$",fine, "fine", "Collect licence")
    if over >= 80:
        print("$",fine, "fine", "Go to jail")

    if speed_v <= speed_l:
        print("Not speeding")

def printSummary():
    
    name = input("What is your name?")
    if name in wantedList:
        print(name.upper(),",You are now under arrested!")
    else:
        repeat = True
        while repeat == True:
            try:
                speed_v = float(input("What's the speed of your vehical?"))
                speed_l = float(input("What's the speed limit there?"))
                repeat = False
            except ValueError:
                print("PLease enter in digits")
        calculateFine(speed_v, speed_l)

printSummary()



