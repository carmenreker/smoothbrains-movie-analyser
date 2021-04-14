# Authors: Taede Meijer, Sijbren van Vaals

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

# Invoke with:
# compare(script, dictionary_of_subtitles)
