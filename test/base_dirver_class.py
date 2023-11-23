import warnings
from appium import  webdriver
import  unittest
class driver_base_class():
    @classmethod
    def setup_class(cls)-> None:
     cls.desired_caps = {
      "appPackage": "plus.H5EA2E279",
      "platformName": "Android",
      "deviceName": "cb5c2f8f",
      "appActivity": "io.dcloud.PandoraEntry",
      "skipServerInstallation": "false"
     }
     with warnings.catch_warnings():
       warnings.filterwarnings("ignore", category=DeprecationWarning)
     cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)  # 启动app
    @classmethod
    def teardown_class(cls)-> None:
        cls.driver.quit()





