# A Program that will demostrate loops, if else , lists in python.
# This script allows to encrypt and decrypt your messages and have fun with friends

# Feel Free to Fork and lets make it more strong encoder!

alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type Message:\n")
shift = int(input("Type the shift number:\n"))

def ceaser(text,shift,direction):
  cipher_text = ""
  text_origin_position = 0
  for char in text:
    if char not in alphabet: 
      cipher_text += char
    else:
      text_origin_position = alphabet.index(char)
      if direction == "encode":
        cipher_text+=alphabet[text_origin_position+shift]
      elif direction == "decode":
        cipher_text+=alphabet[text_origin_position-shift]
  if direction == "decode":
    secret = input("Enter Secret Code to Decode now!")
    if secret == "!inlove!": # the Secret Your Friend and you know, becuase hacker can try all shift numbers to get desired message
      print(cipher_text)
    else:
      print("#############--------YOU ARE A HACKER ----------###############")
  elif direction == "encode":
    print(cipher_text)

  
  
  

ceaser(text,shift%26,direction)


