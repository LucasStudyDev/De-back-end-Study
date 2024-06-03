# Função para calcular os juros simples
def calcular_juros_simples(principal, taxa, tempo):
    """
    Calcula os juros simples.

    :param principal: Valor principal (em reais)
    :param taxa: Taxa de juros mensal (em porcentagem)
    :param tempo: Tempo (em meses)
    :return: Juros simples
    """
    juros = principal * (taxa / 100) * tempo
    return juros

# Função para calcular o montante total
def calcular_montante(principal, juros):
    """
    Calcula o montante total.

    :param principal: Valor principal (em reais)
    :param juros: Juros simples calculados
    :return: Montante total
    """
    montante = principal + juros
    return montante

def main():
    # Solicitar os dados do usuário
    principal = float(input("Digite o valor principal (em reais): "))
    taxa = float(input("Digite a taxa de juros mensal (em porcentagem): "))
    tempo = int(input("Digite o tempo (em meses): "))

    # Calcular os juros simples
    juros = calcular_juros_simples(principal, taxa, tempo)

    # Calcular o montante total
    montante = calcular_montante(principal, juros)

    # Exibir os resultados
    print(f"Juros simples: R$ {juros:.2f}")
    print(f"Montante total: R$ {montante:.2f}")

# Executar a função principal
if __name__ == "__main__":
    main()
    