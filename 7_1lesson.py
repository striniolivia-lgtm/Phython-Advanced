# Iteratoren
# iter() und next()
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# Achtung! Wenn keine Werte vorhanden sind
    # print(next(it))  # Exception: StopIteration

# Iterationen sind nur einmal nutzbar
numbers = [1, 2, 3]
it = iter(numbers)

for number in it:
    print(number)

print("Nochmal")
# Beim zweiten Durchlauf kommt nichts

for number in it:
    print(number)

# Eigene iterierbare Klasse bauen
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


count = Counter(5)

for elem in count:
    print(elem)

