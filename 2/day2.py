twos = 0
threes = 0

with open("input.txt", "r") as f:
    for item in f:
        temp_twos = 0
        temp_threes = 0
        seen = []
        for letter in item:
            if not letter in seen:
                if item.count(letter) == 2 and temp_twos == 0:
                    twos = twos +1
                    temp_twos = temp_twos +1
                elif item.count(letter) == 3 and temp_threes == 0:
                    threes = threes +1
                    temp_threes = temp_threes +1
            seen.append(letter)

print(twos)
print(threes)
print(twos * threes)