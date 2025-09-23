#1 - Criar publicacao:
#Conteúdo da publicacao (por enquanto, apenas texto).
#Descricao da publicacao.
#Autor da publicação.
#Data e hora da publicacao.

#2 Curtir publicacao:
#Incrementar contador de curtidas d euma publicacao

#3 Visualizar feed:
#Exibir todas as publicacoes disponiveis
#Mostrar número de curtidas de cada publicação

#4 Visualizar publicação individual:
#Exibir detalhes de uma publicação específica (conteúdo, descrição, autor, data, curtidas, comentários.)
#Exibir detalhes de publicações de uma pessoa específica.  

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Publicacao:
    conteudo: str
    descricao: str
    autor: str
    data_hora: datetime
    curtidas: int = 0
    
lista_publicacoes = []
    #explicar o usuario entra com as informações de conteudo, autor e descrição
def criar_publicacao():
    print("\n=== CRIAR PUBLICAÇÃO===")
    conteudo = input("Digite o conteúdo da publicação: ")
    descricao = input("Digite a descrição:")
    autor = input("Digite o nome do autor: ")
    data_hora = datetime.now()
    
    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)
    print("Publicação criada com sucesso!")
    #explicacao O usuário escolhe curtir uma publicação se a lista de publicações estiver vazia, vai ter um retorno de publicação indisponível, se tiver algo na lista, o usuario escolhe oindice da publicação que quer curtire e essa curtida é adicionada na lista de publicações  
def curtir_publicacao():
    print("\n=== CURTIR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    #explicacao Se o indíce digitado fro um número negativo ou um número for maior que o tamanho da lista, o número vai ser inválido, não dando pra curtir a publicação, se o número for válido, a curtida é adicionada.
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para curtir: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].curtidas += 1
            print("Publicação curtida!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")
    #explicacao usuario pode visualizar o feed com todas as publicacoes, se não tiver nenhuma publicação, aparecerá que nenhuma publicação está disponível        
def visualizar_feed():
    print("\n=== FEED ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    for i, pub in enumerate(lista_publicacoes, 1):
        print(f"{i}. {pub.autor} - {pub.curtidas} curtidas")
        print(f"   {pub.conteudo[:50]}...")
        print(f"   {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 40)
        
def visualizar_publicacao_individual():
    print("\n=== VISUALIZAR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            print(f"\nAutor: {pub.autor}")
            print(f"Data: {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print(f"Conteúdo: {pub.conteudo}")
            print(f"Descrição: {pub.descricao}")
            print(f"Curtidas: {pub.curtidas}")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")
        
def visualizar_publicacoes_por_autor():
    print("\n=== PUBLICAÇÕES POR AUTOR ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
            
    autor = input("Digite o nome do autor: ")
    publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()]
            
    if not publicacoes_autor:
        print(f"Nenhuma publicação encontrada para {autor}.")
        return
            
    print(f"\nPublicações de {autor}:")
    for pub in publicacoes_autor:
        print(f"- {pub.conteudo[:50]}... ({pub.curtidas} curtidas)")
        print(f" {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 30)
                
def menu():
    while True:
        print("\n=== REDE SOCIAL ===")
        print("1. Criar Publicação")
        print("2. Curtir Publicação")
        print("3. Visualizar Feed")
        print("4. Visualizar Publicação Individual")
        print("5. Visualizar Publicações por Autor")
        print("0. Sair")
        opcao = input("escolha uma opção: ")
                        
                    
        if opcao == "1":
            criar_publicacao()
        elif opcao == "2":
            curtir_publicacao()
        elif opcao == "3":
            visualizar_feed()
        elif opcao == "4":
            visualizar_publicacao_individual()
        elif opcao == "5":
            visualizar_publicacoes_por_autor()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
        
menu()