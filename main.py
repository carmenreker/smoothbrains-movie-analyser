# Filename: main.py
# Description: opens the files and calls the other programs
# Author: Taede Meijer (als je iets verandert/toevoegd, je naam erbij gooien)


def main():
    with open('movies/mission_impossible/mi.txt', 'r') as script:
        with open('movies/mission_impossible/mi.srt', 'r') as subtitles:
            for line in subtitles:
                print(line)


if __name__ == "__main__":
    main()
