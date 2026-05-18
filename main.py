# Você irá desenvolver um sistema de gestão de tarefas que permita ao usuário adicionar, listar, marcar como concluída e remover tarefas. O programa utilizará loops, manipulação de listas e funções para realizar essas operações.

# As tarefas a serem utilizadas poderão ter diferentes metadados: ID da tarefa, descrição, data de criação, status, prazo final, urgência, entre outros atributos... (O seu professor irá disponibilizar uma listagem de tarefas, bem como, as informações que serão manipuladas para cada uma das tarefas.)

# Funcionalidades do Programa:

# Adicionar Tarefa: Permitir ao usuário adicionar uma nova tarefa à lista de tarefas pendentes.
# Listar Tarefas: Mostrar todas as tarefas pendentes na lista, enumerando-as.
# Marcar Tarefa como Concluída: Permitir ao usuário marcar uma tarefa específica como concluída.
# Remover Tarefa: Dar ao usuário a opção de remover uma tarefa da lista.
# Detalhes da Implementação:

# Utilize loops (for e/ou while) para apresentar um menu de opções ao usuário e realizar operações repetidas.
# Manipule uma lista para armazenar e gerenciar as tarefas, incluindo adicionar, listar, marcar como concluída e remover tarefas.
# Crie funções para cada funcionalidade do sistema (adicionar, listar, marcar como concluída, remover), utilizando argumentos, parâmetros por palavra-chave, parâmetros padrão e retorno de valores.
# Documente cada função utilizando DocStrings para descrever seu propósito, uso e parâmetros.
# Este projeto lhe permite demonstrar suas habilidades em Python, incluindo o uso de loops para controle de repetição, manipulação de listas para armazenar e gerenciar tarefas, definição e utilização de funções para operações específicas e documentação adequada utilizando DocStrings para descrever o propósito e uso de cada função.

from datetime import datetime

class Tarefa:
    def __init__(self, id_tarefa, nome, prazo="Sem prazo", urgencia="Normal"):
        """
        Cria um objeto do tipo Tarefa.

        Parâmetros:
        id_tarefa (int): Identificador único da tarefa.
        nome (str): Descrição da tarefa.
        prazo (str): Prazo final da tarefa.
        urgencia (str): Nível de urgência da tarefa.
        """
        self.id = id_tarefa
        self.nome = nome
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.concluida = False
        self.prazo = prazo
        self.urgencia = urgencia

tarefas = []
contador_id = 1

def menu():
    """
    Exibe o menu principal do sistema.
    """
    print("\n===== SISTEMA DE GESTÃO DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

def adicionar_tarefa(nome=None, prazo="Sem prazo", urgencia="Normal"):
    """
    Adiciona uma nova tarefa à lista.

    Parâmetros:
    nome (str): Nome da tarefa.
    prazo (str, opcional): Prazo final da tarefa.
    urgencia (str, opcional): Nível de urgência.

    Retorna:
    Tarefa: Objeto da tarefa criada.
    """
    global contador_id

    if nome is None:
        nome = input("Digite a descrição da tarefa: ")

    prazo = input("Digite o prazo da tarefa: ")
    urgencia = input("Digite a urgência (Baixa, Normal, Alta): ")

    tarefa = Tarefa(
        id_tarefa=contador_id,
        nome=nome,
        prazo=prazo,
        urgencia=urgencia
    )

    tarefas.append(tarefa)
    contador_id += 1

    print("Tarefa adicionada com sucesso!")
    return tarefa

def listar_tarefas():
    """
    Lista todas as tarefas cadastradas.
    """
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for tarefa in tarefas:
        status = "Concluída" if tarefa.concluida else "Pendente"

        print(f"""
ID: {tarefa.id}
Descrição: {tarefa.nome}
Status: {status}
Data de criação: {tarefa.data_criacao}
Prazo: {tarefa.prazo}
Urgência: {tarefa.urgencia}
---------------------------
""")

def marcar_tarefa():
    """
    Marca uma tarefa como concluída.
    """
    if len(tarefas) == 0:
        print("Não existem tarefas cadastradas.")
        return

    listar_tarefas()

    id_tarefa = int(input("Digite o ID da tarefa concluída: "))

    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            tarefa.concluida = True
            print("Tarefa marcada como concluída!")
            return

    print("Tarefa não encontrada.")

def remover_tarefa():
    """
    Remove uma tarefa da lista.
    """
    if len(tarefas) == 0:
        print("Não existem tarefas cadastradas.")
        return

    listar_tarefas()

    id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))

    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada.")

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        marcar_tarefa()

    elif opcao == "4":
        remover_tarefa()

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")