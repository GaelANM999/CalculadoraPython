import tkinter as tk
import math

class calculator:

    # Método para centrar la pantalla
    @staticmethod
    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')

    # Calculadora
    def __init__(self):
        # Inicializa la variable de expresión
        self.expresion = ""

        self.root = tk.Tk()
        self.root.title("Calculator")

        windowWidth = 350
        windowHeight = 380

        self.centerWindow(self.root, windowWidth , windowHeight)

        self.textbox = tk.Text(self.root,height=1.25, font=('Arial', 32))
        self.textbox.pack(side='top', fill='both', padx=10, pady=(10))

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight= 1)
        self.buttonFrame.columnconfigure(1, weight= 1)
        self.buttonFrame.columnconfigure(2, weight= 1)
        self.buttonFrame.columnconfigure(3, weight= 1)

        self.btnPorcentaje = tk.Button(self.buttonFrame, text='(',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("("))
        self.btnPorcentaje.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btnCE = tk.Button(self.buttonFrame, text='CE',  font=("Arial", 18), command=self.clearEntry ) #ClearEntry
        self.btnCE.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btnC = tk.Button(self.buttonFrame, text='C',  font=("Arial", 18) ,command=self.Clear)
        self.btnC.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.btnB = tk.Button(self.buttonFrame, text='B',  font=("Arial", 18) ,command=self.borrar) #Backspace
        self.btnB.grid(row=0, column=3, sticky=tk.W+tk.E)

        self.btnFraccion = tk.Button(self.buttonFrame, text='1/x',  font=("Arial", 18), command=self.fraccion) #fraccion de 1/ el numero
        self.btnFraccion.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.btnCuadrado = tk.Button(self.buttonFrame, text='x²',  font=("Arial", 18), command=self.numCuadrado) #^2
        self.btnCuadrado.grid(row=1, column=1, sticky=tk.W+tk.E)

        self.btnRaiz = tk.Button(self.buttonFrame, text='√',  font=("Arial", 18) , command=self.raiz)
        self.btnRaiz.grid(row=1, column=2, sticky=tk.W+tk.E)

        self.btnDivision = tk.Button(self.buttonFrame, text='÷',  font=("Arial", 18) ,command = lambda: self.agregar_a_expresion('/'))
        self.btnDivision.grid(row=1, column=3, sticky=tk.W+tk.E)

        self.btn7 = tk.Button(self.buttonFrame, text='7',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("7"))
        self.btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.btn8 = tk.Button(self.buttonFrame, text='8',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("8"))
        self.btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.btn9 = tk.Button(self.buttonFrame, text='9',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("9"))
        self.btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

        self.btnX = tk.Button(self.buttonFrame, text='x',  font=("Arial", 18) ,command=lambda : self.agregar_a_expresion("*"))
        self.btnX.grid(row=2, column=3, sticky=tk.W+tk.E)

        self.btn4 = tk.Button(self.buttonFrame, text='4',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("4"))
        self.btn4.grid(row=3, column=0, sticky=tk.W+tk.E)

        self.btn5 = tk.Button(self.buttonFrame, text='5',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("5"))
        self.btn5.grid(row=3, column=1, sticky=tk.W+tk.E)

        self.btn6 = tk.Button(self.buttonFrame, text='6',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("6"))
        self.btn6.grid(row=3, column=2, sticky=tk.W+tk.E)

        self.btnResta = tk.Button(self.buttonFrame, text='-',  font=("Arial", 18) ,command= lambda: self.agregar_a_expresion("-"))
        self.btnResta.grid(row=3, column=3, sticky=tk.W+tk.E)

        self.btn1 = tk.Button(self.buttonFrame, text='1',  font=("Arial", 18), command=lambda: self.agregar_a_expresion("1"))
        self.btn1.grid(row=4, column=0, sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.buttonFrame, text='2',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("2"))
        self.btn2.grid(row=4, column=1, sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.buttonFrame, text='3',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("3"))
        self.btn3.grid(row=4, column=2, sticky=tk.W+tk.E)

        self.btnSuma = tk.Button(self.buttonFrame, text='+',  font=("Arial", 18) ,command=lambda: self.agregar_a_expresion("+")) 
        self.btnSuma.grid(row=4, column=3, sticky=tk.W+tk.E)

        self.btnNegar = tk.Button(self.buttonFrame, text=')',  font=("Arial", 18) ,command= lambda :self.agregar_a_expresion(")")) 
        self.btnNegar.grid(row=5, column=0, sticky=tk.W+tk.E)

        self.btn0 = tk.Button(self.buttonFrame, text='0',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("0"))
        self.btn0.grid(row=5, column=1, sticky=tk.W+tk.E)

        self.btnPunto = tk.Button(self.buttonFrame, text='.',  font=("Arial", 18) , command=lambda: self.agregar_a_expresion("."))
        self.btnPunto.grid(row=5, column=2, sticky=tk.W+tk.E)

        self.btnIgual = tk.Button(self.buttonFrame, text='=',  font=("Arial", 18) ,command=self.mostrarResultado)
        self.btnIgual.grid(row=5, column=3, sticky=tk.W+tk.E)

        self.buttonFrame.pack(fill='x', padx=10, pady=10)

        self.root.mainloop()

    def agregar_a_expresion(self, valor):
        self.expresion += str(valor)
        self.textbox.delete("1.0", "end")
        self.textbox.insert("end", self.expresion)
        
    def numCuadrado(self):
        try:
            resultado = eval(self.expresion)
            self.textbox.delete("1.0", "end")
            self.expresion = str(resultado ** 2)
            self.textbox.insert("end", self.expresion)
            
        except Exception:
            self.textbox.delete("1.0", "end")
            self.textbox.insert("end", "Error")
            self.expresion = ""
            
    def borrar(self):
        self.textbox.delete("end-2c", "end-1c")
        self.expresion = self.textbox.get("1.0", "end-1c")
        
    def mostrarResultado(self):
        try:
            resultado = eval(self.expresion)
            self.textbox.delete("1.0", "end")
            self.textbox.insert("end", str(resultado))
            self.expresion = str(resultado)
        except Exception:
            self.textbox.delete("1.0", "end")
            self.textbox.insert("end", "Error")
            self.expresion = ""
            
    def fraccion(self):
        try:
            resultado = eval(self.expresion)
            self.textbox.delete("1.0", "end")
            self.expresion = str(1/resultado)
            self.textbox.insert("end", self.expresion)
            
        except Exception:
            self.textbox.delete("1.0", "end")
            self.textbox.insert("end", "Error")
            self.expresion = ""
            
    def raiz(self):
        try:
            resultado = eval(self.expresion)
            self.textbox.delete("1.0", "end")
            self.expresion = str(math.sqrt(resultado))
            self.textbox.insert("end", self.expresion)
            
        except Exception:
            self.textbox.delete("1.0", "end")
            self.textbox.insert("end", "Error")
            self.expresion = ""
            
    def Clear(self):
        self.textbox.delete("1.0", "end")
        self.expresion = ""
       
    def clearEntry(self):
        temp = self.textbox.get("1.0", "end-1c")
        self.textbox.delete("1.0", "end")
        self.expresion = temp
        


calculator()
