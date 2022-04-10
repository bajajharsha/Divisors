#Create a program that asks the user for a number and then prints out a list of all the divisors of that number

num = int(input("Enter a number: "))
listRange = list(range(1,num+1))
divisorList = []

for x in listRange:
    if num % x == 0:
        divisorList.append(x)

print(divisorList)