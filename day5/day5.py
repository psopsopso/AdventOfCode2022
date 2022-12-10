stacks = {
    "stack_1": ["G", "T", "R", "W"],
    "stack_2": ["G", "C", "H", "P", "M", "S", "V", "W"],
    "stack_3": ["C", "L", "T", "S", "G", "M"],
    "stack_4": ["J", "H", "D", "M", "W", "R", "F"],
    "stack_5": ["P", "Q", "L", "H", "S", "W", "F", "J"],
    "stack_6": ["P", "J", "D", "N", "F", "M", "S"],
    "stack_7": ["Z", "B", "D", "F", "G", "C", "S", "J"],
    "stack_8": ["R", "T", "B"],
    "stack_9": ["H", "N", "W", "L", "C"]
}

with open("inputDay5.txt") as f:
    dataArr = [line.replace("from", "").replace(
        "to", "").replace("move ", "").strip().split() for line in f]

for instructions in dataArr:
    for i in range(int(instructions[0])):
        stacks[f"stack_{instructions[2]}"].append(
            stacks[f"stack_{instructions[1]}"].pop())

result = [f"{v[-1]}" for k, v in stacks.items()]
resultStr = ""
for elem in result:
    resultStr += elem

print(resultStr)
