# Author: Taede Meijer

import re

def add_names(script, subtitles):

    # We create two lists that run parallel to each other
    # matching_lines[5] contains the line that matches
    # and character_names[5] contains the speaker of that matching line. 
    matching_lines = []
    character_names = []

    amount = script.count("C|")

    for i in range(amount):
        first = script.find("C|")

        # Replace the first C with a placeholder, so we can locate the next 
        script = script.replace("C|", "PLACEHOLDER", 1)
        second = script.find("C|")

        # Saves the string in between the first and second 'C|'
        temporary_text = script[first:second]

        temporary_text = temporary_text.replace("                          ", " - ")

        for line in subtitles:

            # If a line in the subtitles has been found in the temporary text:
            if line in temporary_text:

                matching_lines.append(line)

                # Save the name of the current speaker
                name = re.match('^PLACEHOLDER\s.+\n', temporary_text)
                name = name.group().replace("PLACEHOLDER - ", "")
                name = name.replace("\n", "")
                character_names.append(name)

    return matching_lines, character_names