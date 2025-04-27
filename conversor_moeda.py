# Função para converter de Real para outras moedas
def converter(valor, moeda_origem, moeda_destino):
    # Taxas de conversão (simulação de taxas fixas)
    taxas = {
        "BRL-USD": 0.19,  # 1 BRL = 0.19 USD
        "BRL-EUR": 0.18,  # 1 BRL = 0.18 EUR
        "BRL-GBP": 0.15   # 1 BRL = 0.15 GBP
    }
    
    # Chave para procurar a taxa de conversão
    chave = f"{moeda_origem}-{moeda_destino}"
    
    if chave in taxas:
        valor_convertido = valor * taxas[chave]
        return valor_convertido
    else:
        return None

# Função principal para executar o conversor
def main():
    print("Bem-vindo ao Conversor de Moedas!")
    valor = float(input("Digite o valor em Reais (BRL): "))
    
    print("\nEscolha a moeda para conversão:")
    print("1. Dólar (USD)")
    print("2. Euro (EUR)")
    print("3. Libra Esterlina (GBP)")
    
    escolha = int(input("Digite o número correspondente à moeda: "))
    
    if escolha == 1:
        moeda_destino = "USD"
    elif escolha == 2:
        moeda_destino = "EUR"
    elif escolha == 3:
        moeda_destino = "GBP"
    else:
        print("Opção inválida.")
        return
    
    # Chamada da função para realizar a conversão
    valor_convertido = converter(valor, "BRL", moeda_destino)
    
    if valor_convertido is not None:
        print(f"{valor} Reais é equivalente a {valor_convertido:.2f} {moeda_destino}")
    else:
        print("Erro na conversão. Tente novamente.")

# Executa a função principal
if __name__ == "__main__":
    main()
