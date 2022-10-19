from playwright.sync_api import sync_playwright
from time import sleep

meuNome = "imports_bjl"
minhaSenha = "informatica013"

class playwright:
   with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.instagram.com")
            page.locator('//*[@id="loginForm"]/div/div[1]/div/label/input').click()

            page.locator('//*[@id="loginForm"]/div/div[1]/div/label/input').fill(meuNome)
            sleep(4)
            page.locator('//*[@id="loginForm"]/div/div[2]/div/label/input').click()
            sleep(5)
            page.locator('//*[@id="loginForm"]/div/div[2]/div/label/input').fill(minhaSenha)
            sleep(2)
            page.locator('//*[@id="loginForm"]/div/div[3]/button').click()
            sleep(100)
            browser.close()

print("automação Finalizada :)")     