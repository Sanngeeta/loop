i=1
while i<=2:
    num=input("What is a capital of india:(1)Delhi  (2)Kolkata (3)Goa (4)Mombai:")
    if num=="delhi":
        print("Congratulation:-you are vin")
        break
    else:
        print("Wrong")
        num=input("Do you want lifeline:")
        if num=="yes":
            num2=input("What is a capital of india:")
            if num2=="delhi":
                print("Congratulation you Win")
                break
            else:
                print("Time over") 
                break 
        else:
            print("chance over")  
            break 
    i=i+1               

        