from dataclasses import dataclass

@dataclass
class RegistroCliente:
    nome: str
    email: str
    telefone: str
    
    
registro_clientes = []

class ReservaCorte:
    nome: str
    estilo: str
    hora: str
    email: str
    profissional: str
    
    reservas_lista = []
    
def adicionar_cliente():
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    telefone = input("Digite o seu telefone: ")
    novo_registro = RegistroCliente(nome,email,telefone)
    registro_clientes.append(novo_regsitro)
    print("Registro concluído!")
    
def verificar_acesso():
    email_login = input("Digite seu email: ")
    telefone_login = input("Digite o seu telefone:" )
    
    for registro in registros_clientes:
         if registro.email == email_login:
            if registro.telefone == telefone_login:
                print("Acesso concedido")
            else:
                print("Email ou telefone incorretos")
                
def reservar_corte():
    estilo_corte = input("Qual estilo de corte deseja: ")
    profissional = input("Qual profissional prefere: ")
    hora_reserva = input("Informe o horário do corte: ")
    
def incluir_serviço():
    nome_servico = input("Informe o nome do serviço a adicionar: ")
    detalhes = input("Descreva o serviço: ")
    custo = input("Informe o custo do serviço: ")
    print(f"O serviço {nome_servico} foi incluído com sucesso!")

def suporte_cliente():
    mensagem = input("Informe sua dúvida: ")
    print("Um email foi enviado para você")

def opcoes_menu():
    print("\n--- ✂ Barbearia Déyan ✂ ---")
    print("1 - Registro de cliente")
    print("2 - Acesso ao sistema")
    print("3 - Reserva de corte")
    print("4 - Incluir serviço")
    print("5 - Suporte ao cliente")
    print("6 - Encerrar")
    return input("Selecione uma opção: ")

while True:
    selecao = opcoes_menu()
    if selecao == "1":
        adicionar_cliente()
    
    elif selecao == "2":
        verificar_acesso()
    
    elif selecao == "3":
        reservar_corte()
        
    elif selecao == "4":
        incluir_servico()
    
    elif selecao == "5":
        suporte_cliente()
        
    elif selecao == "6":
        print("Encerrando o programa... Até breve")
        break
    else:
        print("Opção não reconhecida")