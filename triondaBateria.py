# 1. Definição das variáveis (altere os valores para testar os cenários)
bateria_atual = 14
bola_em_jogo = False

# 2. Processamento das regras de lógica condicional (If / Elif / Else)
if bateria_atual < 15 and bola_em_jogo == True:
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")

elif bateria_atual < 15 and bola_em_jogo == False:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    print("Sistema Trionda operando normalmente. Bateria ok.")
