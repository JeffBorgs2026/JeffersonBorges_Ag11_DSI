from colorama import Back, Fore, Style, init

# Inicializa o colorama para restaurar o padrão do terminal automaticamente
init(autoreset=True)


def definir_cor_nivel(nivel):
  """Função responsável por retornar a cor correspondente

  conforme o nível de água informado do reservatório.
  """
  if nivel == 1:
    return Fore.RED + Style.BRIGHT
  elif nivel == 2:
    return Fore.YELLOW + Style.BRIGHT
  elif nivel == 3:
    return Fore.GREEN + Style.BRIGHT
  elif nivel == 4:
    return Fore.CYAN + Style.BRIGHT
  elif nivel == 5:
    return Fore.BLUE + Style.BRIGHT
  else:
    return Style.RESET_ALL


def main():
  # Lista contendo os dados dos níveis do reservatório
  reservatorio_niveis = [
      {
          "nivel": "Nível 1",
          "situacao": "Muito baixo (crítico)",
          "cor_sugerida": "Vermelho",
      },
      {"nivel": "Nível 2", "situacao": "Baixo", "cor_sugerida": "Amarelo"},
      {"nivel": "Nível 3", "situacao": "Médio", "cor_sugerida": "Verde"},
      {"nivel": "Nível 4", "situacao": "Alto", "cor_sugerida": "Ciano"},
      {
          "nivel": "Nível 5",
          "situacao": "Muito alto (alerta)",
          "cor_sugerida": "Azul",
      },
  ]

  print("=== SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA ===")
  print("Simulando status atuais do sistema:\n")

  # Loop para percorrer a lista e exibir os alertas coloridos no terminal
  for i, dados in enumerate(reservatorio_niveis, start=1):
    estilo_cor = definir_cor_nivel(i)
    mensagem = f"[{dados['nivel']}] - Situação: {dados['situacao']} (Cor de alerta: {dados['cor_sugerida']})"
    print(estilo_cor + mensagem)

  print("\nMonitoramento finalizado. Estilos do terminal restaurados.")


if __name__ == "__main__":
  main()