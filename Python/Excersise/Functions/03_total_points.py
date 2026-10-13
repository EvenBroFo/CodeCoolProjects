def total_points(matchresult):
    points = 0
    for result in matchresult:
        scores = result.split(":")
        team_score = int(scores[0])
        opponent_score =int(scores[1])
        if team_score > opponent_score:
            points += 3
        elif team_score == opponent_score:
             points += 1
        elif opponent_score > team_score:
            points += 0 

    return points
        

matches = ["3:1", "2:2", "0:1"]
matches2 = ["3:4", "10:0", "20:0", "2:1", "3:2", "10:10", "20:20"]

print(total_points(matches))
print(total_points(matches2))