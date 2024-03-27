import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

@st.cache(allow_output_mutation=True)
def get_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    return webdriver.Chrome(
        executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),
        options=options,
    )

# Prompt the user to enter a URL
url = st.text_input("Enter the URL:")
if url:
    # Get the webdriver instance
    driver = get_driver()
    driver.get(url)

    # Display the page source
    st.code(driver.page_source)
else:
    st.warning("Please enter a URL.")
