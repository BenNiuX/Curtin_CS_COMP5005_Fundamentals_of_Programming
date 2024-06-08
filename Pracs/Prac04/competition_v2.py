#
# competition_v2.py - validating inputs
#

numJudges = 7
numCompetitors = int(input("Enter number of competitors (3-16 inc):"))
while numCompetitors < 3 or numCompetitors > 16:
    numCompetitors = int(input("Error - Re-enter number of competitors (3-16 inc):"))
for comp in range(numCompetitors):
    totalC = 0
    print("Input scores between 0 and 10 for each Judge")
    for j in range(numJudges):
        scoreJ = int(input("Score for judge "))
        while scoreJ < 0 or scoreJ > 10:
            scoreJ = int(input("Error - Re-enter score (0-10)"))
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("Score for competitor ", comp+1, " is", scoreC)
