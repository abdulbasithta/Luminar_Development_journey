# last_week_attendence store organize "P","O","A","H"

attendence =["H","A","P","P","P","O","H"]

attendence[4] ="O" # update "P" >>> "O"

# for at in attendence:

#     if at =="H":

#         print("Holiday")

#     elif at =="P":

#         print("Offline")

#     elif at =="O":

#         print("Online")

#     elif at =="A":

#         print("Absent")

holiday_count =0
offline_count =0
online_count =0
absent_count =0

for at in attendence:

    if at =="H":

        holiday_count +=1

    elif at =="P":

        offline_count +=1

    elif at =="O":

        online_count +=1

    elif at =="A":

        absent_count +=1

print("Holiday count", holiday_count)

print("Offline count", offline_count)

print("Absent count", absent_count)                                 

print("Online count", online_count)

