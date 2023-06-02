from conexao import conectar

def listar(conn, cursor):
    
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM animaisAfrica")
    
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        print(resultado)
        
    cursor.close()
    conn.close()
    
    
def inserir(id, raca, quantidade, riscoExtincao, area):
    
    conn = conectar()
    cursor = conn.cursor()
    
    sql = "INSERT INTO animaisAfrica (id, raca, riscoExtincao, area) VALUES (%s, %s, %s, %s)"
    val = (id, raca, riscoExtincao, area)
    cursor.execute(sql, val)
    
    conn.commit()
    
    print("Registro inserido com sucesso.")
    
    cursor.close()
    conn.close()
    
    
    
def atualizar(id, novaRaca, novaQuantidade, novoRiscoExtincao, novaArea):
    
    conn = conectar()
    cursor = conn.cursor()
    
    sql = "UPDATE animaisAfrica SET raca = %s, quantidade = %s, riscoExtincao = %s, area = %s  WHERE id = %s"
    val = (novaRaca, novaQuantidade, novoRiscoExtincao, novaArea)
    cursor.execute(sql, val)
    
    conn.commit()
    
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado")
    else:
        print("Atualizado com sucesso")
        
        
    cursor.close()
    conn.close()
    
    
    
    
def deletar(id):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM animaisAfrica WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
    

conn = conectar()

cursor = conn.cursor()
while True:
    print("O que deseja fazer?")
    print("1 - Listar animais")
    print("2 - Inserir animais Africanos")
    print("3 - Atualizar animais")
    print("4 - Deletar animais")
    print("0 - Sair")
    
    op = int(input("Digite o número da opção desejada: "))
    
    
    if op == 1:
        listar(conn, cursor)
        
    
    elif op == 2:  
        id = int(input("Digite o código do novo animal Africano: "))
        raca = input("Digite a raça do novo animal: ")
        quantidade = int(input("Digite a quantidade de animais: "))
        riscoExtincao = input("Digite se o animal está em risco de estinção ou não (sim ou não): ")
        area = input("Digite a área em que o animal habita (norte, sul, leste, oeste): ")
        inserir(id, raca, quantidade, riscoExtincao, area)
        
    elif op == 3:  
        id = int(input("Digite o código do animal que deseja atualizar: "))
        novaRaca = input("Digite a raça do animal: ")
        novaQuantidade = int(input("Digite a quantidade de animais: "))
        novoRiscoExtincao = input("Digite se o animal está em risco de estinção ou não (sim ou não): ")
        novaArea = input("Digite a área em que o animal habita (norte, sul, leste, oeste): ")
        atualizar(id, novaRaca, novaQuantidade, novoRiscoExtincao, novaArea)
        
        
    elif op == 4:  
        codigo = int(input("Digite o código do animal que deseja deletar: "))
        deletar(id)
        
    elif op == 0:
        print("Você escolheu sair")
        break
    
    else: 
        print("Escolha uma opção válida")
        
        
        
    conn.close