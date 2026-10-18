# pages/login_page.py
from playwright.sync_api import Page, expect
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Para el nickname 
        self.username = page.locator("#nickname")  
        
        # Para la contraseña 
        self.password = page.locator("#password")
        
        # Para el botón de enviar 
        self.submit_button = page.locator("#btnEnviar")

        self.error_message = page.locator("#mensajeError")

    def navigate(self):
        self.page.goto("http://localhost:8080/pages/auth/login-desktop-claro.html")

    def check_title(self):
        expect(self.page).to_have_title("Iniciar sesion")

    def login_exitoso(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()

        expect(self.error_message).not_to_be_visible()


    def login_fallido(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()

        expect(self.error_message).to_be_visible()

