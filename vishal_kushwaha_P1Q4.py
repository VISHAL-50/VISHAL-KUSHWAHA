ram=int(input("Enter age of ram:-"))
shyam=int(input("Enter age of shyam:-"))
ajay=int(input("Enter age of ajay:-"))

if (ram < shyam and ram <= ajay):
    if(ram==shyam):
        print("ram and shyam are of same age and are youngest")
    elif(ram==ajay):
        print("ram amd ajay are of same age and are youngest")
    else:
        print("ram is youngest")
elif(shyam <= ram and shyam <= ajay):
    if(ram==shyam):
        print("ram and shyam are of same age and are youngest")
    elif(shyam==ajay):
        print("ram and ajay are of same age and are youngest")
    else:
        print("shyam is the youngest")
else:
    print("ajay is the youngest")
              


   
    

