from playwright.sync_api import sync_playwright, expect

def test_wrong_email_or_password_authorization():

    with sync_playwright() as playwright:
        # Открываем браузер и создаем новую страницу
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Переходим на страницу входа
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Заполняем поле email
        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.abaran@mail.ru')

        # Заполняем поле пароль
        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill('Password')

        # Нажимаем на кнопку Login
        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        # Проверяем, что появилось сообщение об ошибке
        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

        # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
        page.wait_for_timeout(5000)