from conection import conectar
from tkinter import messagebox

def inserir_impressora(tipo, modelo):
    conn = conectar()
    cursor = conn.cursor()
    query = '''INSERT INTO impressoras (tipo, modelo)
               VALUES (%s, %s)'''
    cursor.execute(query, (tipo, modelo))
    conn.commit()
    conn.close()

def listar_impressoras():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM impressoras")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_lista_treeview(tree):
    # Limpa o treeview
    for row in tree.get_children():
        tree.delete(row)
    try:
        impressoras = listar_impressoras()
        for imp in impressoras:
            tree.insert("", "end", values=imp)
    except Exception as e:
        messagebox.showerror("erro", f"Erro ao listar impressoras: {str(e)}")

def cadastrar_impressora_interface(tipo_var, modelo_var, tree):
    tipo = tipo_var.get()
    modelo = modelo_var.get()

    if not tipo or not modelo:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return
    
    try:
        inserir_impressora(tipo, modelo)
        messagebox.showinfo("Sucesso", "Impressora cadastrada com sucesso")
        # Limpa os dados após o cadastro
        tipo_var.set("")
        modelo_var.set("")
        # Atualiza a lista automaticamente
        atualizar_lista_treeview(tree)
    except Exception as e:
        return False, f"Erro ao cadastrar: {str(e)}"
    
    #---------------------------------------------------------------
    # Funções consumíveis 
    #------------------------------------------------------------------

def inserir_consumivel(id_impressora, nome, tipo, quantidade):
    conn = conectar()
    cursor = conn.cursor()
    query = '''INSERT INTO consumiveis (id_impressora, nome, tipo, quantidade)
                VALUES (%s, %s, %s, %s)'''
    conn.commit()
    conn.close()
    
def listar_consumiveis():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''SELECT c.id, i.modelo, c.nome, c.tipo, c.quantidade
                        FROM consumiveis c
                        JOIN impressoras i on c.id_impressora = i.id''')
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_lista_consumiveis_treeview(tree):
    # Limpa o Treeview de consumíveis 
    for row in tree.get_children():
        tree.delete(row)
    try:
        consumiveis = listar_consumiveis()
        for c in consumiveis:
            tree.insert("", "end", values=c)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao listar consumíveis: {str(e)}")

def cadastrar_consumivel_interface(impressora_var, nome_var, tipo_consumivel_var, quantidade_var, tree):
    # Extrai os valores dos campos
    impressora_str = impressora_var.get()
    nome = nome_var.get()
    tipo = tipo_consumivel_var.get()
    quantidade_str = quantidade_var.get()

    if not impressora_str or not nome or not tipo or not quantidade_str:
        messagebox.showwarning("Atenção", "Preencha todos os campos")
        return

        # Combobox de impressoras deverá ter ter itens no formato "ID - Modelo"
    try:
        id_impressora = int(impressora_str.split(" - ")[0])
    except Exception as e:
        messagebox.showwarning("Atenção", "Selecione uma impressora válida.")
        return
        
    try:
        quantidade = int(quantidade_str)
    except:
        messagebox.showwarning("Atenção", "Quantidade deve ser um número inteiro.")
        return
    
    try:
        inserir_consumivel(id_impressora, nome, tipo, quantidade)
        messagebox.showinfo("Sucesso", "Consumível cadastrado com sucesso!")
        impressora_var.set("")
        nome_var.set("")
        tipo_consumivel_var.set("")
        quantidade_var.set("")
        atualizar_lista_consumiveis_treeview(tree)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar consumível: {str(e)}")
        
        
