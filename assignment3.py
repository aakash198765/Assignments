#-------------------function--------------------------
#function to check whether a number is prime or not

#checking with user input
def is_prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==1:
        print(num, "is not prime number")
    else:
        print(num,"is prime number")
        
        


num=int(input("please enter a number :"))
is_prime(num)