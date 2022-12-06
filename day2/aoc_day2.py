with open("day2/inputDay2.txt") as f:
    data = f.read().splitlines()

totalScore = 0

playerDict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

playerWinSelection = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

playerLoseSelection = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

playerDrawSelection = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}


def part1():
    outcomeScore = 0
    totalScore = 0
    for line in data:
        # Player's score based on item used
        handScore = playerDict[line[2]]
        # Draw Scenario
        if line[0] == "A" and line[2] == "X":
            outcomeScore = 3
        elif line[0] == "B" and line[2] == "Y":
            outcomeScore = 3
        elif line[0] == "C" and line[2] == "Z":
            outcomeScore = 3
        # Outcome if player's hand is rock
        elif line[0] == "A" and line[2] == "Y":
            outcomeScore = 6
        elif line[0] == "A" and line[2] == "Z":
            outcomeScore = 0
        # Outcome if player's hand is paper
        elif line[0] == "B" and line[2] == "X":
            outcomeScore = 0
        elif line[0] == "B" and line[2] == "Z":
            outcomeScore = 6
        # Outcome if player's hand is scissors
        elif line[0] == "C" and line[2] == "X":
            outcomeScore = 6
        elif line[0] == "C" and line[2] == "Y":
            outcomeScore = 0
        totalScore += handScore + outcomeScore
    print(totalScore)


def part2():
    outcomeScore = 0
    totalScore = 0
    handScore = 0

    for line in data:
        opponentChoice = line[0]
        outcomeNeeded = line[2]
        mode = ""
        # Determine which hand to play (rock, paper, or scissors)
        if outcomeNeeded == 'X':
            mode = "lose"
        elif outcomeNeeded == 'Y':
            mode = "draw"
        elif outcomeNeeded == 'Z':
            mode = "win"

        if mode == "win":
            playerSelection = playerWinSelection[opponentChoice]
            handScore = playerDict[playerSelection]
            outcomeScore = 6

        elif mode == "lose":
            playerSelection = playerLoseSelection[opponentChoice]
            handScore = playerDict[playerSelection]
            outcomeScore = 0

        elif mode == "draw":
            playerSelection = playerDrawSelection[opponentChoice]
            handScore = playerDict[playerSelection]
            outcomeScore = 3

        totalScore += handScore + outcomeScore
    return totalScore


print(part2())
