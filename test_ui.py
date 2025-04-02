# test_ui.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_add_widget():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://demo.reportportal.io/ui/#login")
        
        # Ожидание и ввод логина (новые локаторы)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
        ).send_keys("default")
        
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("1q2w3e")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Ожидание загрузки dashboard
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sidebarContainer"))
        )
        
        # Переход на страницу dashboard
        driver.get("https://demo.reportportal.io/ui/#default_personal/dashboard")
        
        # Добавление виджета (новые локаторы)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-widget-button']"))
        ).click()
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Task Progress')]"))
        ).click()
        
        # Проверка
        assert WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='task-progress-widget']"))
        ).is_displayed()
        
    finally:
        driver.quit()