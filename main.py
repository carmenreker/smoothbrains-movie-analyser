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
                                    usage="Enter a subtitle (.srt) and a"
                                    "movie script (.txt) file, in this order,"
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

    with open(args.scriptFile[0][0], 'r') as script:
        text = script.read()
        labelled_script = create_labels(text)

        # Uncomment deze code om de movie te printen voor debuggen ofzo, zelf weten
        # print(movie)
    # subtitle_file = args.subtitleFile[0]
    # print(str(subtitle_file))
    subtitle = loadsubtitles(args.subtitleFile)

    labelled_script = add_timestamps(labelled_script, subtitle)
    
    # Get two lists, one with matching lines between the subtitles and script, 
    # the other with the character names
    matching_lines, character_names = add_names(labelled_script, subtitle)
    # print(matching_lines, character_names)
    
    # Print the amount of matches between the subtitles and script
    match(labelled_script, subtitle)

    
if __name__ == "__main__":
    main()

# Wat nog moet:
# De juiste naam bij de subtitle zetten ?
