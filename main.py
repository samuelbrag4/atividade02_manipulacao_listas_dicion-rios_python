# ----- Objetivo 1 ----- 

# Programa que solicita que o usuário insira 5 fruatras e armazena em uma lista.
# Além de inserir o programa possibilita que o usuário remova uma fruta da lista.

# --- Código ---

# Cria uma lista vazia para armazenar as frutas inseridas pelo usuário
frutas = []

# Solicita ao usuário que insira 5 frutas
for i in range(5):
    fruta = input(f"Insira a fruta {i+1}: ")
    frutas.append(fruta)
# Explicação:
# 1. O programa utiliza um loop for para solicitar ao usuário que insira 5 frutas.
# 2. A variavel fruta armazena o valor inserido pelo usuário e é adicionado a lista de frutas.
# 3. O loop for executa 5 vezes, solicitando ao usuário que insira uma fruta em cada iteração.
# 4. O valor de i é incrementado em 1 para exibir a ordem da fruta inserida.
# 5. A função append() é utilizada para adicionar o valor inserido pelo usuário à lista de frutas.
# 6. Ao final do loop, a lista de frutas contém as 5 frutas inseridas pelo usuário.

# Exibe a lista completa de frutas
print(f"\nLista de frutas inseridas: {frutas}")
# Explicação: O f permite que o programa insira o valor da variável frutas na string.

# Explicação: O /n é utilizado para pular uma linha antes de exibir a lista de frutas.
print("\nLista de Frutas inseridas:")

# O for faz um loop em cada fruta da lista e a imprime na tela em uma linha.
for fruta in frutas:
    print(fruta)

# - Funcionliadade de remoção de frutas -

# Solicita ao usuário que insira o nome da fruta que deseja remover
fruta_remover = input("\nDigite o nome da fruta que deseja remover:")

# if que remove a fruta da lista
if fruta_remover in frutas:
    frutas.remove(fruta_remover)
    print(f"\n{fruta_remover} foi removida da lista.")
# Explicação: "remove" serve para remover um item da lista.

else:
    print(f"\n{fruta_remover} não está na lista. Veja se escreveu corretamente ou se a fruta foi inserida.")
# Explicação: O else é utilizado para exibir uma mensagem caso a fruta não esteja na lista.

# Exibição da lista atualizada de frutas
print("\nLista atualizada de frutas:")
print(frutas)