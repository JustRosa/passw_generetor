# Password Manager - `passw_generetor`

Este projeto é um gerador de senhas seguro escrito em Python, que salva as credenciais geradas (site, e-mail e senha) em um arquivo Excel e permite que você procure contas salvas com base no nome do site. Ideal para quem quer manter suas senhas organizadas e seguras localmente.

## Funcionalidades

1. **Gerar senha**: Gera uma senha aleatória de comprimento personalizado usando letras maiúsculas, minúsculas, números e símbolos. A senha é armazenada junto com o e-mail e o nome do site no arquivo Excel.
2. **Procurar conta**: Permite buscar uma conta existente no arquivo Excel, fornecendo o nome (ou parte do nome) do site. Exibe o site, e-mail e senha armazenados.

3. **Salvamento seguro**: As informações são salvas em um arquivo Excel (`senhas_salvas.xlsx`), que é gerado e atualizado automaticamente conforme novas senhas são criadas. O arquivo também ajusta automaticamente a largura das colunas para melhorar a legibilidade.

## Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina, além das bibliotecas necessárias:

### Instalar bibliotecas necessárias

Para instalar as bibliotecas exigidas, execute o seguinte comando:

```bash
pip install pandas openpyxl
```

## Como usar

1. Clone este repositório ou faça o download do arquivo `main.py` para seu computador.
2. Execute o script `main.py` no terminal/console:

```bash
python main.py
```

### Menu principal

Ao iniciar o programa, você verá o seguinte menu:

```
   ___                  ___                         _
  / _ \__ _ ___ ___    / _ \___ _ __   ___ _ __ ___| |_ ___  _ __
 / /_)/ _` / __/ __|  / /_\/ _ \ '_ \ / _ \ '__/ _ \ __/ _ \| '__|
/ ___/ (_| \__ \__ \ / /_\\  __/ | | |  __/ | |  __/ || (_) | |
\/    \__,_|___/___/ \____/\___|_| |_|\___|_|  \___|\__\___/|_|

by : C0d3x_

Menu:
1. Gerar senha
2. Procurar conta
99. Sair
```

### Opções do menu

- **1. Gerar senha**: Escolha esta opção para gerar uma senha. Você será solicitado a fornecer:
  - Nome do site.
  - Endereço de e-mail.
  - Comprimento desejado da senha (recomendado 16+).

A senha será gerada e salva automaticamente no arquivo Excel `senhas_salvas.xlsx`.

- **2. Procurar conta**: Escolha esta opção para procurar uma conta armazenada. Basta digitar o nome do site (ou parte do nome), e o programa irá exibir as informações correspondentes, como site, e-mail e senha.

- **99. Sair**: Use esta opção para encerrar o programa.

## Exemplo de uso

### Gerando uma senha:

```
Escolha uma opção (1, 2, ou 99): 1
Digite o nome do site: facebook.com
Digite o e-mail: user@example.com
Digite o tamanho da senha (ex: 16): 20

Senha gerada: sA}g$zR9qA?B)nxK@!%o
Dados salvos com sucesso no arquivo senhas_salvas.xlsx!
```

### Procurando uma conta:

```
Escolha uma opção (1, 2, ou 99): 2
Digite o nome do site que deseja procurar (pode ser parte do nome): facebook

Conta(s) encontrada(s) para o site 'facebook':

Site  : facebook.com
Email : user@example.com
Senha : sA}g$zR9qA?B)nxK@!%o
----------------------------------------
```

## Estrutura do projeto

```
passw_generetor/
│
├── main.py          # Script principal do gerenciador de senhas
├── README.md        # Instruções e documentação do projeto
├── requirements.txt # Dependências do projeto (opcional)
└── senhas_salvas.xlsx # Arquivo gerado com as senhas armazenadas (criado automaticamente)
```

## Melhorias futuras

- Criptografia das senhas no arquivo Excel para maior segurança.
- Interface gráfica para facilitar o uso.
- Suporte para organização por pastas/etiquetas dentro do gerenciador de senhas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um _issue_ ou _pull request_ com melhorias ou correções.
