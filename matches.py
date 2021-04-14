# Filename: matches.py
# Description: Two functions that return the timestamps, character names and tags of matching lines.
# Author: Taede Meijer

import re


def get_tag(sub, text):
    """ Grabs the tags and returns them in a list """

    # Removes all the double spaces, to make the search more efficient.
    while text.count("  ") > 0:
        text = text.replace("  ", " ")

    index = text.find(sub)

    # Save the text up to the current index. This way we can loop back to grab
    # the tag of the match.
    text = text[:index]

    i = 0
    while i < (len(text)) and text[-i] != "|":
        i += 1
        # Save the tag at index -1 if the current character is a "|""
        if text[-i] == "|":

            tag = text[-i-1]

    return tag
# Invoke with:
# get_tag(matching subtitle, text to find the tag in)


def get_matches(script, subtitles):
    """ Returns a list of matching lines, with according character names,
        timestamps and tags. """

    # We create three lists that run parallel to each other
    # timestamps[5] contains the timestamp of the matching line
    # matching_lines[5] contains the line that matches
    # and character_names[5] contains the speaker of that matching line.
    timestamps = []
    character_names = []
    matching_lines = []
    tags = []

    # Loop over small parts of the script
    amount = script.count("C|")

    for i in range(amount):
        first = script.find("C|")

        # Replace the first C| with a placeholder, so we can locate the next
        script = script.replace("C|", "PLACEHOLDER", 1)
        second = script.find("C|")

        # Saves the string in between the first and second occuring 'C|'
        temporary_text = script[first:second]

        temporary_text = temporary_text.replace(
            "                          ", " - ")

        # Loops over every saved subtitle
        for line in subtitles:

            # If a line in the subtitles has been found in the temporary text:
            if line in temporary_text:

                matching_lines.append(line)
                timestamps.append(subtitles[line])

                # Save the name of the current speaker
                name = re.match(r'^PLACEHOLDER\s.+\n', temporary_text)
                name = name.group().replace("PLACEHOLDER - ", "")
                name = name.replace("\n", "")
                character_names.append(name)

                tags.append(get_tag(line, temporary_text))

    return timestamps, character_names, matching_lines, tags
# Invoke with:
# get_matches(labelled_script, dictionary_of_subtitles)
