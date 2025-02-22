import mysql.connector
import os

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Perfil"
)

cursor = conexao.cursor()

# Criar tabela se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfil (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        idade INT,
        cpf VARCHAR(14),
        email VARCHAR(100)
    )
""")


op = 0
while op != 6:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("1 - CADASTRAR PERFIL")
    print("2 - VER PERFIL")
    print("3 - LISTAR PERFIL")
    print("4 - ALTERAR DADOS GMAIL")
    print("5 - EXCLUIR CADASTRO")
    print("6 - SAIR")
    
    op = int(input("Escolha a opção desejada: "))

    if op == 1:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite seu CPF: ")
        email = input("Digite seu e-mail: ")
        
 
        comando = f'INSERT INTO perfil (nome, idade, cpf, email) VALUES ("{nome}", {idade}, "{cpf}", "{email}")'
        cursor.execute(comando)
        conexao.commit()
        print("Perfil cadastrado com sucesso!")
        input("Pressione Enter para continuar...")

    elif op == 2:
        nome = input("Digite o nome do perfil: ")
        
     
        comando = f'SELECT * FROM perfil WHERE nome = "{nome}"'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        if resultado:
            for perfil in resultado:
                print(f"Nome: {perfil[1]}")
                print(f"Idade: {perfil[2]}")
                print(f"CPF: {perfil[3]}")
                print(f"E-mail: {perfil[4]}")
        else:
            print("Perfil não encontrado.")
        
        input("Pressione Enter para continuar...")

    elif op == 3:
      
        comando = 'SELECT * FROM perfil'
        cursor.execute(comando)
        resultados = cursor.fetchall()
        
        for perfil in resultados:
            print(f"Nome: {perfil[1]}, Idade: {perfil[2]}, CPF: {perfil[3]}, E-mail: {perfil[4]}")
        
        input("Pressione Enter para continuar...")

    elif op == 4:
        nome = input("Digite o nome do cadastro que deseja alterar: ")
        novo_email = input("Digite o novo e-mail: ")
 
        comando = f'UPDATE perfil SET email = "{novo_email}" WHERE nome = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
        print(f"Perfil de {nome} alterado com sucesso!")
        input("Pressione Enter para continuar...")

    elif op == 5:
        nome = input("Digite o nome do perfil que deseja excluir: ")
        decisao = input("Tem certeza que deseja excluir este perfil? (sim/nao): ").lower()
        
        if decisao == 'sim':
            
            comando = f'DELETE FROM perfil WHERE nome = "{nome}"'
            cursor.execute(comando)
            conexao.commit()
            print(f"Perfil de {nome} excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
        
        input("Pressione Enter para continuar...")

    elif op == 6:
        print("Saindo... Obrigado!")
    else:
        print("Opção inválida!")
        input("Pressione Enter para continuar...")

cursor.close()
conexao.close()
