# smoothbrains-movie-analyser
# Manual

How to run the program:
python3 main.py path/file1 path/file2 (if file1 or file2 is in the current directory, then path/ is not necessary, only the filename is used)

Where path/file1 is a path to the srt file containing the subtitles from the movie. 
Where path/file2 is a path to the txt file containing the script from the movie.

For instance:
python3 main.py movies/mission_impossible/mi.srt movies/mission_impossible/mi.txt
This command line will be make project reproducible. 

Project:
The goal is to create a preprocessing tool that aligns the matching subtitles and lines in the script. To learn to work together via a version control system, in this case GitHub. 
The project takes two files in the command line, a srt file and a txt file. The project consists of a user interface that helps when incorrect files are given in the command line. 
The main program then invokes labels.py where the lines in the script are labelled for scene boundary (S), scene description (N), dialogues (D), characternames (C) and metadata (M). 
Main.py then invokes loadsubtitle.py where the subtitles are put into a dictionnary and returned to main. Thereafter, main.py write the labelled script to a txt file. Following, main.py invokes matches.py which then returns a list of matching lines, character names, timestamps and tags. Then, main.py invokes compare.py which compares the subtitles to the script, and prints the percentage of matches. Main.py then writes titles of columns and the values of these columns to output.csv.

Team:
Taede: loadsubtitle.py, matches.py (timestamps, characternames, tags subtitles/script), main.py (comparing matches subtitles and script)
Carmen: unit tests (for each function), clean.py, loadsubtitle.py, pycodestyle
Indy: labels.py (S scene description, N scene boundary, D dialogue, C charactername, M metadata for lines in script), unit tests with Carmen, manual
Sijbren: user interface in main.py, loadsubtitle.py, manual, csv output, main.py (comparing matches subtitles and script)
Everyone helped each other with the functions, and there were many discord calls.

We a created a discussion where all the dificluties and obstacles during the project are discussed. Moreover, this section contains a few problems which we were unable to solve with the explanations.

# Discussion

labels.py :

- De labelling is niet 100% correct. Dit was een groot probleem voor ons 
omdat de format van de scripts heel erg verschillend was. We hebben geprobeerd om
zoveel mogelijk formats te betrekken, maar sommigen waren te inconsistent of hadden
meerdere typen tekst op dezelfde indentatie.

loadsubtitle.py :

- We hebben door een dictionary te gebruiken problemen gehad met scriptlines die
meerdere keren voorkwamen. We hadden echter het gevoel dat een dictionary hier 
de meest efficiente manier was om de subtitles op te slaan.

main.py/output.csv :

- De output is niet zoals de voorbeelden op het discussion board, maar
deze output werd pas een paar dagen voor de deadline duidelijk. Ons programma is
gebouwd op pure sentence matching en is niet berekend op 'niet-perfecte' matches.
Ook lukte het ons niet om alle zinnen uit het script te extracten samen met de 
bijbehorende tags. Hierdoor staat bijna alleen de dialoog in de output.
