inputs = []
while True:
    inp = input()
    if inp == "0":
        inputs.append(int(inp))
        break
    inputs.append(int(inp))

for i in range(len(inputs)-1,-1,-1):
    print(inputs[i])