import funciones
import tkinter as tk

# Variables

texto_label = ''

# ventana

win = tk.Tk()
win.title('Calculadora basica')
win.geometry('300x300')

# Cuerpo de la ventana

# Label que resive los valores

label = tk.Label(win, font=('Arial', 20), justify='right', text=texto_label)
label.grid(row=0,  column=0, columnspan=4, rowspan=2, padx=10,
           pady=10, sticky='SNEW')


def Presionar(simbolo):
    label['text'] += simbolo


# Botones

# Raiz

btn_root = tk.Button(win, text='√', command=lambda: Presionar('√'))
btn_root.grid(row=3, column=0, padx=5, pady=5, sticky='SNEW')

# Porcentaje

btn_percentage = tk.Button(win, text='%')
btn_percentage.grid(row=3, column=1, padx=5, pady=5, sticky='SNEW')

# Borrar

btn_delete = tk.Button(win, text='⌫')
btn_delete.grid(row=3, column=2, padx=5, pady=5, sticky='SNEW')

# Dividir

btn_split = tk.Button(win, text='÷')
btn_split.grid(row=3, column=3, padx=5, pady=5, sticky='SNEW')

# Ciete

btn_seven = tk.Button(win, text='7')
btn_seven.grid(row=4, column=0, padx=5, pady=5, sticky='SNEW')

# Ocho

btn_eight = tk.Button(win, text='8')
btn_eight.grid(row=4, column=1, padx=5, pady=5, sticky='SNEW')

# Nueve

btn_nine = tk.Button(win, text='9')
btn_nine.grid(row=4, column=2, padx=5, pady=5, sticky='SNEW')

# Multiplicar

btn_multiply = tk.Button(win, text='X')
btn_multiply.grid(row=4, column=3, padx=5, pady=5, sticky='SNEW')

# Cuatro

btn_four = tk.Button(win, text='4')
btn_four.grid(row=4, column=0, padx=5, pady=5, sticky='SNEW')

# Cinco

btn_five = tk.Button(win, text='5')
btn_five.grid(row=4, column=1, padx=5, pady=5, sticky='SNEW')

# Seis

btn_six = tk.Button(win, text='6')
btn_six.grid(row=4, column=2, padx=5, pady=5, sticky='SNEW')

# resta

btn_subtract = tk.Button(win, text='-')
btn_subtract.grid(row=4, column=3, padx=5, pady=5, sticky='SNEW')

# Uno

btn_one = tk.Button(win, text='1')
btn_one.grid(row=5, column=0, padx=5, pady=5, sticky='SNEW')

# Dos

btn_two = tk.Button(win, text='2')
btn_two.grid(row=5, column=1, padx=5, pady=5, sticky='SNEW')

# Three

btn_three = tk.Button(win, text='3')
btn_three.grid(row=5, column=2, padx=5, pady=5, sticky='SNEW')

# Suma

btn_add = tk.Button(win, text='+')
btn_add.grid(row=5, column=3, padx=5, pady=5, sticky='SNEW')

# Elevado

btn_high = tk.Button(win, text='^')
btn_high.grid(row=6, column=0, padx=5, pady=5, sticky='SNEW')

# Cero

btn_zero = tk.Button(win, text='0')
btn_zero.grid(row=6, column=1, padx=5, pady=5, sticky='SNEW')

# Punto

btn_point = tk.Button(win, text='.')
btn_point.grid(row=6, column=2, padx=5, pady=5, sticky='SNEW')

# Igual

btn_equals = tk.Button(win, text='=')
btn_equals.grid(row=6, column=3, padx=5, pady=5, sticky='SNEW')

for i in range(4):
    win.columnconfigure(i, weight=1)
for i in range(7):
    win.rowconfigure(i, weight=1)

win.mainloop()
