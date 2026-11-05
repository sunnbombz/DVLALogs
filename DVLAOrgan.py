# global CONSTANTS
SEPFEB_ADD_ON = 50
REQ_CHARS = 7
INVALID_LETTERS = 'QIZ'
VALID_FIRST_LETTERS = 'ABCDEFGHKLNMOPRSVWY'
INVALID_FIRST_LETTERS = "QIZJTUX"
VALID_SECOND_LETTERS = 'ABCDEFGHJKLMNOPRSTUVWXY'

# ARRAYS/LISTS
VALID_NUMS = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76"]
VALID_SEC_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y" ]



VALID_FIR_LETTERS = ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN", 
                     "AO", "AP", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", 
                     "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY", "CA", "CB", "CC", 
                     "CD", "CE", "CF", "CG", "CH", "CJ", "CK", "CL", "CM", "CN", "CO", "CP", "CR", "CS", "CT", "CU", "CV", "DA",
                     "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DJ", "DK", "DL", "DM", "DN", "DO", "DP", "DR", "DS", "DT", "DU", 
                     "DV", "DW", "DX", "DY", "EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EJ", "EK", "EL", "EM", "EN", "EO", 
                     "EP", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY", "FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FJ", 
                     "FK", "FL", "FM", "FN", "FP", "FR", "FS", "FT", "FV", "FW", "FX", "FY", "GA", "GB", "GC", "GD", "GE", "GF", 
                     "GG", "GH", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY", "HA", 
                     "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HJ","HK", "HL", "HM", "HN", "HO", "HP", "HR", "HS", "HT", "HU", 
                     "HV", "HW", "HX", "HY", "KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KJ", "KK", "KL","KM", "KN", "KO", 
                     "KP", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY","LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LJ",
                     "LK", "LL", "LM", "LN", "LO", "LP", "LR", "LS", "LT","LU", "LV", "LW", "LX", "LY","MA", "MB", "MC", "MD", 
                     "ME", "MF", "MG", "MH", "MJ", "MK", "ML", "MM", "MN", "MP", "MT", "MU", "MV", "MW", "MX", "MY","MS", "NA", 
                     "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NJ", "NK", "NL", "NM", "NN", "NO","NP", "NR", "NS", "NT", "NU", 
                     "NV", "NW", "NX", "NY", "OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OJ", "OK", "OL", "OM", "ON", "OO", 
                     "OP", "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY","PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PJ", 
                     "PK", "PL", "PM", "PN", "PO", "PP", "PR", "PS", "PT", "PU", "PV", "PW", "PX", "PY","RA", "RB", "RC", "RD", 
                     "RE", "RF", "RG", "RH", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RR", "RS", "RT", "RU", "RV", "RW", "RX", 
                     "RY","SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ", "SK", "SL", "SM", "SN", "SO", "SP", "SR", "SS", 
                     "ST", "SU", "SV", "SW", "SX", "SY", "VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VJ", "VK", "VL", "VM", 
                     "VN", "VO", "VP", "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY", "WA", "WB", "WC", "WD", "WE", "WF", "WG", 
                     "WH", "WJ", "WK", "WL", "WM", "WN", "WO", "WP", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY", "YA", "YB", 
                     "YC", "YD", "YE", "YF", "YG", "YH", "YJ", "YK", "YL", "YM", "YN", "YO", "YP", "YR", "YS", "YT", "YU", "YV",
                     "YW", "YX", "YY"  ]


VALID_THREES_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X","Z"]
VALID_SECONDS_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X"]
VALID_LETTERSS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y"]





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

# FUNCTIONS

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

# checks length
def length_check(input):
    if len(input) != REQ_CHARS:
        #wrong length
        length_error = f"The licence plate you entered was {len(input)} characters characters, it should be 7 spaces do not count"
        return length_error

    elif input[0] not in VALID_FIRST_LETTERS or input[1] in INVALID_LETTERS and INVALID_LETTERS or not input[1].isalpha:
        letter_error = "Fail, first two letters contain INVALID characters, numbers, or special characters e.g Q, I, Z, J, U, T, X"
        return letter_error

    else:
        print("Valid. Correct length and first 2 letters.")

