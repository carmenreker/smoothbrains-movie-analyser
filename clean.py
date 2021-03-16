# Filename : clean.py
# Description : This program cleans the text of the script
# and the subtitles for proper sentence matching.

import re

def clean():
    #s = '<i>Za Druziye.<i>'
    #t = '- yeah.'
    print(re.sub('<.*?>','', s))
    print(re.sub('- ', '', t))
    
clean()