from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Convertisseur de mot en mMORSE ")
label.pack()

fenetre.mainloop()

morse_lettre={
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    #Chiffre
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}


lettre_morse = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',

    #Chiffre
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
}



def morse1 (mot_lettre):
    mot_lettre=mot_lettre.upper()

    mot_morse=[]
    for i in mot_lettre:
        if i in morse_lettre :
            mot_morse.append(morse_lettre[i] + " ")


        if i == " ":
            mot_morse.append(" ")

        if i not in morse_lettre and i != " " :
            print("veuillez entrer un eent")



    mot_morse="".join(mot_morse)
    mot_morse=mot_morse[:-1]
    print(mot_morse)


#Test
def morse3(mot_morse):
    mot=[]
    mot_morse=mot_morse.split(' ')



    print(mot_morse)

    for i in mot_morse:
        if i in lettre_morse:
            mot.append(lettre_morse[i])

        if i == '':
            mot.append(" ")


    mot_str=''.join(mot)





    return mot_str