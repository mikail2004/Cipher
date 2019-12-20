import eel

eel.init('don')
print("dally llama")


@eel.expose
def to_morse_code(text):
    characters = { 'A':'.-', 'B':'-...', 
                   'C':'-.-.', 'D':'-..', 'E':'.', 
                   'F':'..-.', 'G':'--.', 'H':'....', 
                   'I':'..', 'J':'.---', 'K':'-.-', 
                   'L':'.-..', 'M':'--', 'N':'-.', 
                   'O':'---', 'P':'.--.', 'Q':'--.-', 
                   'R':'.-.', 'S':'...', 'T':'-', 
                   'U':'..-', 'V':'...-', 'W':'.--', 
                   'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                   '1':'.----', '2':'..---', '3':'...--', 
                   '4':'....-', '5':'.....', '6':'-....', 
                   '7':'--...', '8':'---..', '9':'----.', 
                   '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                   '?':'..--..', '/':'-..-.', '-':'-....-', 
                   '(':'-.--.',')':'-.--.-', ' ' : ' ', '!' : '-.-.--'}
    morse_code = ''
    
    for x in text:
        morse_code += characters[x.upper()]

    encrypted = morse_code
    
    print(encrypted)
    
    eel.printGreeting(encrypted)
    
    return morse_code

@eel.expose
def to_ascii_code(text):
    characters = { 'A':'65', 'B':'66', 
                   'C':'67', 'D':'68', 'E':'69', 
                   'F':'70', 'G':'71', 'H':'72', 
                   'I':'73', 'J':'74', 'K':'75', 
                   'L':'76', 'M':'77', 'N':'78', 
                   'O':'79', 'P':'80', 'Q':'81', 
                   'R':'82', 'S':'83', 'T':'84', 
                   'U':'85', 'V':'86', 'W':'87', 
                   'X':'88', 'Y':'89', 'Z':'90', 
                   '1':'049', '2':'050', '3':'051', 
                   '4':'052', '5':'053', '6':'054', 
                   '7':'055', '8':'056', '9':'057', 
                   '0':'048', ', ':'044', '.':'046', 
                   '?':'063', '/':'047', '-':'045', 
                   '(':'040',')':'041', ' ' : ' ', '!' : '033'}
    ascii_code = ''
    
    for x in text:
        ascii_code += characters[x.upper()]

    encrypted2 = ascii_code
    
    print(encrypted2)
    
    eel.printRemarks(encrypted2)
    
    return ascii_code

eel.start('land.html', size=(1000,500))


