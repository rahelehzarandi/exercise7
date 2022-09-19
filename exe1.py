
monthNum=int(input("enter number of month: ",))
seasons=("Spring","summer","autumn","winter")
if (monthNum == 12) or (monthNum== 1) or (monthNum==2):
    print(seasons[3])
elif (monthNum==3) or (monthNum==4) or (monthNum==5):
    print(seasons[0])
elif (monthNum==6) or (monthNum==7) or (monthNum==8):
    print(seasons[1])
elif (monthNum==9) or (monthNum==10) or (monthNum==11):
    print(seasons[2])
else:
    print("not correct")