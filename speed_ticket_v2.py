#variable list
wantedList =['tomson','kelly','andrew','kei'] #wanted list

#function wiht parameter
def calculateFine(speed_v, speed_l): #calculate the fine depending on how much the driver surpass the speed limit
    
    over = speed_v - speed_l
    fine = over * 10
    
    if over >= 1 and over <= 10:
        print(name.upper(), "you will receive $",fine, "fine")
    if over > 10 and over < 40:
        print(name.upper(), "you will receive $",fine, "fine", "and your driver licence will be taken by the police")
    if over >= 40:
        print(name.upper(), "you will receive $",fine, "fine", "and you are going to jail")
    if speed_v <= speed_l:
        print("Good", name,"you are not speeding")

#main routine
name = input("What is your name?")
if name in wantedList:
    print(name.upper(),",You are now under arrest!")
else: #ask information needed for the fine calculation
    repeat = True
    while repeat == True:
        try:
            speed_v = float(input("What's the speed of your vehical?"))
            speed_l = float(input("What's the speed limit there?"))
            repeat = False #stop the loop
        except ValueError:
            print("PLease enter in digits") #demends the user to enter in digit
    calculateFine(speed_v, speed_l)
    





