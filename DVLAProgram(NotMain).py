#DVLA programme to check and generate licence plate

#define my CONSTANTS
SEPFEB_ADD_ON = 50
REQ_CHARS = 7
INVALID_LETTERS = 'QIZ'
VALID_FIRST_LETTERS = 'ABCDEFGHKLNMOPRSVWY'
INVALID_FIRST_LETTERS = "QIZJTUX"
VALID_SECOND_LETTERS = 'ABCDEFGHJKLMNOPRSTUVWXY'

# arrays

GROUPED_MAP = {
    # ANGLIA
    "Peterborough": ("Anglia", ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN"]),
    "Norwich": ("Anglia", ["AO", "AP", "AR", "AS", "AT", "AU"]),
    "Ipswich": ("Anglia", ["AV", "AW", "AX", "AY"]),
    
    # BIRMINGHAM
    "Birmingham":("Birmingham",["BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY"]),
    
    # CYMRU (WALES)
    "Cardiff": ("Cymru/Wales", ["CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CJ", "CK", "CL"]),
    "Swansea": ("Cymru/Wales", ["CM", "CN", "CO"]),
    "Bangor": ("Cymru/Wales", ["CP", "CR", "CS", "CT", "CU", "CV"]),
    
    # DEESIDE TO SHREWSBURY
    "Chester": ("Deeside / Shrewsbury", ["DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DJ"]),
    "Shrewsbury": ("Deeside / Shrewsbury", ["DK", "DL", "DM", "DN", "DO", "DP", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY"]),
    
    # ESSEX
    "Chelmsford": ("Essex", ["EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY"]),
    
    # FOREST AND FENS
    "Nottingham": ("Forest and Fens", ["FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FJ", "FK", "FL", "FM", "FN", "FP"]),
    "Lincoln": ("Forest and Fens", ["FR", "FS", "FT", "FV", "FW", "FX", "FY"]),
    
    # GARDEN OF ENGLAND
    "Maidstone": ("Garden of England", ["GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN"]),
    "Brighton": ("Garden of England", ["GO", "GP", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY"]),
    
    # HAMPSHIRE AND DORSET
    "Bournemouth": ("Hampshire and Dorset", ["HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HJ"]),
    "Portsmouth": ("Hampshire and Dorset", ["HK", "HL", "HM", "HN", "HO", "HP", "HR", "HS", "HT", "HU", "HV", "HW", "HX", "HY"]),
    
    # LUTON AND NORTHAMPTON
    "Luton": ("Luton / Northampton", ["KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KJ", "KK", "KL"]),
    "Northampton": ("Luton / Northampton", ["KM", "KN", "KO", "KP", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY"]),
    
    # LONDON
    "Wimbledon": ("London", ["LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LJ"]),
    "Stanmore": ("London", ["LK", "LL", "LM", "LN", "LO", "LP", "LR", "LS", "LT"]),
    "Sidcup": ("London", ["LU", "LV", "LW", "LX", "LY"]),
    
    # MANCHESTER AND MERSEYSIDE
    "Manchester":("Manchester",["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MJ", "MK", "ML", "MM", "MN", "MP", "MT", "MU", "MV", "MW", "MX", "MY","MS"]),
    
    # NORTH
    "Newcastle": ("North", ["NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NJ", "NK", "NL", "NM", "NN", "NO"]),
    "Stockton": ("North", ["NP", "NR", "NS", "NT", "NU", "NV", "NW", "NX", "NY"]),
    
    # OXFORD
    "Oxford": ("Oxford", ["OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OJ", "OK", "OL", "OM", "ON", "OO", "OP", "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY"]),
    
    # PRESTON
    "Preston": ("Preston / Carlisle", ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PJ", "PK", "PL", "PM", "PN", "PO", "PP", "PR", "PS", "PT", "PU", "PV", "PW", "PX", "PY"]),
    
    # READING
    "Reading": ("Reading", ["RA", "RB", "RC", "RD", "RE", "RF", "RG", "RH", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RR", "RS", "RT", "RU", "RV", "RW", "RX", "RY"]),
    
    # SCOTLAND
    "Glasgow": ("Scotland", ["SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ"]),
    "Edinburgh": ("Scotland", ["SK", "SL", "SM", "SN", "SO"]),
    "Dundee": ("Scotland", ["SP", "SR", "SS", "ST"]),
    "Aberdeen": ("Scotland", ["SU", "SV", "SW", "SX"]),
    "Inverness": ("Scotland", ["SY"]),
    
    # SEVERN VALLEY
    "Worcester": ("Severn Valley", ["VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VJ", "VK", "VL", "VM", "VN", "VO", "VP", "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY"]),
    
    # WEST OF ENGLAND
    "Exeter": ("West of England", ["WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH"]),
    "Truro": ("West of England", ["WJ", "WK", "WL"]),
    "Bristol": ("West of England", ["WM", "WN", "WO", "WP", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY"]),
    
    # YORKSHIRE
    "Leeds": ("Yorkshire", ["YA", "YB", "YC", "YD", "YE", "YF", "YG", "YH", "YJ", "YK", "YL"]),
    "Sheffield": ("Yorkshire", ["YM", "YN", "YO", "YP", "YR", "YS", "YT", "YU", "YV"]),
    "Beverley": ("Yorkshire", ["YW", "YX", "YY"])
}





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

#FIRST_LETTER = ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L", "M", "N", "O", "P", "R", "S", "V", "W", "Y"]
#REGIONS = ["Anglia", "Birmingham", "Cymru(Wales)", "Deeside", "Essex", "Forest & Fens", "Garden of England", "Hampshire & Dorset",
#          "No official mnemonic","London","Manchester", "North", "Oxford", "Preston", "Reading", "Scotland", "Severn Valley", 
#          "West of England", "Yorkshire"]
#OFFICE = [] 

#this function takes a string and strips out the spaces
def strip_spaces(s):
    s = s.replace(" ", "")
    return s

#this function returns true if the final 3 letters are valid, false otherwise
def validEnd(s):
    for char in s:
        if char in INVALID_LETTERS:
            return False
    #for loop ends
    return True

def find_Office(region):

    for i in range(len(List_Of_DLVA_Offices)):
        if List_Of_DLVA_Offices[i][0] == region:
            if user_licence_plate[1] in List_Of_DLVA_Offices[i][2]:
                return List_Of_DLVA_Offices[i][0]
    return "Invalid second letter that office does not exist."

user_licence_plate = "YY 72 ABc"
user_licence_plate = strip_spaces(user_licence_plate.upper())
#print(strip_spaces(user_licence_plate)) #debug to help us see if it worked

# we will test the licence plate in this order 1. First two letters 3. final 3 letters 3. Regions/Region checker using first 2 letters 4. second 2 nums
# each of these tests follow different rules, all three must PASS for a valid licence plate.

def length_check(input):
    if len(user_licence_plate) != REQ_CHARS:
        #wrong length
        print(f"The licence plate you entered was {len(user_licence_plate)} characters characters, it should be 7 spaces do not count")

    elif user_licence_plate[0] not in VALID_FIRST_LETTERS or user_licence_plate[1] in INVALID_LETTERS and INVALID_LETTERS or not user_licence_plate[1].isalpha:
        print("Fail, first two letters contain INVALID characters, numbers, or special characters e.g Q, I, Z, J, U, T, X")

    else:
        print("Valid. Correct length and first 2 letters.")

    #first = user_licence_plate[0]
    #second = user_licence_plate[1]
    # find where first is in the list of first letters
    #REGION = OFFICE[FIRST_LETTER.index(first)]
    #print(REGIONS)
    #print(REGIONS[FIRST_LETTER.index(user_licence_plate[0])])


# FINAL LETTER CHECKER

# slice out the last 3 chars in the licence plate
def final_letter_check(input):

    final_letters = input[-3:]

    if (validEnd(final_letters)):
        print("That is a valid final 3 letters for a licence plate")
    else:
        print("That is NOT a valid final 3 letters for the licence plate")

# REGION CHECKER

def office_checker(input):

    region = find_Office(input)

    if region == "Anglia" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:13]:
        print("Your office is Peterborough")
    elif region == "Anglia" and user_licence_plate[1] in VALID_SECOND_LETTERS[13:19]:
        print("Your office is Norwich.")
    elif region == "Anglia" and user_licence_plate[1] in VALID_SECOND_LETTERS[19:23]:
        print("Your office is Ipswich.")
    elif region == "Birmingham" and user_licence_plate[1] in VALID_SECOND_LETTERS:
        print("Your office is Birmingham")
    elif region == "Cymru" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:14]:
        print("Your office is Cardiff")
    elif region == "Cymru" and user_licence_plate[1] in VALID_SECOND_LETTERS[14:20]:
        print("Your office is Swansea")
    elif region == "Cymru" and user_licence_plate[1] in VALID_SECOND_LETTERS[20:23]:
        print("Your office is Bangor")
    elif region == "Deeside" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:10]:
        print("Your office is Chester")
    elif region == "Deeside" and user_licence_plate[1] in VALID_SECOND_LETTERS[10:23]:
        print("Your office is Shrewsbury")
    elif region == "Essex" and user_licence_plate[1] in VALID_SECOND_LETTERS:
        print("Your office is Chelmsford")
    elif region == "Forest & Fens" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:15]:
        print("Your office is Nottingham")
    elif region == "Forest & Fens" and user_licence_plate[1] in VALID_SECOND_LETTERS[15:23]:
        print("Your office is Lincoln")
    elif region == "Garden of England" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:14]:
        print("Your office is Maidstone")
    elif region == "Garden of England" and user_licence_plate[1] in VALID_SECOND_LETTERS[14:23]:
        print("Your office is Brighton")
    elif region == "Hampshire & Dorset" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:9]:
        print("Your office is Bournemouth")
    elif region == "Hampshire & Dorset" and user_licence_plate[1] in VALID_SECOND_LETTERS[9:20] and VALID_SECOND_LETTERS[21:23]:
        print("Your office is Portsmouth")
    elif region == "Hampshire & Dorset" and user_licence_plate[1] in VALID_SECOND_LETTERS[20]:
        print("Your office is Portsmouth (Isle of Wright)")
    elif region == "(No official mnemonic)" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:11]:
        print("Your office is Luton")
    elif region == "(No official mnemonic)" and user_licence_plate[1] in VALID_SECOND_LETTERS[11:23]:
        print("Your office is Northhampton")
    elif region == "London" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:9]:
        print("Your office is Wimbledon")
    elif region == "London" and user_licence_plate[1] in VALID_SECOND_LETTERS[9:18]:
        print("Your office is Stanmore")
    elif region == "London" and user_licence_plate[1] in VALID_SECOND_LETTERS[18:23]:
        print("Your office is Sidcup")
    elif region == "Manchester" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:23]:
        print("Your office is Manchester")
    elif region == "North" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:11]:
        print("Your office is Newcastle")
    elif region == "North" and user_licence_plate[1] in VALID_SECOND_LETTERS[11:23]:
        print("Your office is Stockton")
    elif region == "Oxford" and user_licence_plate[1] in VALID_SECOND_LETTERS:
        print("Your office is Oxford")
    elif region == "Preston" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:18]:
        print("Your office is Preston")
    elif region == "Preston" and user_licence_plate[1] in VALID_SECOND_LETTERS[18:23]:
        print("Your office is Carlisle")
    elif region == "Reading" and user_licence_plate[1] in VALID_SECOND_LETTERS:
        print("Your office is Reading")
    elif region == "Scotland" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:9]:
        print("Your office is Glasgow")
    elif region == "Scotland" and user_licence_plate[1] in VALID_SECOND_LETTERS[9:14]:
        print("Your office is Edinburgh")
    elif region == "Scotland" and user_licence_plate[1] in VALID_SECOND_LETTERS[14:18]:
        print("Your office is Dundee")
    elif region == "Scotland" and user_licence_plate[1] in VALID_SECOND_LETTERS[18:21]:
        print("Your office is Aberdeen")
    elif region == "Scotland" and user_licence_plate[1] in VALID_SECOND_LETTERS[21:23]:
        print("Your office is Inverness")
    elif region == "Severn Valley" and user_licence_plate[1] in VALID_SECOND_LETTERS:
        print("Your office is Worcester")
    elif region == "West of England" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:9]:
        print("Your office is Exeter")
    elif region == "West of England" and user_licence_plate[1] in VALID_SECOND_LETTERS[9:11]:
        print("Your office is Truro")
    elif region == "West of England" and user_licence_plate[1] in VALID_SECOND_LETTERS[11:23]:
        print("Your office is Bristol")
    elif region == "Yorkshire" and user_licence_plate[1] in VALID_SECOND_LETTERS[0:10]:
        print("Your office is Leeds")
    elif region == "Yorkshire" and user_licence_plate[1] in VALID_SECOND_LETTERS[10:19]:
        print("Your office is Sheffield")
    elif region == "Yorkshire" and user_licence_plate[1] in VALID_SECOND_LETTERS[19:23]:
        print("Your office is Beverly")
    else:
        print("Invalid office.")

