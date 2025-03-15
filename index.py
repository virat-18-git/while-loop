# reverse number
num=123456
rev_num=0
temp=num
sum=0
count=0
while num>0:
    rem=num % 10
    sum+=rem   #will give you sum of digits
    count+=1  # to count number of digits in a given number
    rev_num= rev_num* 10 +rem
    num = num // 10
print(rev_num)
print(sum)
print(count)
if temp == rev_num:
    print("PALINDROME")


# implement a basic logic system where the user has three attempts to enter the correct password using a loop:
user_name = 'Pawan Kalyan'
user_password = 'Janasena'
allowed_attempts = 3
while allowed_attempts > 0:
    print("Enter Username and Password")
    print("you have",allowed_attempts,"attempts")

    username_input = input("Enter Username")
    password_input = input("Enter the Password")

    if user_name == username_input and user_password == password_input:
        print("Login Successfull")
        break
    else:
        print("Wrong Credentials")
        allowed_attempts -= 1


# to find square and cube of the number:
choice = input("Enter either square or cube or exit")
while True:
    if choice == 'square':
        user_num_input = float(input("Enter the number for square"))
        print("valid input")
    elif choice =='exit':
        break
    else:
        print("Invalid Input")


# to find given number is prime:
# method 1
num1 = int(input("Enter a number to check if prime  "))
count = 0
for i in range(1,num1 + 1):
    if num1 % i == 0:
        count +=1
if count == 2:
    print("Given number is prime")
else:
    print("NOT PRIME")


# to find  prime number in a given range
num1=int(input("Enter Lower Bound "))
num2=int(input("Enter Upper Bound "))
for p in range (num1,num2+1):
    count = 0
    for i in range(1,p + 1):
        if p % i == 0:
         count += 1
    if count == 2:
        print(p, "is prime")
    else:
        print(p,"not a prime")


# nearest prime number
num1 = int(input("Enter Number "))
while True:
    num1 +=1
    count = 0
    for i in range (1,num1 + 1):
        if num1 % i == 0:
            count += 1
    if count == 2:
        print(num1)
        break








