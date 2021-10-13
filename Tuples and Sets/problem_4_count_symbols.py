dataset = set()
text = input()
for current in text:
    dataset.add(current)
collection = {}
for i in dataset:
    collection[i] = text.count(i)
collection = sorted(collection.items())
for item, value in collection:
    print(f"{item}: {value} time/s")