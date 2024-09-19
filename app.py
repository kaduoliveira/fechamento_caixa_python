from datetime import datetime
import os
import win32print
import win32api

data_atual = datetime.now()

print()
print("Seja bem-vindo ao".center(35))
print("-------------------------------------")
print("_F_E_C_H_A_M_E_N_T_O__D_O__C_A_I_X_A_")
print("-------------------------------------")
print(data_atual.strftime("%d/%m/%Y -- %H:%M:%S").center(35))
print()
func_caixa = str(input("Responsável pelo Caixa: "))

match func_caixa:
    case '1':
        print("Michelly".upper())
    case '2':
        print("Geovana".upper())
    case '3':
        print("Kadu".upper())

func_caixa = func_caixa.capitalize()

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
despesa = float(input("Totals das DESPESAS: "))
despesa = round(despesa, 2)

os.system('cls')
print("----------------------------------------------")
print("----_F_E_C_H_A_M_E_N_T_O__D_O__C_A_I_X_A_-----")
print("----------------------------------------------")
print("---------------------VALOR--------------------")
print("DINHEIRO       |",f" {dinheiro} |".rjust(10))
print("Cartão Débito  |",f" {cartao_debito} |".rjust(10))
print("Cartão Crédito |",f" {cartao_credito} |".rjust(10))
print("Cheque         |",f" {cheque} |".rjust(10))
print("----------------------------------------------")
total1 = dinheiro + cartao_debito + cartao_credito + cheque
print(f"Total = {total1:.2f}")
print(f"Despesas = {despesa:.2f}")
print()
print("----------------------------------------------")
resultado = total1 - despesa
print(f" RESULTADO = R$ {resultado:.2f}")
print("----------------------------------------------")

file_name = "saida_cmd.txt"
with open(file_name, "w") as f:
    subprocess.run(stdout=f, shell=True)

printer_name = win32print.GetDefaultPrinter()
file_name = "arquivo.txt"
win32api.ShellExecute(0, "print", file_name, None, ".", 0)