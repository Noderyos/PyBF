values = [0]*30000
loops = []
ptr = 0
cur = 0

INPUT = input("Input BF Code: ")
while cur < len(INPUT):
	if INPUT[cur] == ">": ptr+=1
	if INPUT[cur] == "<": ptr-=1

	if INPUT[cur] == "+": values[ptr]+=1
	if INPUT[cur] == "-": values[ptr]-=1

	if INPUT[cur] == ".": print(chr(values[ptr]),end="")
	if INPUT[cur] == ",": values[ptr] = ord(input(""))

	
	if INPUT[cur] == "[": loops.append(cur)
	if INPUT[cur] == "]":
		if values[ptr] != 0:
			cur = loops.pop() - 1
	cur+=1
