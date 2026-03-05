#nova atualizacao

#bibliotecas que utilizei ]
import pyautogui
import time
import pandas as pd

# variaveis para salvar as informacoes
EMAIL = "dev@gmail.com"
PASSWORD = "sua senha"
LOGIN_URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
CSV_PATH = "registrodeprodutos.csv"

# coordenadas da tela para clicar nos campos
COORDS = {
    "email_field": (730, 397),
    "first_code_field": (714, 277), 
}


pyautogui.FAILSAFE = True  
pyautogui.PAUSE = 1  # pausa para cada comando

def open_browser():
    """inciar o navegador e abrir pagina de login"""
    pyautogui.press("win")
    pyautogui.write("opera")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write(LOGIN_URL)
    pyautogui.press("enter")
    time.sleep(3)


def login():
    """fazer login."""
    pyautogui.click(*COORDS["email_field"])
    pyautogui.write(EMAIL)
    pyautogui.press("tab")
    pyautogui.write(PASSWORD)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)


def fill_row(row: pd.Series):
    pyautogui.click(*COORDS["first_code_field"])

    for col in ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]:
        value = row.get(col, "")
        if pd.isna(value) or value == "":
            pyautogui.press("tab")
            continue
        pyautogui.write(str(value))
        pyautogui.press("tab")

    pyautogui.press("enter")
    # dar um scroll de volta ao topo
    pyautogui.scroll(5000)


def main():
    open_browser()
    login()

    tabela = pd.read_csv(CSV_PATH)
    print(tabela)

    for _, row in tabela.iterrows():
        fill_row(row)

    print("All products have been registered.")


if __name__ == "__main__":
    main()