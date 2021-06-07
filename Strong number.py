# num=int(input("enter the number"))
# i=1
# while num>i:
#     a=num%10
#     b=(num//10)%10
#     c=(num//10)//10
#     y=a+b+c
#     if y%10==0:
#         print("Strong Number:",num)
#     else:
#         print("Not Strong:",num)    
#     i=i+num    



num=int(input("enter the number"))
yn=num
sum=0
while num:
    i=1
    f=1
    y=num%10
    while i<=y:
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
    if sum==yn:
        print("Strong number=",sum)
    else:
        print("Not Strong=",sum)   
        
