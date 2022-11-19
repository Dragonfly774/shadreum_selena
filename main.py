import pickle
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import random

# пароль от меты должен быть один ведь я не гений
from const import password_meta_mask


def send_password_metamask(driver):
    """залетает на сайт чтоб пароль в мету ввести"""
    sleep(5)
    # нажатие на конект валлет
    driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div[2]/div[1]/button/span[1]").click()
    sleep(2)
    # переключение к окну меты
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
    try:
        # ввод пароля
        driver.find_element(By.TAG_NAME, "input").send_keys(password_meta_mask)
        sleep(1.5)
        driver.find_element(By.TAG_NAME, "button").click()
        driver.close()
        sleep(1)
        # переход назад к браузеру
        driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"Ошибка не удалось вести пароль метамаска{e}")
    sleep(1)


def mint_110(driver, url_):
    """
    https://boss.shardeum.us/#mint
    минт двух nft
    :param driver: драйвер
    :param url_: линк задания
    """
    driver.get(url_)
    try:
        # конект к сайту
        driver.find_element(By.CLASS_NAME, "connect_button").click()
    except:
        print("Ошибка конекта кошелька к сайту")

    # проверка на откртые новой вкладки и ее закрыте если она открылась
    #
    if driver.window_handles[1]:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("Зашло в if? открыласть новая вкладка при конекте кошелька")
        print("Закрыли")
    else:
        print("Новая вкладка не открылась")

    try:
        sleep(2)

        # наажатие на кнопку mint
        driver.find_element(By.CLASS_NAME, "connect_button3").click()
        print("Нажатие на минт было")

        sleep(3)
        # переход к окну меты
        driver.switch_to.window(driver.window_handles[1])
        try:
            # нажатие потверждение тразакции
            sleep(3)
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[5]/div[3]/footer/button[2]").click()
            sleep(5)

            sleep(1)
        except:
            print("не было нажатия на транзу")
        # переход назад к сайту
        driver.switch_to.window(driver.window_handles[0])
    except:
        print("Ошибка нажатия кнопик минт")
    sleep(5)


def create_collection_mint(driver, url_, nft_):
    """
    https://www.spriyo.xyz/
    задание с созданием одной nft

    :param driver: драйвер
    :param url_: линк задания
    :param nft_: номер картикни из папки imgs, название и описание картинки(это число)
    """
    # переход к сайту
    driver.get(url_)
    sleep(1)
    try:
        # нажатие на кнопку create
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div[4]/div").click()
        sleep(1)
        try:
            # нажатие на создание одной nft
            driver.find_elements(By.TAG_NAME, "img")[2].click()
            sleep(1)
            try:
                # это переменная отвечает за номер картинки, название, описание

                # вставка картинки
                driver.find_element(By.NAME, "Asset").send_keys(
                    f"C:\\Users\\roman\\OneDrive\\Рабочий стол\\проекты\\dao_proj\\Shardeum\\imgs\\{nft_}.png")

                # вставка названия
                driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[2]/div[1]/input").send_keys(
                    f'{nft_}')

                # вставка описания
                driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[2]/div[2]/textarea").send_keys(
                    f'{nft_}')

                # выбор сети
                driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[2]/div/div/div").click()
                driver.find_elements(By.TAG_NAME, "li")[2].click()

                # нажатие кнопки создания
                driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[2]/div[5]/div").click()

                # апрув метамаска
                sleep(10)
                driver.switch_to.window(driver.window_handles[1])
                sleep(3)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[5]/div[3]/footer/button[2]").click()
                sleep(3)
                driver.switch_to.window(driver.window_handles[0])
                sleep(25)

                # может вылазить окно апрува сверху серое и тут мы его убираем
                driver.find_element(By.XPATH, "/html/body/div/div[1]/div").send_keys(Keys.ENTER)
                sleep(3)
            except:
                print("не были заполнены поля создания nft")
        except:
            print("Не было нажатия на сингл креате")
    except:
        try:
            driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div[4]/div").click()
            sleep(1)
        except:
            print("Не было нажатия на кнопку креати")


def claim_domen(driver, url_):
    """
    https://nft.shardeum.us/
    клайм домена
    :param driver: драйвер
    :param url_: линк задания
    """

    driver.get(url_)
    sleep(1)
    # генерация рандомного слова
    alf = "qwertyuiopasdfghjklzxcvbnm1234567890"
    random_domen = ''.join([random.choice(alf) for i in range(8)])

    # вставка радномного слова
    driver.find_elements(By.TAG_NAME, "input")[0].send_keys(random_domen)

    # встав в record не ебу что
    driver.find_elements(By.TAG_NAME, "input")[1].send_keys("2")
    sleep(2)

    # нажатие на кнопку минт
    driver.find_element(By.TAG_NAME, "button").click()

    # апрув метамаска
    sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[5]/div[3]/footer/button[2]").click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    sleep(3)


def mint_tokens(driver, url_):
    """
    https://shardeumtest.netlify.app/
    минт токенов

    :param driver: драйвер
    :param url_: линк задания
    """
    driver.get(url_)
    sleep(1)

    # количество токенов рандомное
    amount_tokens = random.randint(1, 100)

    # вставка токенов
    driver.find_element(By.TAG_NAME, "input").send_keys(amount_tokens)
    sleep(1)

    # нажатие на минт
    driver.find_element(By.TAG_NAME, "button").click()

    # апрув метамаска
    sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[5]/div[3]/footer/button[2]").click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    sleep(3)


