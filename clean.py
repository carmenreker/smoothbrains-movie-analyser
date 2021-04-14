# Filename : clean.py
# Description : This program cleans the text of the script
# and the subtitles for proper sentence matching.
# Author(s): Carmen Reker

import re


def clean(subs):
    """ Cleans the script and returns the clean text """
    # removes angle brackets like italic indications
    subs = re.sub('<.*?>', '', subs)
    # removes indicators denoting multiple sentences
    subs = re.sub('- ', '', subs)

    return subs

# invoke with:
# clean(string_to_be_cleaned)
