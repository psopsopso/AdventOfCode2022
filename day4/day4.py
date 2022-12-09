with open("inputDay4.txt") as f:
    data = f.read().splitlines()

print(data)


def containsSum(data):
    sum = 0
    for pair in data:
        split_pair = pair.split(",")

        first_elf = split_pair[0]
        second_elf = split_pair[1]

        first_elf_split = first_elf.split("-")
        second_elf_split = second_elf.split("-")

        first_elf_stations = [i for i in range(
            int(first_elf_split[0]), int(first_elf_split[1])+1)]

        second_elf_stations = [i for i in range(
            int(second_elf_split[0]), int(second_elf_split[1])+1)]

        if len(first_elf_stations) >= len(second_elf_stations):
            biggestList = first_elf_stations
            shortestList = second_elf_stations
        else:
            biggestList = second_elf_stations
            shortestList = first_elf_stations

        contains = all(item in biggestList for item in shortestList)
        if contains:
            sum += 1
    return sum


print(containsSum(data))
