from playwright.sync_api import Page, expect    
from pages.login_page import LoginPage

def test_ejercicios_1_2(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.check_title()


def test_ejercicios_3_4(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.check_title()
    login_page.login_exitoso("gaston_test", "Contraseña1")


def test_ejercicios_5_6(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.check_title()
    login_page.login_fallido("gaston_test", "Contraseña12")


def test_ejercicios_7_8(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.check_title()
    login_page.login_exitoso("gaston_test", "Contraseña1")
    page.screenshot(path="evidencias/captura_1.png", full_page=True)
    page.go_back()
    page.screenshot(path="evidencias/captura_2.png", full_page=True)