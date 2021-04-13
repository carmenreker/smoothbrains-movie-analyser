# Author: Taede Meijer

import re


def get_tag(sub, text):
    """ Grabs the tags and returns them in a list """

    # Removes all the double spaces, to make the search more efficient.
    while text.count("  ") > 0:
        text = text.replace("  ", " ")
    
    index = text.find(sub)
    #print("\n\n===========================================================\n")
    #print(sub, index)
    #print(text)

    #print("-----------------------------------------------------------\n")
    text = text[:index]
    #print(text)

    tags = ""
    i = 0
    while i < (len(text)) and text[-i] != "|":
        i += 1
        #print(i, text[-i])
        if text[-i] == "|":

            tag = text[-i-1]

    
    return tag
    #for i in range(len(text)):
        #print(text[i-1])

    

    

    
    
    
    
    
    
    

    #tag = text[text.find(sub)-3]
    #print("EY YO DE TAG VAN DIE HIERBOVEN IS: ", tag)


def add_names(script, subtitles):

    # We create three lists that run parallel to each other
    # timestamps[5] contains the timestamp of the matching line
    # matching_lines[5] contains the line that matches
    # and character_names[5] contains the speaker of that matching line.
    timestamps = []
    character_names = []
    matching_lines = []
    tags = []

    amount = script.count("C|")

    for i in range(amount):
        first = script.find("C|")

        # Replace the first C with a placeholder, so we can locate the next
        script = script.replace("C|", "PLACEHOLDER", 1)
        second = script.find("C|")

        # Saves the string in between the first and second 'C|'
        temporary_text = script[first:second]

        temporary_text = temporary_text.replace(
            "                          ", " - ")

        # Loopt over de opgeslagen zinnen in de ondertiteling
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

    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ DIT ZIJN DE TAGS HOPELIJK\n", tags)
    return timestamps, character_names, matching_lines, tags
