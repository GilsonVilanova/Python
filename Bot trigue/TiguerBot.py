from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:  
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://hhbet34.com/")  # Replace with the actual URL of Tiguer
    
    page.getByRole('textbox', { name: 'Digite o Número do Celular/E-' })
    time.sleep(10)  # Wait for a while to see the page (optional)
    browser.close()