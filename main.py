REGISTERED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

username = input("username:")
password = input("password:")

if username in REGISTERED_USERS and REGISTERED_USERS[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
    vyber = input("Enter a number btw. 1 and 3 to select: ")

    if not vyber.isdigit():
        print("Error: input is not a number. Exiting.")
    else:
        vyber = int(vyber)
        if vyber < 1 or vyber > 3:
            print("Error: invalid choice. Exiting.")
        else:
            text = TEXTS[vyber - 1]

            znaky_k_odstraneni = ".,!?;:-\n"
            text_bez_znaku = ""
            for znak in text:
                if znak in znaky_k_odstraneni:
                    text_bez_znaku += " "
                else:
                    text_bez_znaku += znak

            slova = text_bez_znaku.split()

            pocet_slov = 0
            zacinaji_velkym = 0
            vse_velkym = 0
            vse_malym = 0
            pocet_cisel = 0
            soucet_cisel = 0
            cetnost_delky = {}

            for slovo in slova:
                if slovo == "":
                    continue
                pocet_slov += 1

                delka = len(slovo)
                if delka in cetnost_delky:
                    cetnost_delky[delka] += 1
                else:
                    cetnost_delky[delka] = 1

                if slovo.isdigit():
                    pocet_cisel += 1
                    soucet_cisel += int(slovo)
                elif slovo.isalpha():
                    if slovo.istitle():
                        zacinaji_velkym += 1
                    if slovo.isupper():
                        vse_velkym += 1
                    if slovo.islower():
                        vse_malym += 1

            print("----------------------------------------")
            print(f"There are {pocet_slov} words in the selected text.")
            print(f"There are {zacinaji_velkym} titlecase words.")
            print(f"There are {vse_velkym} uppercase words.")
            print(f"There are {vse_malym} lowercase words.")
            print(f"There are {pocet_cisel} numeric strings.")
            print(f"The sum of all the numbers {soucet_cisel}")
            print("----------------------------------------")
            print("LEN|  OCCURENCES  |NR.")
            print("----------------------------------------")

            delky = list(cetnost_delky.keys())
            i = 0
            while i < len(delky):
                j = i + 1
                while j < len(delky):
                    if delky[j] < delky[i]:
                        delky[i], delky[j] = delky[j], delky[i]
                    j += 1
                i += 1

            for d in delky:
                pocet = cetnost_delky[d]
                stars = "*" * pocet
                print(f"{d:3}|{stars:<18}|{pocet}")

else:
    print("unregistered user, terminating the program..")