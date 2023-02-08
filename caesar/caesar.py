#!/usr/bin/python
# -*- coding: utf-8 -*-

# program to encrypt a string into cipher text using the caesar cipher, or decrypt a cipher text and provide the shift number

# To take input from the user

message = input('Enter message to encrypt: ').lower()
shift = int(input('Enter a the caesar rotation number: '))
alphabets = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    ]


# print("Message:" + message)
# print("Shift:",shift)
ciphertext = []
fullciphertext = []
def encrypt(message, shift):
	for i in message:

		if i in alphabets:

			print(i,alphabets.index(i))
			num =(alphabets.index(i) + shift) % 26
		
			ciphertext.append(num)
			print(ciphertext)

	
		else:
			
			print("ELSE")
			string = str(i)
			ciphertext.append(string)
			print(ciphertext)	
		
			

	for index_value in ciphertext:
		if type(index_value) == int:
			num=index_value
			letter=(alphabets[index_value])
			fullciphertext.append(letter)
			print(fullciphertext)
		else:
			fullciphertext.append(index_value)
			print(fullciphertext)
	


	print("".join(fullciphertext))

				
#the list above should actually be a string, but I don't know how to do that yet.





encrypt(message, shift)
#This function should output a cipher text given a plaintext

#given a ciphertext the decrypt function should be able to decrypt it  to plaintext.
#First with the key/shift value. Utltimately it should decrypt the message and provide the 
#return shift value as well.


