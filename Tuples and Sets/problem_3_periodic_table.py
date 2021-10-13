n = int(input())
dataset = set()

for _ in range(n):
    data = input().split()
    for current in data:
        dataset.add(current)

for i in dataset:
    print(i)