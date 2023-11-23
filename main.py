import time
import unittest
import pytest
from config import config
from config.config import test_all_path, REPORT_SAVE_PATH
def creat_suite():
   suiteTest_defaultTestLoader = unittest.defaultTestLoader.discover(start_dir=test_all_path, pattern='test_*.py',
                                                                     top_level_dir=None)
   return suiteTest_defaultTestLoader
suite = creat_suite()

if  __name__=="__main__":
    pytest.main([r'--alluredir={}'.format(REPORT_SAVE_PATH)])
