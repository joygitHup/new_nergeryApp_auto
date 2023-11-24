from test.test_login_moudle.test_login import Test_login
class Test_my(Test_login):
    '''我的模块'''
    def test_check_accountinfor(self):
        '''检查账户信息'''
        print("检查账户信息")
    def test_check_myaccountinfo(self):
        '''检查我的信息'''
        print("我的信息")
    def test_chang_phone(self):
        '''更改手机号'''
        print("更改手机号")
    def test_check_updata(self):
        '''检查更新'''
        print("检查更新")