# slice out the last 3 chars in the licence plate
def final_letter_check(input):

    final_letters = input[-3:]

    if (validEnd(final_letters)):
        print("That is a valid final 3 letters for a licence plate")
    else:
        print("That is NOT a valid final 3 letters for the licence plate")

#checks if second nums are valid
def num_valid(s):
    num = ""
    for char in s:
        if char.isdigit():
            num += char
        else:
            return False

    if (2 <= int(num) <= 26):
        print(f"Your car was registered in 20{num}.")
        return True
    
    elif  (51 <= int(num) <= 76):
        year = int(num) - 50
        print(f"Your car was registered in ...")
        return True
    
    else:
        return False

# checks the region
def region_checker(list):
    tag= list[:2]
        
    for cities,(region,tags) in GROUPED_MAP.items():
            if tag in tags:
                print(f"region in: {region} registered in: {cities}")
                break

# r u sure program
def r_u_sure():
    print("Are you sure?")
    answer = input("Enter your answer (Y/N): ").upper()
    if answer == "Y":
        print("Quitting program...")
        return 'y'
    elif answer == "N":
        print("OK")
    else:
        print("Invalid Arguement.")

# TO GENERATE 
def generate_plate():
    import random
    plate = ""

    last_three = random.sample(VALID_THREES_LETTERS, 3)
    last_three ="".join(last_three)
    first_one = random.choice(VALID_LETTERSS)
    second_one = random.choice(VALID_SECOND_LETTERS)
    second_nums = random.choice(VALID_NUMS)

    plate = first_one + second_one + second_nums + last_three

    return plate

# MENU / MAIN PROGRAM

quitChoice = False
choice = ""
choice2 = ""
answer = ""


while quitChoice == False:

    print("-- MAIN MENU -- \n1. Check for valid licence plate \n2. Generate Licence plate \n3. Find age of car from licence plate \n4. Quit.")
    #quitChoice = True
    #get the users choice
    choice = input("Enter your choice: ")
    
    #when the user chooses the quit option, set quitChoice to True and this will exit the while loop
    if choice == "4":
        print("Are you sure?")
        answer = input("Enter Y for yes: ").upper()
        if answer == "Y":
            print("Quitting program...")
            quitChoice = True
        else:
            print("Ok, continue.")

    elif choice == "1":
        print("Option 1 - Check for valid licence plate - has been chosen.")
        input_user_plate = input("Enter Licence Plate: ")
        input_user_plate= strip_spaces(input_user_plate.upper())

        if len(input_user_plate) != REQ_CHARS:
            #wrong length
            length_error = f"The licence plate you entered was {len(input)} characters characters, it should be 7 spaces do not count"
            print(length_error)


        elif input_user_plate[0] not in VALID_FIRST_LETTERS or input_user_plate[1] in INVALID_LETTERS and INVALID_LETTERS or not input_user_plate[1].isalpha:
            letter_error = "Fail, first two letters contain INVALID characters, numbers, or special characters e.g Q, I, Z, J, U, T, X"
            print(letter_error)

        else:
            print("Valid. Correct length and first 2 letters.")


        break

    elif choice == "2":
        print("Option 2 has been chosen - Generate a Random Licence Plate")
        print(f"Generated licence plate: {generate_plate()}")
        


    elif choice == "3":
        print("Option 3 has been chosen - Find age of car from plate.")
        input_user_plate = input("Enter Licence Plate: ")
        input_user_plate= strip_spaces(input_user_plate.upper())
        print(length_check(input_user_plate))
        print(num_valid(input_user_plate))

        r_u_sure()
          
    else:
        print("Invalid Choice , please retry.")
