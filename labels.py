#!/bin/python3
# Author(s): Indy van Boven

import sys
import re


def create_labels(text):
    """adds labels to a script and returns the labelled script"""
    #file = argv[1]
    #with open(file, 'r') as inp:
        #text = inp.read()
        
        # replacing tabs with spaces to create indentation
        text = re.sub(r'\n([A-Za-z])', r'\n     \1', text)
        text = re.sub(r'\n\t\t\t\t', r'\n                           ', text)
        text = re.sub(r'\n\t\t\t', r'\n                   ', text)
        text = re.sub(r'\n\t\t', r'\n                 ', text)
        
        # special cases pagenumbers and CUT TO and THE END, metadata
        text = re.sub(r'\n[0-9][0-9]?[0-9]?[A-Z]?', r'\n  ', text) 
        text = re.sub(r'\n\n(\s+CUT TO)', r'\n\nM|\1', text)
        text = re.sub(r'\n\n\n(\s+THE END)', r'\n\n\nM|\1', text)
        
        # indentation scene boundary INT and EXT
        text = re.sub(r'\n(      ?EXT)', r'\nS|\1', text)
        text = re.sub(r'\n(      ?INT)', r'\nS|\1', text)
        
        # special cases for scence description and metadata 
        text = re.sub(r'\n(                CONNECTION)', r'\nN|\1', text)
        text = re.sub(r'\n(                    TRANSFER)', r'\nN|\1', text)
        text = re.sub(r'\n(                   ? ? ? ?\([A-Za-z])', r'\nM|\1', text)
        
        # labels for characters and dialogues
        text = re.sub(r'\n(                           ? ? ? ? ?[A-Z])', r'\nC|\1', text)
        text = re.sub(r'\n(                 ? ? ? ? ?[A-Za-z0-9-\.\"])', r'\nD|\1', text) 
        
        # labels for scene description and specific cases
        text = re.sub(r'\n(                      [A-Za-z])', r'\nN|\1', text)
        text = re.sub(r'\n(                              [A-Za-z])', r'\nN|\1', text)
        text = re.sub(r'\n(      ?[A-Za-z\"])', r'\nN|\1', text)
        text = re.sub(r'\n(     --)', r'\nN|\1', text)
        
        # label for metedata
        text = re.sub(r'\n(                     \(?[A-Za-z])', r'\nM|\1', text)
        
        # adding a | to every empty line or line with a pagenumber
        text = re.sub(r'\n\n\n\n', r'\n |\n |\n |\n |', text)
        text = re.sub(r'\n\n\n', r'\n |\n |\n', text)
        text = re.sub(r'\n\n', r'\n |\n', text)
        labelled_script = re.sub(r'\n(\s+[0-9][0-9]?.)\n', r'\n |\1\n', text)
        
        #print(labelled_script)
        
        return labelled_script

if __name__ == "__main__":
    create_labels(sys.argv)
    
# can be invoked with:
# labelled_script = create_labels(text)