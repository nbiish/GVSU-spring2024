num_rows = int(input())

increment_this = 1

while increment_this <= num_rows:
    print(' '.join('*' for i in range(increment_this)))
    increment_this += 1
