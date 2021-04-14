# Filename: main.py
# Description: opens the files and calls the other programs
# Author(s): Taede Meijer, Sijbren van Vaals

from loadsubtitle import loadsubtitles
from labels import create_labels
#from timestamps import add_timestamps
from matches import get_matches
import argparse


def compare(script, subtitles):
    """Compares the subtitles to the script, and prints the percentage
       of matches"""

    counter_not_in_script = 0
    counter_is_in_script = 0

    # loops over each subtitle text in the dictionary
    for line in subtitles:

        # checks if the subtitle text is somewhere in the script
        if line in script:

            counter_is_in_script += 1

        else:
            counter_not_in_script += 1

    print("De ondertiteling matcht voor {}{} met het script".format(
        round(counter_is_in_script / (counter_is_in_script +
              counter_not_in_script) * 100, 2), "%"))


def main():

    parser = argparse.ArgumentParser(
                                    description="This programme aligns \
                                    subtitles and movie scripts, \
                                    output is in csv.",
                                    usage="Enter a subtitle (.srt) and a "
                                    "movie script (.txt) file, in this order, "
                                    "for the programme to align.")
    parser.add_argument(
                        "subtitleFile", metavar="subtitle file",
                        help="the file that contains the subtitles"
                        "(.srt extention).",
                        action="append", nargs="+")
    parser.add_argument(
                        "scriptFile", metavar="movie script file",
                        help="the file that contains the movie script"
                        "(.txt extention).",
                        action="append", nargs="+")
    args = parser.parse_args()

    labelled_script = create_labels(args.scriptFile)

    subtitle = loadsubtitles(args.subtitleFile)

    # Output the script to labelled_script.txt. 
    output_script = open("labelled_script.txt", "w")
    output_script.write(labelled_script)
    output_script.close()
    

    # Get four lists, one with timestamps when matches occur, one with the
    # character name of the matched line, and one of the matched line
    timestamps, character_names, matching_lines, tags = (
        get_matches(labelled_script, subtitle))


    #for i in range(len(matching_lines)):
    #    print(timestamps[i], character_names[i], matching_lines[i], tags[i])
    #print(len(timestamps), len(character_names), len(matching_lines), len(tags))

    print("\n\nDit zijn alle matches die we hebben. \n"
          "Hier zitten duplicates in als één stuk tekst \
          uit de ondertiteling 2x in het script zit :/ \n"
          "Het staat niet op volgorde van tijd :/\n"
          "Bij loadsubtitle() wordt ingelezen als een dict, \
          als er in de ondertiteling dezelfde tekst bij meerdere \
          timestamps staat, \
          dan wordt alleen de laatste timestamp wordt opgeslagen :/ \n\n")

    # Print the amount of matches between the subtitles and script
    compare(labelled_script, subtitle)

    f = open("output.csv", "w")
    f.write("Character,Subtitle,Script,Timestamp,Tag\n")
    f.close()
    f = open("output.csv", "a")

    for count, item in enumerate(subtitle):
        # Check if subtitle in match
        if str([item][0]) in matching_lines:
            # Find the index of the match
            place = matching_lines.index(str([item][0]))
            # Write the corresponding name to the match
            f.write(character_names[place])
            f.write(",")
        else:
            f.write(",")
        f.write(str([item][0]))
        f.write(",Tekst script,")
        f.write(str(subtitle[item]))
        f.write(",")
        if str([item][0]) in matching_lines:
            place = matching_lines.index(str([item][0]))
            f.write(tags[place])
        else:
            f.write("D")
        f.write("\n")
    f.close() 

if __name__ == "__main__":
    main()
