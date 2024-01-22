from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(text, shift_amount, direction):
    output_text = ""

    if direction == "decode":
        shift_amount *= -1
    for char in text:
        try:
            i = alphabet.index(char)
            output_text += alphabet[(i+shift_amount) % len(alphabet)]
        except:
            output_text += char
        
    print("The output is:", output_text)

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cesar(text, shift, direction)

    if input("Press enter to restart, type \"quit\" to exit: ").lower() == "quit":
        break
    print()