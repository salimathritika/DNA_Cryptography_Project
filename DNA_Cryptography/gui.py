from tkinter import *
from PIL import Image, ImageTk
import random
from dna_encrypt import dna_encrypt_with_key
from dna_decrypt import dna_decrypt_with_key
from key_generation import generate_dynamic_key
from dna_encoding import encode_to_dna, encoding_table,decode_from_dna, reverse_table


#Generation of a symmetric key
key=generate_dynamic_key(random.randint(4,100))

#Generate the number of rounds of encryption and decryption
round=random.randint(1,50)

def encrypt_text():
    #Encrypts the data
    pt=Encryption_field.get()
    if pt:
        Encrypted_field.delete(0, END)
        global flag
        flag = 0
        if len(pt) % 2 == 0:
            pt = pt + 'x'
            flag = 1
        dna_seq = encode_to_dna(pt, encoding_table)
        enc = dna_seq
        enc = dna_encrypt_with_key(enc, key, round)
        Encrypted_field.insert(10,enc)

def decrypt_text():
    #Decrypts the data 
    ct=Decryption_field.get()
    if ct:
        Decrypted_field.delete(0, END)
        dec = dna_decrypt_with_key(ct, key, round)
        dec = decode_from_dna(dec, reverse_table)
        if flag == 1:
            dec = dec[:len(dec) - 1]
        Decrypted_field.insert(10,dec)

def clear_enc():
    #Clears the textboxes/fields used in decryption
    Encrypted_field.delete(0,END)
    Encryption_field.delete(0,END)

def clear_dec():
    #Clears the textboxes/fields used in decryption
    Decrypted_field.delete(0,END)
    Decryption_field.delete(0,END)


if __name__=="__main__":
    root=Tk()
    root.title("DNA Cryptography")
    root.geometry('500x300')

    #Putting an image as background
    image=Image.open("background.png")
    resize_image = image.resize((500, 300))
    bg= ImageTk.PhotoImage(resize_image)
    label5 = Label( root, image = bg) 
    label5.place(x = 0, y = 0)

    #Defining all the labels, text boxes and buttons to be used
    label1 = Label(root, text = "Enter the text to be encrypted: ", fg = 'white', bg='black',font=("Arial", 11, "bold"))
    label2 = Label(root, text = "Encrypted text: ", fg = 'white', bg = 'black',font=("Arial", 11, "bold")) 
    label3 = Label(root, text = "Enter the text to be decrypted:", fg = 'white', bg = 'black',font=("Arial", 11, "bold")) 
    label4 = Label(root, text = "Decrypted text: ", fg = 'white', bg = 'black',font=("Arial", 11, "bold")) 
    button1 = Button(root, text = "Encrypt", bg = "white",  fg = "black",font=("Arial", 11, "bold"), command = encrypt_text) 
    button3=Button(root,text="Clear",bg = "white",  fg = "black",font=("Arial", 11, "bold"), command = clear_enc)
    button2 = Button(root, text = "Decrypt", bg = "white",  fg = "black",font=("Arial", 11, "bold"), command = decrypt_text)
    button4=Button(root,text="Clear",bg = "white",  fg = "black",font=("Arial", 11, "bold"), command = clear_dec)
    Encryption_field = Entry(root)  
    Encrypted_field=Entry(root)
    Decryption_field = Entry(root)  
    Decrypted_field = Entry(root)
    
    #Using the grid method to align all the elements on the window
    label1.grid(row = 5, column = 0,ipady="10")  
    Encryption_field.grid(row=5,column=1,ipadx="100")
    label2.grid(row = 10, column = 0,ipady="10")  
    Encrypted_field.grid(row=10,column=1,ipadx="100")
    button1.grid(row=15,column=0,ipady="10")
    button3.grid(row=15,column=1,ipady="10")
    label3.grid(row = 30, column = 0,ipady="10") 
    Decryption_field.grid(row=30,column=1,ipadx="100")
    label4.grid(row = 35, column = 0,ipady="10")
    Decrypted_field.grid(row=35,column=1,ipadx="100")
    button2.grid(row=40,column=0)
    button4.grid(row=40,column=1)


    root.mainloop()