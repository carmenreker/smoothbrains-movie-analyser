# Filename: compare.py
# Description: Prints the percentage of how many sentences in the
#              subtitles match with the script
# Authors: Taede Meijer, Sijbren van Vaals


def compare(script, subtitles):
    """ Prints the percentage of how many sentences in the subtitles
        match with the script """

    counter_not_in_script = 0
    counter_is_in_script = 0
    script = script.lower()
    # Loops over every subtitle text in the dictionary
    for line in subtitles:
        line = line.lower()

        # Checks if the subtitle text is somewhere in the script
        if line in script:

            counter_is_in_script += 1

        else:
            counter_not_in_script += 1

    print("The subtitles matches for {}{} with the script".format(
        round(counter_is_in_script / (counter_is_in_script +
              counter_not_in_script) * 100, 2), "%"))

# Invoke with:
# compare(script, dictionary_of_subtitles)
