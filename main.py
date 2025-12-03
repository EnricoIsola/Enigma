import string
import myModule

print(myModule.enigma)
alphabet = list(string.ascii_lowercase)
alphabet.append(" ")
nuovaLista = list()

myModule.loadNuovaLista(nuovaLista,alphabet)
print(myModule.encrypt_description())
myModule.printNuovaLista(nuovaLista)

testo_da_codificare = input("\nEnter the text to be encoded: \n")

print("\nBelow is the encrypted text...")

#Code
codifica_finale = myModule.code(nuovaLista,testo_da_codificare)
print(codifica_finale)

print(myModule.decrypt_description())
testo_decodificato = myModule.decode(codifica_finale,nuovaLista)
print("*** " + testo_decodificato +" ***")

print(myModule.farewell_message())




    
