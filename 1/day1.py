
def add_num(x, result_list):
    with open ("input.txt", "r") as f:
        for num in f:
            x = x + int(num)
            result_list.append(x)
    return x

def find_dupe(result_list, q):
    #print("LOOKING")
    start = result_list[q]
    for item in result_list:
        if (item > 0) and (item == start):
            print("SOLUTION: " + str(item))
            return True
    return False

x = 0
result_list = []
q = 0
add_num(x, result_list) #GIVES SOLUTION TO PART 1
#print(result_list)
match = find_dupe(result_list, q)
while (not match):
    add_num(x, result_list)
    match = find_dupe(result_list, q)
    q = q+1
    print(q)