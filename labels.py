#!/bin/python3
# Author: I. van Boven

import sys
import re


def create_labels(argv):
    file = argv[1]
    with open(file, 'r') as inp:
        text = inp.read()
        character_label = re.sub(r'\n(                          [A-Z])', r'\nC|\1', text) 
        dialogue_label = re.sub(r'\n(                [A-Za-z0-9-\.\"])', r'\nD|\1', character_label) 
        scene_boundary = re.sub(r'\n(     EXT)', r'\nS|\1', dialogue_label)
        scene_boundary = re.sub(r'\n(     INT)', r'\nS|\1', scene_boundary)
        
        scene_discription = re.sub(r'\n(                      [A-Za-z])', r'\nN|\1', scene_boundary)
        scene_discription = re.sub(r'\n(                              [A-Za-z])', r'\nN|\1', scene_discription)
        scene_discription = re.sub(r'\n(     [A-Za-z\"])', r'\nN|\1', scene_discription)
        scene_discription = re.sub(r'\n(     --)', r'\nN|\1', scene_discription)
        
        metadata = re.sub(r'\n(                     \(?[A-Za-z])', r'\nM|\1', scene_discription)
        metadata = re.sub(r'\n\n(\s+CUT TO)', r'\n\nM|\1', metadata)
        metadata = re.sub(r'\n\n\n(\s+THE END)', r'\n\n\nM|\1', metadata)
        
        empty_lines = re.sub(r'\n\n\n\n', r'\n |\n |\n |\n |', metadata)
        empty_lines = re.sub(r'\n\n\n', r'\n |\n |\n', empty_lines)
        empty_lines = re.sub(r'\n\n', r'\n |\n', empty_lines)
        print(empty_lines)

if __name__ == "__main__":
    create_labels(sys.argv)