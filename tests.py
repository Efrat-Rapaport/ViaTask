import requests
import json
import config
import time

def sign_in():
    btn_sign_in=config.driver.find_element(config.By.ID,"signin2")
    btn_sign_in.click()
    text_name = config.driver.find_element(config.By.ID, "sign-username")
    time.sleep(2)
    text_name.send_keys(config.user_name)
    text_pass = config.driver.find_element(config.By.ID, "sign-password")
    time.sleep(2)
    text_pass.send_keys(config.password)
    text_pass.submit()
    # print("succses sign in")

def login():
    btn_login=config.driver.find_element(config.By.ID,"login2")
    btn_login.click()
    text_name=config.driver.find_element(config.By.ID,"loginusername")
    time.sleep(2)
    text_name.send_keys(config.user_name)
    text_pass=config.driver.find_element(config.By.ID,"loginpassword")
    time.sleep(2)
    text_pass.send_keys(config.password)
    text_pass.submit()
    # print("succses log in")

def add_to_cart():
    elem=config.driver.find_element(config.By.CLASS_NAME,"nav-link")
    elem.click()
    time.sleep(2)
    nex_link=config.driver.find_element(config.By.LINK_TEXT,"Nexus 6")
    nex_link.click()
    time.sleep(2)
    nex_btn=config.driver.find_element(config.By.LINK_TEXT,"Add to cart")
    nex_btn.click()
    # print("add nex to cart success")

def navigate_to_cart():
    btn_cart = config.driver.find_element(config.By.ID, "cartur")
    btn_cart.click()
    time.sleep(2)

def test_num_products():
    time.sleep(5)
    cart=config.driver.find_elements(config.By.CLASS_NAME,"success")
    if len(cart)==1:
        # print("1 product in cart")
        return True
    # print("more or less then 1 product in cart")
    return False


def test_title():
    product=config.driver.find_elements(config.By.TAG_NAME,"td")
    if product[1].text!="Nexus 6":
        # print("title is not	Nexus 6")
        return  False
    # print("title is Nexus 6")
    return True


def test_price():
    product=config.driver.find_elements(config.By.TAG_NAME,"td")
    if product[2].text!="650":
        # print("price is not 650")
        return False
    # print("price is  650")
    return True

def test_id():
    data={"id":3}
    response = requests.post('https://api.demoblaze.com/view',json=data)
    res=response.content
    res=res.decode("utf-8")
    res_json=json.loads(res)
    id=res_json['id']
    if id==3:
        return True
    return False

def final_test():
    num_product=test_num_products()
    title=test_title()
    price=test_price()
    id=test_id()
    if id and price and title and num_product:
        print("true")
        return True
    print("false")
    return False







