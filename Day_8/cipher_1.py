
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    
    # At each character in our text, we want to find the corresponding index of the alphabet, and add the shift
    for char in plain_text:
        i = alphabet.index(char)
        encrypted_text += alphabet[(i+shift_amount) % len(alphabet)]

    print("The encoded text is:", encrypted_text)

# Reverses the operation
def decrypt(encrypted_text, shift_amount):
    plain_text = ""

    for char in encrypted_text:
        i = alphabet.index(char)
        plain_text += alphabet[(i-shift_amount) % len(alphabet)]

    print("The decoded text is:", plain_text)



#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("invalid entry")