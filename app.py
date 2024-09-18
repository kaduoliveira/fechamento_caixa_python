from datetime import datetime
import os


data_atual = datetime.now()

print()
print("Seja bem-vindo ao".center(35))
print("-------------------------------------")
print("_F_E_C_H_A_M_E_N_T_O__D_O__C_A_I_X_A_")
print("-------------------------------------")
print(data_atual.strftime("%d/%m/%Y -- %H:%M:%S").center(35))
print()
func_caixa = str(input("Responsável pelo Caixa: "))
func_caixa = func_caixa.capitalize()

cheque = 0

print("Digitando o primeiro caixa: ")
dinheiro = float(input("Vendas em DINHEIRO: "))
cartao_debito = float(input("Vendas em CARTÃO DÉBITO: "))
cartao_credito = float(input("Vendas em CARTÃO CRÉDITO: "))
cheque = float(input("Vendas em CHEQUE: "))
despesa = float(input("Totals das DESPESAS: "))
os.system()
print("---------------------VALOR--------------------")
print(f"DINHEIRO       | {dinheiro:.2f}")
print(f"Cartão Débito  | {cartao_debito:.2f}")
print(f"Cartão Crédito | {cartao_credito:.2f}")
print(f"Cheque         | {cheque:.2f}")
print("-----------------------------------------")
total1 = dinheiro + cartao_debito + cartao_credito + cheque
print(f"Total = {total1:.2f}")
print(f"Despesas = {despesa:.2f}")
print()
print("Resultado = ", total1 - despesa)
