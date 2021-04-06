import re

def loadsubtitles():
    #print("esketit")
    with open('movies/mission_impossible/mi.srt') as sub:
        test = sub.read()
        test = re.sub('<.*?>','', test)
        test = re.sub('- ', '', test)
        print(test)
        print("------------------------------------")
        esketit = re.findall('[0-9][0-9][:][0-9][0-9][:].*[\n\n]', test)
        
        poep = re.findall('[0-9]*[- ]*["]*[a-zA-Z].+[^\s*$]', test)

        print('esketit =', + len(esketit))

        print('poep =', + len(poep))
        print("------------------------------------")
        print("------------------------------------")

        for i in range(30):
            print(esketit[i])
            print(poep[i])

loadsubtitles()

# [0-9]*[- ]*["]*[a-zA-Z].+[^\s*$]
# Die doet het half

# Timestaps 
# \d{2}:\d{2}:\d{2},\d{3}.+[\n]