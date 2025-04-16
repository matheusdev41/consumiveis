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
    