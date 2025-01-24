#if statement
#number = int(input("enter a number:"))
#if number %5 == 0:
 #   print("the given number is even")
#else:
  #  print("given number is odd")

#age = int(input("enter a number:"))
#if age>=18:
 #   print("eligible")
#else:
 #   print("not eligible")

###num1 = int(input("enter the first number:"))
#num2 = int(input("enter the second number:"))
#num3 = int(input("enter the third number:"))
#if num1>num2 and num1>num3:
 #    print(f"the greatest number is: {num1}")
#elif num2>num1 and num2>num3:
 #    print(f"the greatest number is: {num2}")
#else:
###     print(f"the greatest number is: {num3}")###

'''leap_year = int(input("enter the year:"))
if leap_year %4 ==0:
    print(f" {leap_year} is a leap year")
else:
    print(f"{leap_year} is not a leap year")'''
import random
from mimetypes import guess_type
from operator import truediv
from os import remove

'''score = int(input("enter a number:"))
if score >= 90:
    print("grade A")
elif 80<= score <90:
    print("grade B")
elif 70<= score <80:
    print("grade C")
elif 60<= score <70:
    print("grade D")
else:
    print("grade F")'''

'''number = int(input("enter a number:"))
if number> 0:
    print("positive")
elif number <0:
    print("negative")
else:
    print("zero")'''

'''word = input("enter a word:").lower()
if word in 'aeiou':
    print(f"{word} is a vowel")
else:
    print(f"{word} is a a constant")'''

'''year = int(input("enter a number:"))
if year > 2000:
    print(f"{year} is a 21st century")
else:
    print(f"{year} is not 21st century")'''

'''correct_number = 3
guess_limit = 4
current_attempt = 0
while current_attempt < guess_limit:
    number = int(input(f" Enter your guess: "))
    current_attempt += 1
    if number == correct_number:
        print("you're the win")
        break
else:
    print("sorry you lose the game")'''

'''count = 0
while count <= 9:
    count += 1
    print(count)'''

'''number = 100
count = 0
while number > count:
    no = int(input("enter a number:"))
    count += no
    print(f"sum ={count}")
    if no == 0:
        break'''

    #count += no
    #print(f"sum ={count}")


'''correct_number = random.randint(1,10)
guess_type = 3
guess_count = 0
while "true":
    guess = int(input("enter a number:"))
    if correct_number == guess:
        print("congratulations maamay")
        break'''

# Find even numbers between 1 and 20
'''print("Even numbers from 1 to 20:")
for number in range(1, 21):
    if number % 2 == 0:  # Check if the number is even
        print(number)'''


'''def sub():
    print("subraction:")
    a = int(input("enter a value:"))
    b = int(input("enter b value:"))
    print(a-b)
sub()'''

'''def findpassorfail(a):
    if a >= 35:
        print("pass")
    else:
        print("fail")

a = int(input("enter a:"))
findpassorfail(a)'''

'''def findrange(a,b):
    for i in range(a,b):
        print(i)

a = int(input("enter a:"))
b = int(input("enter b:"))
findrange(a,b)'''


'''s_username = "EMC"
s_password = "123"

username = (input("enter a value:"))
password = (input("enter a value:"))

def validate():
    if username == s_username and s_password == password:
        return "true"
    else:
        return "false"


print(validate())'''

'''def hello(msg):
    print(f"hello,{msg}!")

msg = "python"
hello(msg)'''



'''def find_max(n1,n2):
    if n1>n2:
        return {n1}
    else:
        return {n2}

print(find_max(10,11))'''


'''def is_vowel(word):
    if word in 'aeiou':
        return True
    else:
        return False


print(is_vowel("mso"))'''

'''def guessing_word_game():
    print("welcome to the W guessing game")
    word = "messi"
    attempt = 3
    guess_count = 0
    while True:
        answer = input().lower()
        if word == answer:
            print(f"great you guess the correct answer {answer}")
            break
        elif attempt <=0:
            print(f"Game Over!")
            break
        else:
            attempt -= 1
            print(f"sry you guess the wrong answer:balance attempt: {attempt}")

guessing_word_game()'''


'''a = int(input())
b = int(input())
for i in range(a+1,b):
    print(i)'''

'''for i  in range(1,11):
    if i %2 == 0:
        print(i)'''

'''count = 0
for i in range(1,100):
    if i %3 ==0 and i %5 ==0:
        count = count+1
print(count)'''

'''add = 0
for i in range(1,6):
    add = add + i
print(add)'''

'''a =[]
c = 0
for i in range(5):
    b = int(input())
    a.append(b)
    c = c+b
    d = c/5
print(d)'''

'''rows = 4
for i in range(1,rows + 1):
    for j in range(i):
        print('*',end = '')
    print()'''

'''a = int(input())
for i in range(1,6):
    j = i*i*i
    print(f"number is:{i} and cube of the {i} is:",j '''

'''sum =0
for i in range(1,8):
    sum = sum + i'''

'''a = input()
add = 0
for a in a:
    add = add + 1
    print(add)'''


'''e_count = 0
o_count = 0
for i in range(1,12):
    if i%2 ==0:
        e_count = e_count +1
    elif i%2 == 1:
        o_count = o_count +1
print("even:",e_count)
print("odd:",o_count)'''


'''str = "iam fucking rule this world"
find = "i"
count = 0
for char in str:
    if char == find:
        count = count +1
print(f"{find} is adding {count} time in the string")'''


'''a = [1,2,3,4,5]
a.reverse()
print(a)'''

'''cube = int(input())
for i in range(1,11):
    a = i*i*i
    print(a)'''


b = "iam fucking rule this world"
vowals = "aeiou"
c = ""
for char in b:
    if char not in vowals:
        c+=char
print(c)










    



