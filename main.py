# Filename: main.py
# Description: Takes a movie script and a subtitle file and aligns them,
# outputs the aligned file in csv.
# Author(s): Taede Meijer, Sijbren van Vaals

from loadsubtitle import loadsubtitles
from labels import create_labels
from matches import get_matches
from compare import compare
import argparse


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

    compare(labelled_script, subtitle)

    f = open("output.csv", "w")
    f.write("Character,Subtitle,Script,Timestamp,Tag\n")
    f.close()
    f = open("output.csv", "a")

    # Write the character name, subtitle, text of script,
    # timestamp and tag to output.csv.
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
        if str([item][0]) in matching_lines:
            f.write(",")
            f.write([item][0])
            f.write(",")
        else:
            f.write(",,")
        f.write(str(subtitle[item]))
        f.write(",")
        if str([item][0]) in matching_lines:
            place = matching_lines.index(str([item][0]))
            f.write(tags[place])
        else:
            f.write("D")
        f.write("\n")
    f.close()

    print("You can find the aligned file(output.csv) in the current directory")


if __name__ == "__main__":
    main()
