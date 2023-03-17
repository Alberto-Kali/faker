from selenium import webdriver
from fake_useragent import UserAgent

print("Default 'Lib' location in 'C:/Users/[user]/AppData/Local/Programs/Python/Python[version]'")
libs = str(input("Python 'Lib' folder path: "))
agent = str(input("user-agent: "))
with open( libs + "/Lib/site-packages/fake_useragent/data/browsers.json", "w") as f:
    f.write(str("""{"chrome": [" """ + str(agent) + """ "]}"""))
useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.chrome)
driver = webdriver.Firefox(firefox_profile=profile, executable_path="geckodriver.exe")
driver.get("http://www.whatsmyua.info/")
