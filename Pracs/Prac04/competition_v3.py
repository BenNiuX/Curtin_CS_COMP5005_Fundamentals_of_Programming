#
# competition_v3.py - adding submodules
#

def inputValue(lower, upper, prompt):
    input_value = int(input(prompt))
    while input_value < lower or input_value > upper:
        print(f"Error - re-enter number ({lower}-{upper})")
        print(prompt)
        input_value = int(input())
    return input_value

numJudges = 7
numCompetitors = inputValue(3, 16, "Enter number of competitions (3-16 inc)")
for comp in range(numCompetitors):
    totalC = 0
    print("Input scores between 0 and 10 for each Judge")
    for j in range(numJudges):
        scoreJ = inputValue(0, 10, "Score for judge ")
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("Score for competitor ", comp+1, " is", scoreC)
