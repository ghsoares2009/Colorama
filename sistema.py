import colorama
from colorama import Fore, Style

# Inicializa o colorama (essencial para Windows)
colorama.init()

def exibir_status_reservatorio(nivel_atual):
    """
    Função responsável por definir a cor e exibir a mensagem 
    conforme o nível informado.
    """
    
    # Lista de configurações (Nível, Mensagem, Cor)
    configuracoes = [
        {"nivel": 1, "status": "Muito baixo (crítico)", "cor": Fore.RED},
        {"nivel": 2, "status": "Baixo", "cor": Fore.YELLOW},
        {"nivel": 3, "status": "Médio", "cor": Fore.GREEN},
        {"nivel": 4, "status": "Alto", "cor": Fore.CYAN},
        {"nivel": 5, "status": "Muito alto (alerta)", "cor": Fore.BLUE},
    ]

    # Busca as informações baseadas no nível informado
    for config in configuracoes:
        if config["nivel"] == nivel_atual:
            print(f"Monitoramento: Nível {config['nivel']}")
            print(f"Situação: {config['cor']}{config['status']}{Style.RESET_ALL}")
            print("-" * 30)
            return

    print("Nível inválido informado.")

def simulacao():
    print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---")
    
    # Simulando a leitura de diferentes níveis
    niveis_para_testar = [1, 2, 3, 4, 5]
    
    for nivel in niveis_para_testar:
        exibir_status_reservatorio(nivel)

if __name__ == "__main__":
    try:
        simulacao()
    finally:

        print(Style.RESET_ALL)
        colorama.deinit()