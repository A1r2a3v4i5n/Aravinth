#guessing game number
'''correct_number = 5
guess_count = 3
guess_limit = 0
print("welcome to the guessing game")
print("you have the 3 chance to find the correct number")
while guess_count > guess_limit:
    guess =int(input(f"enter the {guess_limit+1} try:"))
    guess_limit +=1
    if guess == correct_number:
        print("you win. the correct number is 5")
        break
    elif guess_limit <= 2:
        print("wrong one! try again")
    else:
        print("sorry! you try the all attempts")
        print("you lose the game,correct number is 5")'''


#Generate Fibonacci Sequence
'''a,b = 0,1
c = 10
count = 0
while count<c:
    print(a,end=" ")
    d = a+b
    a = b
    b= d
    count +=1'''

#Stop When the User Enters "exit"
'''word = "exit"
count = 0
while True:
    num1 = (input())
    count +=1
    if num1 == word:
        print("Good bye!")
        break'''

#Count Digits in a Number
'''a = 123456
count = 0
while a!=0:
    count +=1
    a =a//10
print(count)'''

#Print Even Numbers
'''a = 0
count = 0
while count == 0:
    count +=1
    for i in range(1,21):
        if i%2 == 0:
            print(i,end =" ")'''

#Find Factorial of a Number
'''fac = 4
a = 1
for i in range(1,fac+1):
    a = a*i
print(a)'''


#Reverse a String
'''word = "poda bunda"
a = ""
count = 0
while count == 0:
    count +=1
    for i in word[::-1]:
        print(i,end="")'''

#Multiplication Table
'''table = 5
count = 0
while count == 0:
    count+=1
    for i in range(1,11):
        a = table * i
        print(f"{table} x{i}={a}")'''

#Sum of Numbers
'''a = 50
count = 0
sum = 0
b = ""
while count == 0:
    count +=1
    for i in range(1,51):
        sum = sum +i
        b = sum
print(f"The sum of numbers from 1 to 50 is:{b}")'''


#Print Numbers from 1 to 10
'''count =0
while count ==0:
    count +=1
    for i in range(1,11):
        print(i)'''





