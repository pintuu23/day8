alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(massage,letter_shifting):
    encrypted_text=""
    for letter in massage:
        position=alphabet.index(letter)
        new_position=position+letter_shifting
        new_letter=alphabet[new_position]
        encrypted_text+= new_letter
    print(f"Your encrypted message is {encrypted_text}")

def decrypt (massage,shifting):
    decrypt_text = ""
    for letter in massage:
        position = alphabet.index(letter)
        new_position = position-shifting
        new_letter=alphabet[new_position]
        decrypt_text+=new_letter
    print(f"Your message is {decrypt_text}")
if direction=="encode":
    encrypt(text, shift)
elif direction=="decode":
    decrypt(text, shift)