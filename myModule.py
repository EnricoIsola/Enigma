import random

def loadNuovaLista(nuovaLista,alphabet):
    for l in range(len(alphabet)):
        nuovaLista.append(random.sample(alphabet,27))


def printNuovaLista(nuovaLista):
    for elem in nuovaLista:
        print(elem)

def code(nuovaLista,testo_da_codificare):
    coord = list()
    testo_codificato =list()

    for i in range(len(testo_da_codificare)):
        for j in range(27):
            for z in range(27):
                if testo_da_codificare[i] == nuovaLista[j][z]:
                    if j <10: 
                        x = "0" + str(j)
                    else:
                        x = str(j)
                    if z <10:  
                        y = "0" + str(z)
                    else:
                        y = str(z)
                    
                    coord.append([x+y])
        testo_codificato.append(random.choice(random.sample(coord,len(coord))))
        coord.clear()
    return "".join(x for sub in testo_codificato for x in sub)



def decode(codifica_finale,nuovaLista):
    gruppi = [codifica_finale[i:i+4] for i in range(0, len(codifica_finale), 4)]
    testo_decodificato=""
    for gruppo in gruppi:
        x = int(gruppo[:2])  # prime due lettere
        y = int(gruppo[2:]) # ultime due lettere
        testo_decodificato += nuovaLista[x][y]
    return testo_decodificato



def encrypt_description():
    return """
    The program creates a randomly ordered two-dimensional matrix based on the
    letters of the English alphabet (plus a space). The operator types a text
    that is encrypted through the matrix itself. Each letter is converted into
    two numerical coordinates that correspond to the position of the letter
    within the matrix. (Naturally, a letter may appear multiple times in the
    matrix, and its coordinates are extracted randomly.)
    """

def decrypt_description():
    return """
    Now the process proceeds in reverse, from the encrypted string that is passed
    to the decoding matrix to retrieve the original text.
    """
    pass

def farewell_message():
    return """
    .............See you next time.
    """
    pass

enigma = """
  _____ _   _ ___ ____ __  __    _    
 | ____| \ | |_ _/ ___|  \/  |  / \   
 |  _| |  \| || | |  _| |\/| | / _ \  
 | |___| |\  || | |_| | |  | |/ ___ \ 
 |_____|_| \_|___\____|_|  |_/_/   \_\
                                      """

