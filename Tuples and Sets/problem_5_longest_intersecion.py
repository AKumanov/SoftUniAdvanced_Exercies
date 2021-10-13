n = int(input())
max_intersection = set()

for _ in range(n):
    set_1 = set()
    set_2 = set()
    left_range, right_range = input().split("-")
    left_range = left_range.split(',')
    right_range = right_range.split(',')
    for left in range(int(left_range[0]), int(left_range[1]) + 1):
        set_1.add(left)
    for right in range(int(right_range[0]), int(right_range[1]) + 1):
        set_2.add(right)
    current_intersection = set_1.intersection(set_2)
    if len(current_intersection) > len(max_intersection):
        max_intersection = current_intersection
max_intersection = list(max_intersection)
print(f"Longest intersection is [{', '.join([str(x) for x in max_intersection])}] with length {len(max_intersection)}")