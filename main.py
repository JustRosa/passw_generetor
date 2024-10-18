import string
import random
import pandas as pd
import os
from openpyxl import load_workbook

# ASCII art para exibição no menu
def exibir_ascii_art():
    print(r"""
   ___                  ___                         _             
  / _ \__ _ ___ ___    / _ \___ _ __   ___ _ __ ___| |_ ___  _ __ 
 / /_)/ _` / __/ __|  / /_\/ _ \ '_ \ / _ \ '__/ _ \ __/ _ \| '__|
/ ___/ (_| \__ \__ \ / /_\\  __/ | | |  __/ | |  __/ || (_) | |   
\/    \__,_|___/___/ \____/\___|_| |_|\___|_|  \___|\__\___/|_|   
                                                                  
by : C0d3x_
    """)

# Função para gerar a senha
def gerar_senha(tamanho=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Função para ajustar automaticamente o tamanho das células no arquivo Excel
def ajustar_largura_colunas(nome_arquivo):
    wb = load_workbook(nome_arquivo)
    ws = wb.active
    
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Pega a letra da coluna
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = max_length + 2
        ws.column_dimensions[column].width = adjusted_width
    
    wb.save(nome_arquivo)

# Função para salvar a senha em um arquivo Excel
def salvar_senha(site, email, senha, nome_arquivo="senhas_salvas.xlsx"):
    if os.path.exists(nome_arquivo):
        df = pd.read_excel(nome_arquivo)
    else:
        df = pd.DataFrame(columns=["Site", "Email", "Senha"])
    
    novo_dado = pd.DataFrame({"Site": [site], "Email": [email], "Senha": [senha]})
    df = pd.concat([df, novo_dado], ignore_index=True)
    
    df.to_excel(nome_arquivo, index=False)
    ajustar_largura_colunas(nome_arquivo)
    print(f"\nDados salvos com sucesso no arquivo {nome_arquivo}!\n")

# Função para procurar uma conta pelo site
def procurar_conta(site, nome_arquivo="senhas_salvas.xlsx"):
    if os.path.exists(nome_arquivo):
        df = pd.read_excel(nome_arquivo)
        # Busca por correspondência parcial, ignorando maiúsculas/minúsculas
        conta = df[df['Site'].str.contains(site, case=False, na=False)]
        if not conta.empty:
            print(f"\nConta(s) encontrada(s) para o site '{site}':\n")
            for index, row in conta.iterrows():
                print(f"Site  : {row['Site']}")
                print(f"Email : {row['Email']}")
                print(f"Senha : {row['Senha']}")
                print("-" * 40)  # Separador entre entradas
        else:
            print(f"\nNenhuma conta encontrada para o site '{site}'.\n")
    else:
        print("\nNenhum arquivo de senhas encontrado.\n")

# Função principal com menu
def main():
    exibir_ascii_art()  # Exibe o ASCII art ao iniciar o menu
    print("\nMenu:")
    print("1. Gerar senha")
    print("2. Procurar conta")
    print("99. Sair")
    
    escolha = input("\nEscolha uma opção (1, 2, ou 99): ")
    
    if escolha == '1':
        site = input("\nDigite o nome do site: ")
        email = input("Digite o e-mail: ")
        tamanho_senha = int(input("Digite o tamanho da senha (ex: 16): "))
        
        senha = gerar_senha(tamanho_senha)
        print(f"\nSenha gerada: {senha}")
        
        salvar_senha(site, email, senha)
    
    elif escolha == '2':
        site = input("\nDigite o nome do site que deseja procurar (pode ser parte do nome): ")
        procurar_conta(site)
    
    elif escolha == '99':
        print("\nSaindo do programa...\n")

    else:
        print("\nOpção inválida. Por favor, escolha 1, 2, ou 99.\n")

if __name__ == "__main__":
    main()
