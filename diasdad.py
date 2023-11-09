import tkinter as tk

janela = tk.Tk()
padrao = tk.Frame(relief=tk.SUNKEN)
padrao.pack()

t1 = tk.Label(master=padrao, text="nome").grid(row=0,column=0,sticky="e")
t1e = tk.Entry(master=padrao, width=50).grid(row=0,column=1)

janela.mainloop()