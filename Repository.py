blocks = int(input("Enter the number of blocks: "))
i = 1
sum = blocks
#
# Write your code here.
#	
while i <= blocks:
    sum = sum - i
    if sum==0:
        height = i
        break
    elif sum <0:
        height = i-1
        break
    
    i = i + 1

print("The height of the pyramid:", height)

##################################################################
## Pretty vowel eater
# 3.1.2.11
wordWithoutVovels = ""

# Prompt the user to enter a word
# and assign it to the userWord variable
userWord = input("Enter a vowel eater word:")
userWord = userWord.upper()

for letter in userWord:
    # Complete the body of the loop.
    if letter in ("A","E","I","O","U"):
        continue
    wordWithoutVovels = wordWithoutVovels+letter
# Print the word assigned to wordWithoutVowels.
print(wordWithoutVovels)


###############################################################
## 3.1.5.2 Sorting simple List
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            print(myList)

print(myList)

##############################################################
## 3.1.5.3 Sorting Simple List - the bubble sort algorithm
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)


################################################################
## 3.1.6.9 LAB: Operating with lists - basics
# Remove duplicate elements from a List
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList = []

for i in range(len(myList)):
    if myList[i] not in myList[i+1:]:
        newList.append(myList[i])
myList=newList
    
    
print("The list with unique elements only:")
print(myList)


##################################################################
## 4.1.3.6 A leap year: writing your own functions

def isYearLeap(year):
    if year%400==0:
        return True
    elif year%4==0:
        if year%100==0:
            return False
        else:
            return True
        
    else:
        return False
print(isYearLeap(2020))
#
# put your code here
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


#########################################################################
## 4.1.3.7  write and test a function which takes two arguments (a year
##and a month) and returns the number of days for the given month/year pair

def isYearLeap(year):
    if year%400==0:
        return True
    elif year%4==0:
        if year%100==0:
            return False
        else:
            return True
        
    else:
        return False
print(isYearLeap(2020))

def daysInMonth(year, month):
    monthList=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month > 12:
        return None
    elif isYearLeap(year)==True:
        if month==2:
            return 29
        else:
            return monthList[month-1]
    else:
        return monthList[month-1]
        
        
print(daysInMonth(1988,2))

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 13]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

