# Part 4 Exercise 21
# From negative to positive

N = int(input("Please type in a positive integer: "))
negative_N = (N - N) - N
range_N = N + 1

for i in range(negative_N, range_N):
    if i == 0:
        continue
    else:
        print(i)