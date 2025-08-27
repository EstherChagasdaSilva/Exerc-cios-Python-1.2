def bilheteria_de_evento():
    print('\n--- Show do One Direction ---')
    print('1 - Vender ingresso')
    print('2 - Repor ingressos')
    print('3 - Ver ingressos disponíveis')
    print('0 - Sair')
    return input('Escolha uma opção: ')
    
    
    # Variáveis de controle
Ingresso = None
quantidade = 0
    
while True:
    opcao = bilheteria_de_evento()
        
    if opcao == '1':
        Ingresso = input('Quantos ingressos você quer vender?')
        Quantidade = 0
        print(f"Produto 2'{Ingresso}' cadastrado com sucesso!")
            
    elif opcao == '2':
        if ingresso is None:
            print('Nenhum ingresso cadastrado ainda!')
        else:
            retirar = int(input('Digite a quantidade a retirar:'))
        if retirar <= 0:
            print('A quantidade deve ser maior que zero!')
        elif retirar > quantidade:
            print('Quantidade insuficiente no estoque!')
        else:
            quantidade -= retirar
            print(f'Retirado {retirar} unidade(s). Estoque atual: {quantidade}')
    
    elif opcao == "3":
            if Ingresso is None:
                print('Nenhum ingresso cadastrado ainda!')
            else:
                adicionar = int(input('Digite a quantidade a adicionar:'))
                if adicionar <= 0:
                    print('A quantidade deve ser maior que zero!')
                else:
                    quantidade += adicionar
                    print(f"Adicionado {adicionar} unidade(s). Estoque atual:{quantidade}")
                
    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break
                
    else:
        print("Opção inválida, tente novamente.")
                    
                    