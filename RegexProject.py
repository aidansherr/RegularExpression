# -*- coding: utf-8 -*-
"""
Regular Expression Project
CS-312

Write a regular expression that will find
the area code, trunk, number, and an 
optional extension and output them from any
string format read in from a file.

By Aidan Sherr
"""

import re

phonePattern = '''^[1]?\s?[-\.]?\s?\(?          # checks start of string
                                                # and will match w/ 0 or 1 1's
                                                # followed by 0 or 1 spaces
                                                # followed by 0 or 1 dashes or dots
                                                # followed by 0 or 1 spaces
                                                # followed by 0 or 1 open parenthesis
                    (\d{3})                     # matches three digits (area code)
                    \)?\s?[-\.]?\s?\(?          # matches 0 or 1 close parenthesis
                                                # followed by 0 or 1 spaces
                                                # followed by 0 or 1 dashes or dots
                                                # followed by 0 or 1 spaces
                                                # followed by 0 or 1 open parenthesis
                    (\d{3})                     # matches three digits (trunk)
                    \)?\s?[-\.]?\s?\(?          # matches 0 or 1 close parenthesis
                                                # followed by 0 or 1 spaces
                                                # followed by 0 or 1 dashes or dots
                                                # followed by 0 or 1 spaces
                                                # followed by 0 or 1 open parenthesis
                    (\d{4})                     # matches four digits (number)
                    \D*                         # matches 0 or many non-decimal characters
                                                # for extension prefix
                    (\d{4})?$'''                # matches four digits (extension) or end
                                                # of line

# open file and check each line for regular expression
with open('phonenumbers.txt') as f:
    for line in f:
        pgroups = re.search(phonePattern, line, re.VERBOSE).groups()
        print("Area Code = ", pgroups[0], "\tTrunk = ", pgroups[1], "\tNumber = ", pgroups[2])
        if pgroups[3]:
            print("Extension = ", pgroups[3])