def ds(driver, url_, mm, token):
    """

    :param driver: драйвер
    :param url_: линк на канал на сервере шардиума для фаусета
    :param mm: адресс метамаска
    :param token: токен дс( но я его не юзаю пытался просто)
    """

    # все что серое ниже просто пытался

    # driver.get("https://discord.com/login")
    # sleep(4)
    # try:
    #     driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/section/div/div[2]/div/div/div[3]/button[1]").click()
    # except:
    #     pass
    # sleep(2)
    # try:
    #     driver.execute_script('''function login(token) {
    #                               setInterval(() => {
    #                               document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    #                               }, 50);
    #                               setTimeout(() => {
    #                               location.reload();
    #                               }, 2500);
    #                               }
    #                               login(arguments[0]);''', token)
    #     sleep(10)
    # except:
    #     print("не вошло в дс")

    # пытался с куками сделать нихуя не вышло

    # sleep(160)
    # coc = driver.get_cookies()
    # pickle.dump(coc, open(f'coc\\{1}', 'wb'))
    # print(coc)
    # sleep(2)
    # for coc in pickle.load(open(f'coc\\{1}', 'rb')):
    #     driver.add_cookie(coc)
    # sleep(5)
    # driver.refresh()

    driver.get(url_)
    sleep(5)
    # иногда выходит хуйня где надо вход нажать
    try:
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/section/div/div[2]/div/div/div[3]/button[1]").click()
    except:
        pass

    try:
        sleep(15)
        # иногда выходит хуйня где надо вход нажать
        try:
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[2]/div/div[1]/div/div/div/section/div/div[2]/div/div/div[3]/button[1]").click()
        except:
            pass

        # ввод запроса крану
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/form/div/div[1]/div/div[3]/div/div[2]/div").send_keys(
            f"/faucet")
        sleep(2)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/form/div/div[1]/div/div[3]/div/div/div/span/span/span").send_keys(
            Keys.SPACE)
        sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/form/div[1]/div[2]/div/div[2]/div/div/div/span[2]/span[2]").send_keys(
            f"{mm}")
        sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/form/div[1]/div[2]/div/div[2]/div/div/div/span[2]/span[2]").send_keys(
            Keys.ENTER)
    except:
        print("Ошибка в дс")


def main(acc_num):
    """

    :param acc_num: это число которое отвечает за номер браузера который сейчас включится
                    так же оно служит для выбора адресса меты
                    еще для выбора картинки в задании создания nft
    """

    """ссылки на тестнет"""
    lists_url = {"mint_110": "https://boss.shardeum.us/#mint",
                 "create_collection_nft": "https://www.spriyo.xyz/",
                 "claim_domen": "https://nft.shardeum.us/",
                 "swap_token": "https://dex.shardeumswap.finance/swap",
                 "mint_token": "https://shardeumtest.netlify.app/"}

    """"ссылкf на дс для faucet"""
    url_ds = "https://discord.com/channels/933959587462254612/1021737152251441244"

    """токен дс, так же просто пробовал"""
    list_ds_token = {2: ""}

    """адреса меты"""
    lists_meta = {1: "", 2: "",
                  3: "", 4: "",
                  5: "", 6: ""}


    options = Options()
    # тестовое ПО убирает
    options.add_argument("--disable-blink-features=AutomationControlled")

    """путь до файлов хрома
     в профиле стоит +2 потому что хром, который настроен для выполнения задания, имеет номер 3
     от него и идет дальше отсчет"""
    options.add_argument(
        r"--user-data-dir=C:\Users\roman\AppData\Local\Google\Chrome\User Data")  # e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
    options.add_argument(fr'--profile-directory=Profile {int(acc_num + 2)}')

    driver = webdriver.Chrome("chromedriver.exe", options=options)
    sleep(2)

    """кран в дискорде"""
    try:
        ds(driver, url_ds, lists_meta[acc_num], acc_num)
        sleep(4)
    except:
        try:
            ds(driver, url_ds, lists_meta[acc_num], acc_num)
            sleep(4)
        except:
            print("НЕ ВОШЛО В ДС")

    URL = "https://chainlist.org/chain/8081"
    driver.get(URL)

    """ввод пароля в метамаск"""
    send_password_metamask(driver)
    sleep(3)

    """задание с минтом боссов"""
    try:
        mint_110(driver, lists_url["mint_110"])
        sleep(3)
    except:
        try:
            mint_110(driver, lists_url["mint_110"])
            sleep(3)
        except:
            print("НЕ ПРОШЕЛ МИНТ NFT")

    """задания с созданием nft"""
    try:
        create_collection_mint(driver, lists_url["create_collection_nft"], acc_num)
        sleep(3)
    except:
        try:
            create_collection_mint(driver, lists_url["create_collection_nft"], acc_num)
            sleep(3)
        except:
            print("НЕ СОЗДАЛОСЬ NFT")

    """задание с созданием домена"""
    try:
        claim_domen(driver, lists_url["claim_domen"])
        sleep(3)
    except:
        try:
            claim_domen(driver, lists_url["claim_domen"])
            sleep(3)
        except:
            print("НЕ СОЗДАЛСЯ ДОМЕН")

    """задание с минотов токенов"""
    try:
        mint_tokens(driver, lists_url['mint_token'])
        sleep(3)
    except:
        try:
            mint_tokens(driver, lists_url['mint_token'])
            sleep(3)
        except:
            print("НЕ СМИНТИЛИСЬ ТОКЕНЫ")

    sleep(3)
    driver.quit()


if __name__ == '__main__':
    """в range стоит число бразеров, столько должно быть картинок и адресов меты"""
    for i in range(1, 6):
        main(i)
