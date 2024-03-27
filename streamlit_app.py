streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@st.cache_resource
def get_driver():
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

#driver = get_driver()
#driver.get("https://blog.talosintelligence.com/lazarus_new_rats_dlang_and_telegram/")

#st.code(driver.page_source)

url = st.text_input("Enter the URL:")
if url:
    driver = get_driver()
    driver.get(url)
    st.code(driver.page_source)
