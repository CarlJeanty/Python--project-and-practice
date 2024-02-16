from art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction== "decode":
            shift_amount*=-1
    for letter in start_text:
        if letter not in alphabet:
             end_text+= str(letter)
             continue
        position = alphabet.index(letter)
        new_position =position +shift_amount
        if new_position > 26:
             new_position-=26
        end_text+=alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

keep_playing = True
while keep_playing :
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text,cipher_direction=direction,shift_amount=shift)
    ask_player = input("Would you like to keep playing? Yes or No").lower()
    if ask_player == "no":
         keep_playing == False
         print(" Au revoir")



#def encrypt(plain_text, shift_amount):
   # cipher_text =""
 #   for letter in text:
    #    get_i = alphabet.index(letter)
      #  new_i = get_i+shift
      #  if new_i > 26:
      #      new_i= new_i-26
      #  cipher_text+=alphabet[new_i]
   # print(f"The encoded text is {cipher_text}")
   # return cipher_text

#def decrypt(code, shift_amount):
   # rtext =""
   # for i in code:
      #  get_i = alphabet.index(i)
      #  new_i = get_i-shift
     #  rtext+=alphabet[new_i]
   # print(f"The decoded text is {rtext}")



#if direction == "encode":
 #   encrypt(plain_text= text,shift_amount=shift)
#elif direction =="decode":
    #decrypt(code= text,shift_amount=shift)


#print(art.logo)
caesar(start_text=text,cipher_direction=direction,shift_amount=shift)