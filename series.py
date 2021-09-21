terms = int(input("number of terms :"))
n1=0
n2=1
count=0
#check the number of terms given by user
if terms<=0:
    print("please enter positive number")
elif terms==1:
    print("fibonacci series is upto ",terms,":")
    print(n1)
else:
    print("the fibonacci series :")
    while count<terms:
        print(n1)
        x=n1+n2
        n1=n2
        n2=x
        count+=1
