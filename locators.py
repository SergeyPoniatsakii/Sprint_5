from selenium.webdriver.common.by import By

class Locators:

# Главная страница - войти в аккаунт
    LOGIN_ACC_BTN = (By.CSS_SELECTOR, ".button_button__33qZ0")

# Главная страница - войти в личный кабинет
    PERSONAL_ACCOUNT_BTN = (By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX[href='/account']")

# Вход - поле ввода Email
    LOGIN_EMAIL_FLD = (By.XPATH, "//input[@name='name']")

# Вход - поле ввода пароля
    LOGIN_PASSWORD_FLD = (By.XPATH, "//input[@name='Пароль']")

# Вход - кнопка Войти
    LOGIN_BTN = (By.CSS_SELECTOR, ".button_button__33qZ0")

# Вход - Кнопка Зарегистрироваться
    LOGIN_REGISTRATION_BTN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/register']")

# Вход - Кнопка Восстановить пароль
    LOGIN_FORGOT_PWD_BTN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/forgot-password']")

# Регистрация - поле ввода Имя
    REGISTRATION_NAME_FLD = (By.XPATH, "//label[text()='Имя']/../input")

# Регистрация - поле ввода Email
    REGISTRATION_EMAIL_FLD = (By.XPATH, "//label[text()='Email']/../input")

# Регистрация - поле ввода пароля
    REGISTRATION_PASSWORD_FLD = (By.XPATH, "//input[@name='Пароль']")

# Регистрация - кнопка Зарегистрироваться
    REGISTRATION_SUBMIT_BTN = (By.CSS_SELECTOR, ".button_button__33qZ0")

# Регистрация - кнопка Войти
    LOGIN_LOGIN_BTN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/login']")

# Восстановление пароля- поле ввода Email
    FORGOT_EMAIL_FLD = (By.XPATH, "//input[@name='name']")

# Восстановление пароля- кнопка Восстановить
    FORGOT_SUBMIT_BTN = (By.CSS_SELECTOR, ".button_button__33qZ0")

# Восстановление пароля- кнопка Войти
    FORGOT_LOGIN_BTN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/login']")

# Личный кабинет - кнопка Конструктор
    ACCOUNT_CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")

# Личный кабинет - кнопка Логотип
    ACCOUNT_LOGO_BTN = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

# Личный кабинет - кнопка Выход
    ACCOUNT_LOGOUT_BTN = (By.CSS_SELECTOR, ".Account_button__14Yp3")

# Конструктор - кнопка Булки
    CONSTRUCTOR_BAKE_BTN = (By.XPATH, "//span[text()='Булки']")

# Конструктор - кнопка Соусы
    CONSTRUCTOR_SOUS_BTN = (By.XPATH, "//span[text()='Соусы']")

# Конструктор - кнопка Начинки
    CONSTRUCTOR_TOPPINGS_BTN = (By.XPATH, "//span[text()='Начинки']")

# Конструктор - кнопка Булки активна
    CONSTRUCTOR_BAKE_BTN_ACT = (By.XPATH,
"//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']")

# Конструктор - кнопка Соусы активна
    CONSTRUCTOR_SOUS_BTN_ACT = (By.XPATH,
"//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']")

# Конструктор - кнопка Начинки активна
    CONSTRUCTOR_TOPPINGS_BTN_ACT = (By.XPATH,
"//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']")

# Конструктор - Флюоресцентная булка
    R2_D2 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")

# Конструктор - Соус Spicy-X
    SPICY_X = (By.XPATH, "//p[text()='Соус Spicy-X']")

# Конструктор - Мясо бессмертных моллюсков Protostomia
    PROTOSTOMIA = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")

# Регистрация - некорректный пароль
    UNFORMATTED_PWD = (By.XPATH, "//p[text()='Некорректный пароль']")

# Конструктор -  Соберите бургер
    ASSEMBLE_A_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")




