N = int(input("Введіть ціле число N (1 < N < 9): "))

if N <= 1 or N >= 9:
    print("Число N повинно бути більше за 1 і менше за 9.")
else:
    for row in range(N, 0, -1):
        for num in range(N, N - row, -1):
            print(num, end=' ')
        print()
