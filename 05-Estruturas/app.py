'''
# Create
# Read
# Update
# Delete
# List


# Contabilidade
# 5% caso recebam até 2000.00
# 4% caso recebam até 3000.00
# 3% caso recebam acima de 3000.00
# Gerência receberão 800.00
# Para cada dependente, receberá 200.00
# Exibir um relatório informando, para cada colaborador, 
# - o seu nome, 
# - o salário atual
# - a quant de dep.
# - o cargo
# - a porcentagem de aumento
# - novo salário
'''
from os import system, name

def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

# 0 - nome,      1 - sal    2 - dep  3 - cargo  4 - aum  5 - novo sal
funcionarios = [
        {
            "nome": "Fulano de tal", 
            "salario": 2_000.00,  
            "dep": 2,      
            "cargo": "A. Adm.", 
            "aumento": 1.0,     
            "novo_salario": 0.0
        },
        {
            "nome": "Ciclano de tal", 
            "salario": 3_000.00,  
            "dep": 1,      
            "cargo": "Gerente", 
            "aumento": 1.0,     
            "novo_salario": 0.0
        }
    ]




def aplicar_atualizacao_salarial(func):
    if func["salario"] <= 2000.0: func["aumento"] = 1.05
    elif func["salario"] <= 3000.0: func["aumento"] = 1.04
    else: func["aumento"] = 1.03

    func["novo_salario"] = func["salario"] * func["aumento"]

    if func["cargo"] == 'Gerente' :
        func["novo_salario"] = func["novo_salario"] + 800.0

    func["novo_salario"] = func["novo_salario"] + (func["dep"] * 200.0)

    print(func['nome'], end="\t")
    print(f"R$ {func['salario']}", end="\t")
    print(func["dep"], end="\t")
    print(f"{func['cargo']}\t{func['aumento']}\t{func['novo_salario']}")

# Exibe o relatorio de atualizacao salarial
def exibir_atualizacao_salarios(funcs):
    print(f"Funcionario\tSal. Atual\tDeps\tCargo\tAumento\tNovo Sal.")
    for func in funcs:
        aplicar_atualizacao_salarial(func)

'''func_nome_b = "Ciclano de tal"
func_salario_b = 3_000.00
func_dep_b = 1
func_cargo_b = "Gerente"

aumento_b = 1.0
if func_salario_b <= 2000.0: aumento_b = 1.05
elif func_salario_b <= 3000.0: aumento_b = 1.04
else: aumento_b = 1.03

func_novo_salario_b = func_salario_b * aumento_b

if func_cargo_b == 'Gerente' :
    func_novo_salario_b = func_novo_salario_b + 800.0

func_novo_salario_b = func_novo_salario_b + (func_dep_b * 200.0)

# print(f"{func[0]}\tR$ {func[1]}\t{func[2]}", end="\t")
# print(f"{func[3]}\t{func[4]}\t{func[5]}")
# print(f"{func_nome_b}\tR$ {func_salario_b}\t{func_dep_b}", end="\t")
# print(f"{func_cargo_b}\t{aumento_b}\t{func_novo_salario_b}")
'''

def exibir_opcoes_menu():
    print('Escolha uma opção ou 0 para sair:')
    print('1 - Listar Funcionarios')
    print('2 - Inserir Funcionario')
    print('3 - Exibir Funcionario')
    print('4 - Atualizar Funcionario')
    print('5 - Remover Funcionario')
    print('0 - Sair')
    
def lista_funcionarios(): 
    print("Lista de Funcionarios:")
    for id, funcionario in enumerate(funcionarios):
        print(id, ' - ', funcionario['nome'])

def exibir_funcionario(identificador):
    func = funcionarios[identificador]
    print(f"Funcionario\tSalário\tDeps\tCargo")
    print(f"{func['nome']}\t{func['salario']}\t{func['dep']}\t{func['cargo']}")

def inserir_novo_funcionario(funcionario): 
    funcionarios.append(funcionario)

def atualizar_funcionario(identificador, funcionario):
    funcionarios[identificador] = funcionario

def remover_funcionario(identificador):
    funcionarios.pop(identificador)

def pegar_info_func():
    func = {}
    func['nome'] = input("Nome do funcionario: ")
    func['salario'] = float(input("Salário: "))
    func['dep'] = int(input("Quant. de Dep: "))
    func['cargo'] = input("Cargo: ")
    func['aumento'] = 1.0
    func['novo_salario'] = 0.0
    return func

def inicio():
    fim_do_programa = False
    while (not fim_do_programa):
        exibir_opcoes_menu()
        opcao = int(input('Opção: '))
        if (opcao == 0): fim_do_programa = True
        elif (opcao == 1): 
            clear()
            lista_funcionarios()
        elif (opcao == 2):
            func = pegar_info_func()
            inserir_novo_funcionario(func)
        elif (opcao == 3): 
            clear()
            id = int(input('Informe o id do funcionario: '))
            exibir_funcionario(id)
        elif (opcao == 4):
            id = int(input('Informe o id do funcionario: '))
            func = pegar_info_func()
            atualizar_funcionario(id, func)
        elif (opcao == 5):
            id = int(input('Informe o id do funcionario: '))
            remover_funcionario(id)
inicio()