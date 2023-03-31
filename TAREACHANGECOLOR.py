from tkinter import*

root = Tk()
root.title("MENU")
root.grid()
root.geometry('200x150')

datored=StringVar()
datogreen=StringVar()
datoblue=StringVar()
tamañored=StringVar()
tamañogreen=StringVar()
tamañoblue=StringVar()
x=BooleanVar()
y=BooleanVar()

def CambiarColor():
    global tamañored,tamañogreen, tamañoblue,x,y,titulo,tituloR,tituloG,tituloB
    tamañored=len(datored.get())
    tamañogreen=len(datogreen.get())
    tamañoblue=len(datoblue.get())
    x=True
    print(tamañored,tamañogreen, tamañoblue)
    if tamañored>=3 or tamañogreen>=3 or tamañoblue>=3 or tamañored<=1 or tamañogreen<=1 or tamañoblue<=1:
        y=False
        print("****INGRESE SOLO DOS CARACTERES POR COLOR*****")
    if (tamañored ==2 and tamañogreen==2 and tamañoblue==2)and x==True:
        y=True
    if y==True:
        root.config(bg="#"+datored.get()+datogreen.get()+datoblue.get())
        titulo=Label(root,text="CAMBIADOR DE COLOR",font=("Roboto",10),bg="#"+datored.get()+datogreen.get()+datoblue.get()).grid(row=1,column=0,columnspan=3,rowspan=3)
        tituloR=Label(root,text="ROJO",font=("Roboto",10),bg="#"+datored.get()+datogreen.get()+datoblue.get()).grid(row=4,column=1)
        tituloG=Label(root,text="GREEN",font=("Roboto",10),bg="#"+datored.get()+datogreen.get()+datoblue.get()).grid(row=5,column=1)
        tituloB=Label(root,text="BLUE",font=("Roboto",10),bg="#"+datored.get()+datogreen.get()+datoblue.get()).grid(row=6,column=1)
        print(datored.get() , datogreen.get() , datoblue.get())
        

titulo=Label(root,text="CAMBIADOR DE COLOR",font=("Roboto",10)).grid(row=1,column=0,columnspan=3,rowspan=3)
tituloR=Label(root,text="ROJO",font=("Roboto",10)).grid(row=4,column=1)
tituloG=Label(root,text="GREEN",font=("Roboto",10)).grid(row=5,column=1)
tituloB=Label(root,text="BLUE",font=("Roboto",10)).grid(row=6,column=1)

R = Entry(root, textvariable=datored).grid(row=4,column=2)
G = Entry(root, textvariable=datogreen).grid(row=5,column=2)
B = Entry(root, textvariable=datoblue).grid(row=6,column=2)

botonentrada=Button(root, text="COMBINAR COLOR", bg="#00ffff",font=("Roboto", 8, "bold"),fg="Black",width=15,height=1,command=CambiarColor)
botonentrada.grid(row=8,rowspan=3,column=0,columnspan=3)

root.mainloop()