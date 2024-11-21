


# Part 2

start,end = int(input()), int(input()) 
chet,nechet,crat = 0,0,0
while start <= end: 
    if start % 2 == 0: 
        chet += start 
    else: 
        nechet += start 
    if start % 9 == 0: 
        crat +=1 
    start += 1
print(chet, nechet, crat ,(chet + nechet)) 


nline = int(input()) 
nsym = input() 
while nline != 0: 
    print(nsym) 
    nline -= 1

while True:
    local_number = int(input())
    if local_number < 0:
        print("Number is negative")
    elif local_number == 0:
        print('Number is equals to zero')
    elif local_number == 7:
        break
    else:
        print('Number is positive')


lists = [] # Мой код будет считать 7 за довавленое число а если без него надо то просто нужно переместить appendпосле if
while True:
    local_number = int(input())
    lists.append(local_number)
    if local_number == 7:
        print(sum(lists), max(lists), min(lists))
        break
    print(sum(lists), max(lists), min(lists))