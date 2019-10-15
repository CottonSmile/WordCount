import  unittest
from words import *
class Test002_Fail(unittest.TestCase):

    #测试用例前执行
    def setUp(self):
        print('Case Before')
        pass

    def tearDown(self):
        print ('Successful')
        pass

    def test_Case1(self):
        str = 'I love you'
        self.assertEqual(cal_char(str),10,'Result Fail')

    def test_Case2(self):
        str = '501dsds2222fff33300frewwwwf'
        self.assertEqual(cal_alp(str),15,'Result Fail')

    def test_Case3(self):
        str = '501dsds2222fff33300frewwwwf'
        self.assertEqual(cal_num(str), 12, 'Result Fail')

    def tese_Case4(self):
        list0 = ["i", "i", "love", "love", "you", "you"]
        l = 2
        list_test = [[i,i],[i,love],[love,love],[love,you],[you,you]]
        self.assertEqual(list_addplus(list0), list_test, 'Result Fail')

if __name__ == '__main__':
    unittest.main()
