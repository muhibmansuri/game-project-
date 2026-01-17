

while True:
    i =int( input("Enter only positive number:"))
    if i==0:
        break
    print("You entered:", i)
    if i<0:
        print("Please enter only positive number")
        continue
    def square(i):      
        return i * i
    square(i)
    squared_list = [square(i) for i in range(i)]
    print("Squared List using Function:", squared_list)

#example input function use,while loop ,range ,squre function,nagative number square list using function

while True:
    i =int( input("Enter only positive number:"))
    if i==0:
        break
    print("You entered:", i)
    if i<0:
        print("Please enter only positive number")
        continue
    def square(i):      
        return i * i
    square(i)
    squared_list = [square(i) for i in range(i)]
    print("Squared List using Function:", squared_list)

#example input function use,while loop ,range ,squre function,nagative number square ko positive answer ana chahiye, list using function
while True:
    i =int( input("Enter only positive number:"))
    if i==0:
        break
    print("You entered:", i)
    
    def square(i):      
        return abs(i) * abs(i)
    square(i)
    if i<0:
        print("Please enter only positive number")
        continue
    squared_list = [square(i) for i in range(i)]
    print("Squared List using Function:", squared_list)
#example input function use,while loop ,range ,squre function,nagative number square ko positive answer ana chahiye, list using function

while True:
    i =int( input("Enter only positive number:"))
    if i==0:
        break
    print("You entered:", i)
    
    def square(i):      
        return abs(i) * abs(i)
    square(i)
    if i<0:
        print("Please enter only positive number")
        continue
    squared_list = [square(i) for i in range(i)]
    print("Squared List using Function:", squared_list)


def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    prev2, prev1 = 1, 2

    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1
print(climbStairs(5))
    

