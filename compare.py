def loadsubtitles():
    print("esketit")
    with open('movies/mission_impossible/mi.srt') as sub:
        lines = sub.readlines()
        print(lines)

loadsubtitles()