def countingValleys(steps,path):
    Mountain = 0
    valley = 0
    for step in path:
        if step == "U":
            Mountain += 1
        else:
            Mountain -= 1
        if step == "U" and Mountain == 0:
            valley += 1
    return valley


