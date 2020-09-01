number = 1
count = 0
while number <= 10:
    if (number % 2) == 0:
        print(number)
        count = count + 1
    number = number + 1
print(f"Tuvimos {count} números pares")
