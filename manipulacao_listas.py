# ---------------------------------------------------------
# PARTE 1: ACESSO E EXIBIÇÃO
# ---------------------------------------------------------
print("--- PARTE 1: ÍNDICES E LOOPS ---")
alunos_v1 = ['Rafaela', 'Pedro', 'Bianca', 'Jessica', 'Bruno']

# Pegando os nomes pelas posições (lembrando que o Python começa do 0!)
print(f"Aluno 3: {alunos_v1[2]}") 
print(f"Aluno 4: {alunos_v1[3]}") 

print("\nMostrando a lista toda com um loop:")
for aluno in alunos_v1:
    print(aluno)

# ---------------------------------------------------------
# PARTE 2: ADIÇÃO NO FINAL (APPEND)
# ---------------------------------------------------------
print("\n--- PARTE 2: COLOCANDO NO FINAL ---")
alunos_v2 = ['Thiago', 'Pedro', 'Bianca', 'Jessica', 'Bruno']

# Usei o append para jogar a Helena lá no final da lista
alunos_v2.append('Helena')
print(f"Lista atualizada: {alunos_v2}")

# ---------------------------------------------------------
# PARTE 3: INSERÇÃO EM POSIÇÃO ESPECÍFICA (INSERT)
# ---------------------------------------------------------
print("\n--- PARTE 3: INSERINDO ONDE EU QUERO ---")
alunos_v3 = ['Thiago', 'Pedro', 'Bianca', 'Jessica', 'Bruno']

# Aqui eu usei o insert para colocar a Daniela na posição 1 (segundo lugar)
alunos_v3.insert(1, 'Daniela')
print(f"Lista com a Daniela inserida: {alunos_v3}")
