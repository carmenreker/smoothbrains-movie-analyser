#!/bin/python3
# Author: I. van Boven

import sys
import re


def create_labels(argv):
    file = argv[1]
    with open(file, 'r') as inp:
        text = inp.read()                                           # special cases need to go first
        #for i in text:
            #if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                #text = re.sub(r'\n(\s+[A-Za-z0-9])', r'\n     \1', text)
                #text = re.sub(r'\n([A-Za-z0-9])', r'\n     \1', text)
        all_lines = re.sub(r'\n[0-9][0-9]?[0-9]?[A-Z]?', r'\n  ', text) #special cases nummers voor int/ext
        spec_meta = re.sub(r'\n\n(\s+CUT TO)', r'\n\nM|\1', all_lines)
        spec_meta = re.sub(r'\n\n\n(\s+THE END)', r'\n\n\nM|\1', spec_meta)
        
        scene_boundary = re.sub(r'\n(      ?EXT)', r'\nS|\1', spec_meta)
        scene_boundary = re.sub(r'\n(      ?INT)', r'\nS|\1', scene_boundary)
        
        character_label = re.sub(r'\n(                           ? ? ? ? ?[A-Z])', r'\nC|\1', scene_boundary) 
        spec_case_descript = re.sub(r'\n(                CONNECTION)', r'\nN|\1', character_label)
        spec_case_descript = re.sub(r'\n(                    TRANSFER)', r'\nN|\1', spec_case_descript)
        spec_case_meta = re.sub(r'\n(                   ? ? ? ?\([A-Za-z])', r'\nM|\1', spec_case_descript)
        
        dialogue_label = re.sub(r'\n(                 ? ?[A-Za-z0-9-\.\"])', r'\nD|\1', spec_case_meta) 
        
        scene_discription = re.sub(r'\n(                      [A-Za-z])', r'\nN|\1', dialogue_label)
        scene_discription = re.sub(r'\n(                              [A-Za-z])', r'\nN|\1', scene_discription)
        scene_discription = re.sub(r'\n(      ?[A-Za-z\"])', r'\nN|\1', scene_discription)
        scene_discription = re.sub(r'\n(     --)', r'\nN|\1', scene_discription)
        
        metadata = re.sub(r'\n(                     \(?[A-Za-z])', r'\nM|\1', scene_discription)
        #metadata = re.sub(r'\n\n(\s+CUT TO)', r'\n\nM|\1', metadata)
        #metadata = re.sub(r'\n\n\n(\s+THE END)', r'\n\n\nM|\1', metadata)
        
        empty_lines = re.sub(r'\n\n\n\n', r'\n |\n |\n |\n |', metadata)
        empty_lines = re.sub(r'\n\n\n', r'\n |\n |\n', empty_lines)
        empty_lines = re.sub(r'\n\n', r'\n |\n', empty_lines)
        page_numbers = re.sub(r'\n(\s+[0-9][0-9]?.)\n', r'\n |\1\n', empty_lines)
        print(page_numbers)

if __name__ == "__main__":
    create_labels(sys.argv)