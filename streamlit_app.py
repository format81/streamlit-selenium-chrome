import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

#@st.cache_resource
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

driver = get_driver()

# Add a title to the Streamlit app
st.title("SnapShotter: Instant Website Screenshots with Selenium")

#st.code(driver.page_source)

url = st.text_input("Enter the URL:")
if st.button("Take Screenshot"):  # Add a button to start the scraping process
    if url:
        try:
            driver.get(url)
            screenshot_path = "screenshot.png"  # define your path where screenshot will be saved
            driver.save_screenshot(screenshot_path)
            st.image(screenshot_path)  # Display the screenshot in the Streamlit app
        except (TimeoutException, WebDriverException) as e:
            st.error(f"An error occurred: {str(e)}")
            st.warning("The website might be down, not allowing scraping, or the URL could be incorrect.")
    else:
        st.warning("Please enter a URL.")
