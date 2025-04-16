import tkinter as tk
from tkinter import ttk, messagebox
from models import (
    cadastrar_impressora_interface,
    atualizar_lista_treeview,
    listar_impressoras,
    cadastrar_consumivel_interface,
    atualizar_lista_consumiveis_treeview
)
# Janela principal
root = tk.Tk()
root.title("Controle de consumíveis")
root.geometry("800x600")

# Criar abas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

#-------------------------------------------
# Aba 1: Cadastro de Impressoras
#-------------------------------------------
frame_impressora = ttk.Frame(notebook)
notebook.add(frame_impressora, text='Cadastro de Impressora')

# Campos
ttk.Label(frame_impressora, text="Tipo de Impressora:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
tipo_var = tk.StringVar()
tipo_combo = ttk.Combobox(frame_impressora, textvariable=tipo_var, values=["laser", "jato_tinta"])
tipo_combo.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(frame_impressora, text="Modelo:").grid(row=0, column=2, padx=10, pady=10, sticky='w')
modelo_var = tk.StringVar()
modelo_entry = ttk.Entry(frame_impressora, textvariable=modelo_var)
modelo_entry.grid(row=0, column=3, padx=10, pady=10, sticky='w')

# botão
ttk.Button(
    frame_impressora,
    text="Cadastrar Impressora",
    command=lambda: cadastrar_impressora_interface(tipo_var, modelo_var, tree)
).grid(row=0, column=4, columnspan=2,pady=20, sticky='ew')

# Treeview para exibir a lista de impressoras 
tree = ttk.Treeview(frame_impressora, columns=("id", "tipo", "modelo"), show="headings")
tree.heading("id", text="ID")
tree.heading("tipo", text="Tipo")
tree.heading("modelo", text="Modelo")
tree.column("id", width=50, anchor='center')
tree.column("tipo", width=150, anchor='center')
tree.column("modelo", width=150, anchor='center')
tree.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

scrollbar = ttk.Scrollbar(frame_impressora, orient=tk.VERTICAL, command=tree.yview)
tree.config(yscrollcommand=scrollbar.set)
scrollbar.grid(row=2, column=4, sticky='ns', pady=10)

frame_impressora.rowconfigure(2, weight=1)

#--------------------------------------------
# Aba 2: Cadastro de Consumíveis
#--------------------------------------------

frame_consumiveis = ttk.Frame(notebook)
notebook.add(frame_consumiveis, text='Cadastro de Consumíveis')

for i in range(4):
    frame_consumiveis.columnconfigure(i, weight=1)

# Carrega a lista de impressoras para o combobox (formato "ID - MODELO")
impressoras = listar_impressoras()
impressoras_lista = [f"{imp[0]} - {imp[2]}" for imp in impressoras]

ttk.Label(frame_consumiveis, text="Impressora:")\
    .grid(row=0, column=0, padx=10, pady=10, sticky='w')
impressora_var = tk.StringVar()
impressora_combo = ttk.Combobox(frame_consumiveis, textvariable=impressora_var, values=impressoras_lista)
impressora_combo.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# fazer label nome consumível 
