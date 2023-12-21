code_morse= {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',}

def mot_morse(mot):
    mot=mot.upper()
    mot_li=[]
    for i in mot:
        mot_li.append(i)

    morse_li=[]
    for lettre in mot_li :
        if lettre in code_morse.keys():
            morse_li.append(code_morse[lettre] + " ")

        if lettre not in code_morse.keys() and lettre != " ":
            print("c'est pas dans le code morse")

        if lettre == " ":
            morse_li.append("  ")

        morse_str= ' '.join(morse_li)


    print(morse_str)

def morse_mot(morse):
    morse_li=morse.split()
    morse_mot=[]
    for morse in morse_li:
        if morse in code_morse.items():
            morse_mot.append(code_morse)

