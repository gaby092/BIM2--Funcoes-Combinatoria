import math

# Função para calcular combinações
def calcular_combinacoes(N, M):
    combinacoes = math.factorial(N) / (math.factorial(M) * math.factorial(N - M))
    return int(combinacoes)

# Função para determinar o status do aluno com base na média
def determinar_status_nota(nota):
    if nota > 6:
        return "Aprovado"
    elif 4 <= nota <= 6:
        return "Verificação Suplementar"
    else:
        return "Reprovado"

# Lê o valor de N e M
N = int(input("Digite o valor de N (número total de alunos): "))
M = int(input("Digite o valor de M (número de alunos no primeiro grupo): "))

# Calcula e imprime o número de combinações possíveis
comb = calcular_combinacoes(N, M)
print(f"Número de combinações possíveis: {comb}")

# Solicita a nota do aluno
nota_aluno = float(input("Digite a nota do aluno: "))

# Determina e imprime o status do aluno com base na nota
status_aluno = determinar_status_nota(nota_aluno)
print(f"Status do aluno: {status_aluno}")
