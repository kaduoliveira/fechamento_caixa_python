from datetime import datetime
import os
import win32print
import win32api

# Coleta da data atual
data_atual = datetime.now()

# Exibição no terminal
print()
print("Seja bem-vindo ao".center(35))
print("-------------------------------------")
print("_F_E_C_H_A_M_E_N_T_O__D_O__C_A_I_X_A_")
print("-------------------------------------")
print(data_atual.strftime("%d/%m/%Y -- %H:%M:%S").center(35))
print()
func_caixa = str(input("Responsável pelo Caixa: "))

# Seleção do responsável pelo caixa
match func_caixa:
    case '1':
        print("Michelly".upper())
    case '2':
        print("Geovana".upper())
    case '3':
        print("Kadu".upper())

func_caixa = func_caixa.capitalize()

# Variáveis para os valores do fechamento
cheque = 0
print("      \nDigitando o primeiro caixa:\n ")
dinheiro = float(input("Vendas em DINHEIRO: "))
dinheiro = round(dinheiro, 2)
cartao_debito = float(input("Vendas em CARTÃO DÉBITO: "))
cartao_debito = round(cartao_debito, 2)
cartao_credito = float(input("Vendas em CARTÃO CRÉDITO: "))
cartao_credito = round(cartao_credito, 2)
cheque = float(input("Vendas em CHEQUE: "))
cheque = round(cheque, 2)
despesa = float(input("Total das DESPESAS: "))
despesa = round(despesa, 2)

# Limpa o terminal
os.system('cls')

# Cálculos
total1 = dinheiro + cartao_debito + cartao_credito + cheque
resultado = total1 - despesa

# Armazenar a saída em um arquivo de texto
file_name = "saida_cmd.txt"
with open(file_name, "w") as f:
    f.write("----------------------------------------------\n")
    f.write("----_F_E_C_H_A_M_E_N_T_O__D_O__C_A_I_X_A_-----\n")
    f.write("----------------------------------------------\n")
    f.write("---------------------VALOR--------------------\n")
    f.write(f"DINHEIRO       | {dinheiro} |\n")
    f.write(f"Cartão Débito  | {cartao_debito} |\n")
    f.write(f"Cartão Crédito | {cartao_credito} |\n")
    f.write(f"Cheque         | {cheque} |\n")
    f.write("----------------------------------------------\n")
    f.write(f"Total = {total1:.2f}\n")
    f.write(f"Despesas = {despesa:.2f}\n")
    f.write("----------------------------------------------\n")
    f.write(f"RESULTADO = R$ {resultado:.2f}\n")
    f.write("----------------------------------------------\n")

# Envio do arquivo para a impressora
printer_name = win32print.GetDefaultPrinter()
win32api.ShellExecute(0, "print", file_name, None, ".", 0)
