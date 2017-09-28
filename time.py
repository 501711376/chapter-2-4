timenow=float(input("what time is it now 0-24"))
hourswait=float(input("How many hours are you waiting?"))
alarmtime=(hourswait+timenow)%24
print("your alarm will go off at:"+str(alarmtime))                  
        