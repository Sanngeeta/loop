num=int(input("enter number to cheak for armstorng number:"))
yn=num
sum=0
while num>0:
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if yn==sum:
    print("Number of Armstrong=",sum)    
else:
    print("Not Armstrong no=",sum)    



# num=int(input("enter the number"))
# sum=0
# yn=num
# while yn>0:
#     f=1
#     i=1
#     rem=yn%10
#     while i<=rem:
#         f=f*i
#         i=i+1
#     sum=sum+f
#     yn=yn//10
# print(sum)        
   


# num=int(input("enter the number"))
# yn=num
# sum=0
# i=1
# while yn>0:
#     a=yn%10
#     i=i*yn
#     yn=yn//10
#     sum=sum+yn
# if yn==sum:
#     print("Strong number=",sum)
# else:
#     print("not strong",sum)        
