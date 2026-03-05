import pyautogui
import time
import pandas as pd

# configuration constants
EMAIL = "dev@gmail.com"
PASSWORD = "sua senha"
LOGIN_URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
CSV_PATH = "registrodeprodutos.csv"

# screen coordinates (x, y) for the fields/butto
# ns used by the automation
COORDS = {
    "email_field": (730, 397),
    "first_code_field": (653, 294),
}

# adjust PyAutoGUI behaviour
pyautogui.FAILSAFE = True  # move mouse to upper-left to abort
pyautogui.PAUSE = 0.5  # short pause after each call


def open_browser():
    """Start the browser and navigate to the login page."""
    pyautogui.press("win")
    pyautogui.write("opera")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write(LOGIN_URL)
    pyautogui.press("enter")
    time.sleep(3)


def login():
    """Perform the user login sequence."""
    pyautogui.click(*COORDS["email_field"])
    pyautogui.write(EMAIL)
    pyautogui.press("tab")
    pyautogui.write(PASSWORD)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)


def fill_row(row: pd.Series):
    """Fill a single product row on the form."""
    # focus first field so tabs work predictably
    pyautogui.click(*COORDS["first_code_field"])

    for col in ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]:
        value = row.get(col, "")
        if pd.isna(value) or value == "":
            pyautogui.press("tab")
            continue
        pyautogui.write(str(value))
        pyautogui.press("tab")

    pyautogui.press("enter")
    # scroll back to top so next iteration starts at the same place
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