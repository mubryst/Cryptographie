
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
    return plaintext


print()
print('*** PROGRAMME DE CHIFFREMENT CESAR ***')
print()

print('Voulez vous chiffrer ou déchiffrer')
user_input = input('c/d: ')
print()

if user_input == 'c' :
    print('MODE DE CHIFFREMENT SELECTIONNE')
    print()
    key = int(input('Entrer la clé (1 à 26): '))
    text = input('Entrer le texte à chiffrer: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd' :
    print('MODE DE DECHIFFREMENT SELECTIONNE')
    print()
    key = int(input('Entrer la clé (1 à 26): '))
    text = input('Entrer le texte à déchiffrer: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')