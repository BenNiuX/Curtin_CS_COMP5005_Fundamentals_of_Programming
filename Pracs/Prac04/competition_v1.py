#
# competition_v1.py - overall structure
#
numJudges = 7
numCompetitors = int(input("Enter # of competitors (3-16 inc):"))
for comp in range(numCompetitors):
    totalC = 0
    print("Input scores between 0 and 10 for each Judge")
    for j in range(numJudges):
        scoreJ = int(input("Score for judge "))
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("Score for competitor ", comp+1, " is", scoreC)
