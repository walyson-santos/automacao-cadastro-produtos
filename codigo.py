import pyautogui
import time
import pandas
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
senha = os.getenv("SENHA")

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta uma atalho
# PAUSE é para ter uma pausa de 1 segundo entre cada comando



pyautogui.PAUSE = 2
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo a passo do programa

# Email: walyson@gmail.com
# Senha: walyson123
 
# Passo 1: Entrar no sistema da empresa
# Abrir o navegador

pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# fazer uma pausa maior para o site carregar usando a biblioteca "time"
time.sleep(3)


# Passo 2: Fazer login no site da empresa 
pyautogui.click(x=664, y=472)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto

for linha in tabela.index:

    pyautogui.click(x=705, y=325)

    # codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco_unitario 
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") # para cadastrar o produto

    pyautogui.scroll(5000) # para rolar a página para cima 