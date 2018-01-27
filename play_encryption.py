#try to make the encryption more complicated
message = "Hello Vickie!! ;-)"
alphabet="abcdefghijklmnopqrstuvwxyz"
upperCaseAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYX"
key=3
#take the position of the previous character and add it to the key
characters = list(message)
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
print(newMessage)
