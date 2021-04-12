# Filename: main.py
# Description: opens the files and calls the other programs
# Author(s): Taede Meijer, Sijbren van Vaals

from loadsubtitle import loadsubtitles
from timestamps import add_timestamps
from labels import create_labels
from names import add_names
import argparse

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
            # print("Match: ", end="")
            # print(line)
            counter_is_in_script += 1

        else:
            counter_not_in_script += 1      

    print("De ondertiteling matcht voor {}{} met het script".format(round(counter_is_in_script / (counter_is_in_script + counter_not_in_script) * 100, 2), "%"))


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

        # Uncomment deze code om de movie te printen voor debuggen ofzo, zelf weten
        # print(movie)
    # subtitle_file = args.subtitleFile[0]
    # print(str(subtitle_file))
    subtitle = loadsubtitles(args.subtitleFile)
    
    labelled_script = add_timestamps(labelled_script, subtitle)
    print(labelled_script)
    # Get two lists, one with matching lines between the subtitles and script, 
    # the other with the character names
    matching_lines, character_names = add_names(labelled_script, subtitle)
    #print(matching_lines, character_names)
    #print(matching_lines)
    # print(character_names)
    # Print the amount of matches between the subtitles and script
    match(labelled_script, subtitle)
    print(type(character_names))
    print(type(subtitle))
    print(type(labelled_script))
    #print(len(subtitle))
    #print(subtitle)
    
    
    f = open("output.csv", "w")
    f.write("Character,Subtitle,Script,Timestamp,Tag\n")
    f.close
    f = open("output.csv", "a")
    #for i in range(len(matching_lines)):
        #print(character_names[i],matching_lines[i])
        
    
    for count, item in enumerate(subtitle):
        if str([item][0]) in matching_lines: # Check if subtitle in match
            place = matching_lines.index(str([item][0])) # Find the index of the match
            f.write(character_names[place]) # Write the corresponding name to the match
            f.write(",")
        else:
            f.write(",")
        #f.write("Character,")
        #f.write(character_names[count])
        #f.write(",")
        f.write(str([item][0]))
        f.write(",Tekst script,")
        f.write(str(subtitle[item]))
        f.write(",Tag\n")
    
if __name__ == "__main__":
    main()

# Wat nog moet:
# De juiste naam bij de subtitle zetten ?
