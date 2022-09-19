
name=input("enter names:",)
name_set=set()
while name !='':

    name_set.add(name)
    new_name=input("enter new new name:",)
    if new_name not in name_set:
        print("new name")
    else:
        print("exist name")
    name=new_name
print("the names are:" ,name_set)


