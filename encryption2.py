from guizero import App, Text, TextBox, PushButton, Slider, info, Combo


alphabet="abcdefghijklmnopqrstuvwxyz"
upperCaseAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYX"

def encrypt_message():
    message = unencrypted_message.value
    key = int(encryption_key.value)
    newMessage = ""
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) %26
            newCharacter = alphabet[newPosition]
        elif character in upperCaseAlphabet:
            position = upperCaseAlphabet.find(character)
            newPosition = (position + key) %26
            newCharacter = upperCaseAlphabet[newPosition]
        else:
            newCharacter = character
        newMessage += newCharacter
    output.value = newMessage

def decrypt_message():
    message = unencrypted_message.value
    key = int(encryption_key.value)
    newMessage = ""
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position - key) %26
            newCharacter = alphabet[newPosition]
        elif character in upperCaseAlphabet:
            position = upperCaseAlphabet.find(character)
            newPosition = (position - key) %26
            newCharacter = upperCaseAlphabet[newPosition]
        else:
            newCharacter = character
        newMessage += newCharacter
    output.value = newMessage


app = App(title="Secret messages", width="600", height="200", layout ="grid")
message_description = Text(app, text="Enter your message", grid=[0,0], align="left")
unencrypted_message = TextBox(app, width="50", grid=[0,1,2,1], align="left")
encryption_key = Combo(app, options=["1", "2", "3", "4", "5"], grid=[1,2], align="left")
key_description = Text(app, "Choose your key", grid=[0,2])

output = Text(app, "view the result here", grid=[0,3])

send_message = PushButton(app, command=encrypt_message, text="Encrypt", grid=[0,4], align="left")
translate_message = PushButton(app, command=decrypt_message, text="Decrypt", grid=[1,4], align="left")


