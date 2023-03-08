total = 0
for i in range(5):
    number = int(input("insert a number: "))
    answer = input("do you want add number to total?(yes/no)")
    if answer.lower().startswith('y'):
        total += number
    else:
        continue
print(total)