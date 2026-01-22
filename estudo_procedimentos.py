# ---------------------------------------------------------
# PROCEDIMENTO 1: Simples (Sem parâmetros)
# Objetivo: Executar uma tarefa fixa e repetitiva.
# ---------------------------------------------------------
def saudacao_simples():
    print("Olá mundo! (Este é o procedimento 1)")

# ---------------------------------------------------------
# PROCEDIMENTO 2: Com Parâmetro
# Objetivo: Usar um dado externo para tornar a função dinâmica.
# ---------------------------------------------------------
def saudacao_personalizada(nome_usuario):
    print(f"Olá {nome_usuario}, bem-vindo ao procedimento 2!")

# ---------------------------------------------------------
# PROCEDIMENTO 3: Com Lógica Condicional
# Objetivo: Tomar decisões dentro da função.
# ---------------------------------------------------------
def verificar_sexo(sexo):
    # .lower() converte para minúsculo para evitar erro se digitar 'F' ou 'M'
    if sexo.lower() == "f":
        print("Resultado: Feminino (Processado pelo procedimento 3)")
    elif sexo.lower() == "m":
        print("Resultado: Masculino (Processado pelo procedimento 3)")
    else:
        print("Resultado: Opção Inválida")

# =========================================================
# PROGRAMA PRINCIPAL (Execução dos procedimentos)
# =========================================================

# Executando o Procedimento 1
print("--- TESTANDO PROCEDIMENTO 1 ---")
saudacao_simples()

print("\n--- TESTANDO PROCEDIMENTO 2 ---")
nome = input("Digite o seu nome: ")
saudacao_personalizada(nome)

print("\n--- TESTANDO PROCEDIMENTO 3 ---")
opcao_sexo = input("Digite (f) para feminino ou (m) para masculino: ")
verificar_sexo(opcao_sexo)

print("\n" + "="*30)
print("Fim da demonstração dos procedimentos.")
