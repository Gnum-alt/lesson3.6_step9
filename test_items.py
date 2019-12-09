from selenium import webdriver
import time
import pytest


def test_contains_add_button_to_cart(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert button > 0, 'Кнопки "добавить в корзину" нет'