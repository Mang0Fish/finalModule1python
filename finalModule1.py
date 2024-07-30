from statistics import mean
#First module finals 
#Conditionals

#1
num1: float = float(input("Enter a number"))
num2 : float = float(input("Enter a number"))
if num1 > num2:
    for i in range(3):
        print(num2)
elif num2 > num1:
    for i in range(3):
        print(num1)
        
#2
num1: int = int(input("Enter a number"))
num2: int = int(input("Enter a number"))
print((num1+num2)/2)

#3
nums1: list[int] = [input("Enter a number") for i in range(3)]
print(max(nums1))

#4
num1: int = int(input("Enter a movie's length"))
print(f"{num1 // 60} hour(s) and {num1%60} minute(s)")

#5
num1: int = int(input("Enter a number"))
print(num1%10)

#6
num1: int = int(input("Enter a number"))
print((num1//10)%10)

#7
num1: int = int(input("Enter a number"))
print(num1%10 + num1 // 10)

#8
num1: int = int(input("Enter a number"))
print((num1%10)*10 + num1//10)

#9
num1: int = int(input("Enter a number"))
if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#10
num1: float = float(input("Enter your salary"))
if 0 < num1 <= 6000:
    print("You don't need to pay income tax")
elif 6000 < num1 <= 12000:
    print(f"You need to pay {num1*10/100}")
elif 12000 < num1 <= 18000:
    print(f"You need to pay {num1*20/100}")
elif 18000 < num1 <= 25000:
    print(f"You need to pay {num1*30/100}")    
elif 25000 < num1 <= 35000:
    print(f"You need to pay {num1*40/100}")
elif 35000 < num1 <= 50000:
    print(f"You need to pay {num1*45/100}")
elif 50000 < num1:
    print(f"You need to pay {num1*51/100}")
    
#11
num1: int = int(input("Enter your age"))
num2: int = int(input("Enter your height"))
if (8 <= num1 <= 18 and num2 > 115) or (18 < num1 and num2  > 100):
    print("You're allowed on the ride")
else:
    print("You're not allowed on the ride")
    
#Loops

#1
top: int = int(input("Enter a number"))
for i in range(top):
    print(i+1)

#2
num1: int = int(input("Enter a number"))
num2: int = int(input("Enter a number"))
if num1>num2:
    for i in range(num2, num1 + 1):
        print(i)
elif num2>num1:
    for i in range(num1, num2 + 1):
        print(i)
 
#3
n: int = int(input("Enter a number"))
for i in range(0, n + 1, 2):
    print(i)
    
#4
den: int = int(input("Enter a number"))
maxNum: int = int(input("Enter a number"))
for i in range(0, maxNum+1, den):
    print(i)
    
#Data processing

#1
num1: int = 0
num2: int = 0
num1 = int(input("Enter a number"))
if num1 == -99:
    print("None")
else:    
    num2 += num1
    while True:
        num1 = int(input("Enter a number"))
        if num1 == -99:
            break
        else:
            num2 += num1 
    print(num2)    

#2
num1: int = 0
numHigh: int = 0
numLow: int = 0
num1 = int(input("Enter a number"))
if num1 == -99:
    print("None")
elif num1 <= 0:
    pass
else:
    num1 = int(input("Enter a number"))
    numHigh = num1
    numLow = num1
    while True:        
        num1 = int(input("Enter a number"))
        if num1 <= 0:
            break
        else:
            if num1 > numHigh:
                numHigh = num1
            if num1 < numLow:
                numLow = num1
    print(f"Smallest number {numLow}, Biggest number {numHigh}")
    
#3
lst1: list[int] = []
for i in range(5):
    lst1.append(int(input("Enter a number")))
print(lst1.index(max(lst1))+1)

#4
num1: int = int(input("Enter a number"))
num2: int = int(input("Enter a number"))
sum: int = 0
for i in range(num1):
    sum += num2     
print(sum)

#5
num1: int = int(input("Enter a number"))
num2: int = int(input("Enter a number"))
sum: int = 1
for i in range(num2):
    sum *= num1     
print(sum)

#6
num1: int = int(input("Enter a number"))
str1 = input("Enter a digit")
print(str1 in str(num1))

#7
num1: int = int(input("Enter a number"))
num2: int = int(input("Enter a number"))
divid: int = 0
for i in range(num1, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        divid = i
        break
    else:
        continue
print(divid)

#8 
num1: int = int(input("Enter a number"))
prim: bool = True   
for i in range(2, (abs(num1))):
    if num1 % i == 0:
        print("The number is not primary")
        prim = False
        break
    else:
        continue
if prim:
    print("The number is primary")

#Complex loops

#1 havnt continued from average part yet
lst1: list[float] = []
num1: float
afterFirst: bool = False
notDoubleZero: bool = True 
legal: bool = True
former: float = 0
for i in range(12):
    notDoubleZero: bool = True
    try: 
        num1 = float(input("Enter a temperature"))
    except:
        print("Not a number")
    if num1 < -5 or num1 > 40:
        print("Wrong data")
        legal = False
        break     
    if afterFirst:
        if num1 == former and num1 == 0:
            notDoubleZero = False
    if notDoubleZero:
        lst1.append(num1)
    afterFirst = True
    former = num1
if legal:
    print("Correct data")    
print(f"The temperatures' average is {mean(lst1)}")
print(f"Highest temperature is {max(lst1)}, Lowest temperature is {min(lst1)}")

#2
lst1: list[int] = []
num1: int
innerVeto: bool = False
for i in range(44):
    if innerVeto:
        break 
    try: num1 = int(input("Enter the vote"))
    except: print("Enter a number")
    if num1 == 4:
        print(i+1)
        break
    elif num1 < 0 or num1 > 4:
        while num1 < 0 or num1 > 4:
            num1 = int(input("Enter a number"))
            if num1 == 4:
                print(i)
                innerVeto = True
                break
            elif 0 < num1 < 4:
                lst1.append(num1)
                break
            else:
                continue
    else:
        lst1.append(num1)
print(f"Voted in favor - {lst1.count(1)}, Against - {lst1.count(2)}, Restrained - {lst1.count(3)}")
try: print(f"First country in favor {lst1.index(1)+1}")
except: print("No country has voted in favor")
lst1.reverse()
try:print(f"Last country against {44-lst1.index(2)}")
except: print("No country has voted against")
print(lst1)