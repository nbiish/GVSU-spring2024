first_input = int(input())
second_input = int(input())

if second_input < first_input:
    print("Second integer can't be less than the first")
else:
    while first_input <= second_input:
        print(first_input, end=' ')
        first_input += 5
    print()
