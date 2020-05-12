from tkinter import *
import time

def test():
    print("get: "+ password.set(password.get()+"new key") )
    return None
    
root = Tk()

root.title("cMaster")
root.geometry("400x200")
root.configure(bg="#000")

Label(root,text="Password  :",fg="#fff",bg="#000").place(x=10,y=10)
Label(root,text="Your KEY  :",fg="#fff",bg="#000").place(x=10,y=40)
Label(root,text="Encrypted :",fg="#fff",bg="#000").place(x=10,y=70)

password = StringVar()
key = StringVar()
encrypted = StringVar()

Entry(root, textvariable=password, width=15).place(x=200,y=10)
Entry(root, textvariable=key, width=15).place(x=200,y=40)
Entry(root, textvariable=encrypted, width=15).place(x=200,y=70)

Button(root, text="Convert",fg="#000",bg="#eee", relief='flat',width=39, command =test).place(x=10,y=100)

root.mainloop()

"""
root.iconify() #minimiza la ventana
root.deiconify() #maximiza la ventana
time.sleep(3) #hace una pausade 3s
label= Label(root,text="Hi")  # Create a text label
label= Label(root,text="Hi")  # Create a text label
submit=Button(root, text="Submit",command=quikly) #boton para quikly
print("This is a print") #print en ventana
Button(root, text="Exit",fg="#00f", command =root.quit).grid(row=0,column=0) #posicionamiento de objetos
Button(root, text="Exit",fg="#00f", command =root.quit).place(x=0,y=0) 
"""