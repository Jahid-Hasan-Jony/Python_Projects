from tkinter import*

def file():
    a=username.get()
    b=password.get()
    file=open("info.txt","w")
    file.write(a+"\n")
    file.write(b)
    file.close()

def login():
    form=Tk()
    form.geometry("900x600")
    global username
    global password
    username=StringVar()
    password=StringVar()
    form.title("Log in Page")
    Label(form,text="Log In",bg="skyblue",width="900",font=("Cooper Black",30,"bold")).pack()
    Label(form,text="User Name").pack()
    Entry(form,textvariable=username).pack()
    Label(form,text="Password").pack()
    Entry(form,textvariable=password).pack()
    Label(form).pack()
    
    Button(form,text="Login",command=file).pack()
login()

        