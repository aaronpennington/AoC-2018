
def add_num(x):
    with open ("input.txt", "r") as f:
        for num in f:
            x = x + int(num)
    return x

x = 0
y = add_num(x)
print(y) #GIVES SOLUTION TO PART 1

#Provided by u/mcpower_ on reddit. Thanks.
import itertools
data = [int(x) for x in open("input.txt").readlines()]
print(sum(data))

freq = 0
seen = set([0])
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break #SOLUTION TO PART 2
    seen.add(freq)