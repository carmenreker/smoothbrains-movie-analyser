# Filename: user_interface.py
# Description: Creates the user interface
# Author(s): Sijbren van Vaals

import argparse


def main():
    # def user_interface():

    parser = argparse.ArgumentParser(
                                    description="This programme aligns \
                                    subtitles and movie scripts, \
                                    output is in csv.",
                                    usage="Enter a subtitle(.srt) and a \
                                    movie script(.txt) file, in this order, \
                                    for the programme to align.")
    parser.add_argument(
                        "subtitleFile", metavar="subtitle file",
                        help="the file that contains the subtitles \
                        (.srt extention).",
                        action="append", nargs="+")
    parser.add_argument(
                        "scriptFile", metavar="movie script file",
                        help="the file that contains the movie script \
                        (.txt extention).",
                        action="append", nargs="+")
    args = parser.parse_args()
# NOTE: The files are delivered in a list, so index 0 = subtitle file
# and index 1 = movie script file.
# Voor de return moet je even kieke welke van de twee het handigst is
# voor het programma.
    # return args
    # return args.subtitleFile, args.scriptFile

# Als je het programma wil checken moet je het even in een main zetten
# anders werkt de --help/-h  en de error handling niet :)


if __name__ == "__main__":
    main()
