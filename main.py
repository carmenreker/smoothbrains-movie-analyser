# Filename: main.py
# Description: opens the files and calls the other programs
# Author(s): Taede Meijer, Sijbren van Vaals

from loadsubtitle import *

def match(script, subtitles):
    """Compares the subtitles to the script, and prints the percentage
       of matches"""

    counter_not_in_script = 0
    counter_is_in_script = 0

    # loopt over elke subtitle tekst in de dictionary
    for line in subtitles:

        # checkt of de subtitle tekst ergens in het script staat (dit is nog te vaag)
        if line in script:

            # Uncomment deze twee als je de matches wil printen.
            #print("Match: ", end="")
            #print(line)
            counter_is_in_script += 1

        else:
            counter_not_in_script += 1    
    
    print("De ondertiteling matcht voor {}{} met het script".format(round(counter_is_in_script / (counter_is_in_script + counter_not_in_script) * 100, 2), "%"))

def main():

    with open('movies/mission_impossible/mi.txt', 'r') as script:
        movie = script.read()

        # Uncomment deze code om de movie te printen voor debuggen ofzo, zelf weten
        #print(movie)

    data = loadsubtitles('movies/mission_impossible/mi.srt')        

    # Uncomment deze code om de functie uit te voeren
    match(movie, data)

if __name__ == "__main__":
    main()

# Wat nog moet:
# De juiste naam bij de subtitle zetten ?
# Timestamp moet in het script. ( Daarvoor is het handig 
#   als het hele script gewoon 1 lange string is, dan kunnen
#   we die opslaan naar een nieuwe script.txt )