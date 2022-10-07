import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import Tk, Entry, Label, Button, messagebox

#Se crea la ventana, el titulo y el tamaño
vent1= Tk()
vent1.geometry("500x350")
vent1.configure(bg='gray')
vent1.title('Enviar Correo')

def Enviar():
    # Iniciamos los parámetros del script
    remitente = 'rene29alexander@gmail.com'
    destinatario = (input1.get())
    usuario = (input2.get())
 
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
 
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = usuario

    # Creamos el cuerpo del mensaje
    cuerpo = (input3.get())
    # Y lo agregamos al objeto mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
  
    # Ciframos la conexión
    sesion_smtp.starttls()
  
    # Iniciamos sesión en el servidor
    sesion_smtp.login('rene29alexander@gmail.com','usyobbtzawilkrpe')

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatario, texto)
 
    # Cerramos la conexión
    sesion_smtp.quit()
    texto="!!!Se envio el correo!!!"
    messagebox.showinfo(title="Enviar", message=str(texto))



#Se crean el boton y label
labl1=Label(vent1, bg = "gray",text="Enviar a:")
input1=Entry(vent1)
labl2=Label(vent1,bg = "gray", text="Nombre del usuario:")
input2=Entry(vent1)
labl3=Label(vent1, bg = "gray",text="Cuerpo del mensaje:")
input3=Entry(vent1)
btn1 = Button(vent1,text="Enviar",command=Enviar)

#Se muestran en pantalla y se pone su posicion
labl1.place(x=80, y=20)
input1.place(x=150, y=20)
labl2.place(x=30, y=60)
input2.place(x=150, y=60)
labl3.place(x=30, y=100)
input3.place(x=150, y=100, relwidth=0.6,relheight=0.4)
btn1.place(x=185, y=280)

vent1.mainloop()