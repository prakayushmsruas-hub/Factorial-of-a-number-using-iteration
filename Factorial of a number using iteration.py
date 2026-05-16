print("Factorial of a number using iteration\n")
num=int(input("Enter a number you want factorial of:"))
factorial=1
if num==0 or num==1:
    print("Factorial of",num,"is 1")
else:
    for i in range(1,num+1):
        factorial*=i    
print("Factorial of",num,"is",factorial)