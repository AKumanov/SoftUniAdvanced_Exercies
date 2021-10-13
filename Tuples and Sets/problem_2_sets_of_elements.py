n, m = [int(x) for x in input().split()]
n_set = set()

m_set = set()

for _ in range(n):
    current = int(input())
    n_set.add(current)

for _ in range(m):
    other = int(input())
    m_set.add(other)


output = n_set.intersection(m_set)
for item in output:
    print(item)