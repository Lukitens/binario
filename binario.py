import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta = tkinter.Label(ventana, text = "Pone tu numero binario", bg="blue")
entrada = tkinter.Entry(ventana, font= "helvetica")
resultado = tkinter.Label(ventana, font=("arial"))

def Entradafuncion():
    texto = entrada.get()
    lista_inicial = []
    lista_final = []
    contador = 0

    for n in str(texto):
        lista_inicial.append(int(n))

    lista_inicial.reverse()

    for a in lista_inicial:
        if a == 1:
            c = a * (2 ** contador)
            lista_final.append(c)
        contador += 1

    resultado["text"] = sum(lista_final) #Mostrar otra variable

def Saludo(nombre):
    print("Hola", nombre)
boton = tkinter.Button(ventana, text= "Conversión de binario a decimal", padx="50", pady="20",
                       command= Entradafuncion)

etiqueta.pack(fill=tkinter.X)
entrada.pack()
boton.pack()
resultado.pack()
ventana.mainloop()