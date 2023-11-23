import time
import warnings
import allure
from appium import webdriver


from appium.webdriver.webelement import By
import  pytest

from test.base_dirver_class import driver_base_class
class Test_login(driver_base_class):
  """登录模块的测试用例"""
  @pytest.mark.parametrize('accountValue,passwordValue',[("xny123456",'xny123456')])
  def test_login_correct_infor(self,accountValue,passwordValue):
    '''正确的用户信息 密码和账户'''
    xpth1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.widget.EditText"
    time.sleep(2)
    account =self.driver.find_element(by=By.XPATH, value=xpth1)
    account.send_keys(accountValue)
    xpath2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[1]/android.widget.EditText"
    password = self.driver.find_element(by=By.XPATH, value=xpath2)
    password.send_keys(passwordValue)
    time.sleep(2)
    xpath3 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button"
    log_buton = self.driver.find_element(by=By.XPATH, value=xpath3)
    time.sleep(2)
    log_buton.click()
    time.sleep(2)
    business_entry = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.Image"
    business_entry_click =self.driver.find_element(by=By.XPATH, value=business_entry)
    time.sleep(2)
    business_entry_click.click()
  # @pytest.mark.skip(reason="直接跳过")
  @pytest.mark.uat
  def  test_login_correct_username(self):
    '''正确的用户名 错误的密码'''
    pass
  # @pytest.mark.skip(reason="直接跳过")
  @pytest.mark.smok
  def test_login_correct_password(self):
    '''正确的用户名 错误的密码'''
    pass
  @pytest.mark.xfail(reason="标记这个用例为失败用例")
  def test_login_correct_loginFaiul(self):
    pass

if __name__=="__main__":
   pytest.main()


