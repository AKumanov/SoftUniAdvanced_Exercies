n = int(input())

evens = set()
odds = set()

index = 1
for _ in range(n):
    name = input()
    ascii_value = 0
    for char in name:
        ascii_value += ord(char)
    output = int(ascii_value / index)
    if output % 2 == 0:
        evens.add(output)
    else:
        odds.add(output)
    index += 1

if sum(evens) == sum(odds):
    final = list(evens.union(odds))
    print(', '.join([str(x) for x in final]))
elif sum(odds) > sum(evens):
    final = list(odds.difference(evens))
    print(', '.join([str(x) for x in final]))
else:
    final = list(evens.symmetric_difference(odds))
    print(', '.join([str(x) for x in final]))
