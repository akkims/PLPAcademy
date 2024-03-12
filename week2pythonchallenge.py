A = list()
totalElementsOfList = 100 # assuming it is for example 100 elements
for iteration in range(100):
    A.append(input("Value #" + str(iteration) + " :"))

for element in A:
    total += int(element)

print(total)