# NUMBER CHECKER

def num_valid(s):
    num = ""
    for char in s:
        if char.isdigit():
            num += char
    try:
        int(num)
    except ValueError:
        num = 1
    if (2 <= int(num) <= 26) or (51 <= int(num) <= 76):
        return True
    else:
        return False

print(num_valid(user_licence_plate))

def region_checker(list):
    tag= list[:2]
        
    for cities,(region,tags) in GROUPED_MAP.items():
            if tag in tags:
                print(f"region in: {region} registered in: {cities}")
                break


# MENU / MAIN PROGRAM

quitChoice = False
quitChoice2 = False
choice = ""
choice2 = ""
answer = ""


def r_u_sure():
    print("Are you sure?")
    answer == input("Enter your answer (Y/N): ").upper()
    if answer == "Y":
        print("Quitting program...")
        return 'y'
    elif answer == "N":
        print("OK")
    else:
        print("Invalid Arguement.")


while quitChoice == False:

    print("-- MAIN MENU -- \n1. Check for valid licence plate \n2. Generate Licence plate \n3. Find age of car from licence plate \n4. Quit.")
    #quitChoice = True
    #get the users choice
    choice = input("Enter your choice: ")

    #when the user chooses the quit option, set quitChoice to True and this will exit the while loop
    if choice == "4":
        #r_u_sure()
        print("Are you sure?")
        answer = input("Enter y for yes ").upper()
        if answer == "Y":
            print("Quitting program...")
            quitChoice = True
        else:
            print("ok continue.")

    elif choice == "1":
        print("Option 1 has been chosen.")

    elif choice == "2":
        print("Option 2 has been chosen.")

    elif choice == "3":
        print("Option 3 has been chosen.")
        print(num_valid(user_licence_plate))
        break
        
    else:
        print("Invalid Arguement")
