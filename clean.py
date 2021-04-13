# Filename : clean.py
# Description : This program cleans the text of the script
# and the subtitles for proper sentence matching.
# Author(s): Carmen Reker

import re


def clean(filepath):
    with open(filepath, 'r') as inp:
        subs = inp.read()

        # removes angle brackets like italic indications
        subs = re.sub('<.*?>', '', subs)
        # removes indicators denoting multiple sentences
        subs = re.sub('- ', '', subs)

    # print(subs)
    return subs

# invoke with:
# clean('testfiles/cleantest.txt')
