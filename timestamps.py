# Author: Taede Meijer

def add_timestamps(script, subtitles):
    """Adds timestamps to the script where subtitles match """
    for line in subtitles:
        if line in script:
            #print(line)
            index = script.find(line)

            #print(subtitles[line])
            script = script[:index] + subtitles[line] + " " + script[index:]

    return(script)