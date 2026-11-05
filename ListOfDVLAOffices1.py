import string as s # required for the code below
UPPER_ABCS = list(s.ascii_uppercase) # This contains all of the alphabet in uppercase as a list
List_Of_DLVA_Offices = [['Anglia', # This is the mnemonic used for the area
    ['Peterborough',['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N']],
    ['Norwich',['O', 'P', 'R', 'S', 'T', 'U']], # This is all of the second letters that belong to the certain office
    ['Ipswich',['V', 'W', 'X', 'Y']]],
['Birmingham',
    ['Birmingham',[Letter for Letter in UPPER_ABCS if Letter not in ['Q','I','Z']]]], # This contains all of the letter except 'Q','I', and 'Z'
['Cymru',
    ['Cardiff',['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O']], 
    ['Swansea',['P', 'R', 'S', 'T', 'U', 'V']],
    ['Bangor',['W', 'X', 'Y']]], 
['Deeside', 
    ['Chester', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']], 
    ['Shrewsbury', ['L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]], 
['Essex', 
    ['Chelmsford', [Letter for Letter in UPPER_ABCS if Letter not in ['Q','I','Z']]]], 
['Forest & Fens', # also known as F
    ['Nottingham', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P']], 
    ['Lincoln', ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]], 
['Garden of England', # also known as G
    ['Maidstone', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O']], 
    ['Brighton', ['P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]], 
['Hampshire & Dorset', #also known as H
    ['Bournemouth', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']], 
    ['Portsmouth', ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'X', 'Y']],
    ['Portsmouth (Isle of Wight)',['W']]], 
['(No official mnemonic)', # also known as K
    ['Luton', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L']], 
    ['Northampton', ['M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]], 
['London', 
    ['Wimbledon', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']], 
    ['Stanmore', ['K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T']], 
    ['Sidcup', ['U', 'V', 'W', 'X', 'Y']]], 
['Manchester', 
    ['Manchester', [Letter for Letter in UPPER_ABCS if Letter not in ['Q','I','Z']]]],
['North', 
    ['Newcastle', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O']], 
    ['Stockton', ['P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]], 
['Oxford', 
    ['Oxford', [Letter for Letter in UPPER_ABCS if Letter not in ['Q','I','Z']]]],
['Preston', 
    ['Preston', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T']], 
    ['Carlisle', ['U', 'V', 'W', 'X', 'Y']]], 
['Reading', 
    ['Reading', [Letter for Letter in UPPER_ABCS if Letter not in ['Q','I','Z']]]], 
['Scotland', 
    ['Glasgow', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']], 
    ['Edinburgh', ['K', 'L', 'M', 'N', 'O']], 
    ['Dundee', ['P', 'R', 'S', 'T']], 
    ['Aberdeen', ['U', 'V', 'W']], 
    ['Inverness', ['X', 'Y']]], 
['Severn Valley', # also known as V
    ['Worcester', [Letter for Letter in UPPER_ABCS if Letter not in ['Q','I','Z']]]], 
['West of England', # also known as W
    ['Exeter', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']], 
    ['Truro', ['K', 'L']], 
    ['Bristol', ['M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]], 
['Yorkshire', 
    ['Leeds', ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']], 
    ['Sheffield', ['L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U']], 
    ['Beverley', ['V', 'W', 'X', 'Y']]]]

