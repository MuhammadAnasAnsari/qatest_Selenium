import unittest # unittest lib / module
from Examples import Example

class MyTestCase(unittest.TestCase):

    @classmethod   #annotation
    def setUpClass(cls):  # To setup anything or run anything before the test start
        print("This will run once before all the methods")
    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")



    def setUp(self):       # to Setup anything before every test run
        print("This will run before every method")

    def tearDown(self):    # to clear everything after every test run
        print("This will run after every method")

    def test_add(self):              # test method is used to see the test result/test run [recognized by python] if use check_add() it gives "empty suite ran 0 test..."
        result= Example.add(self,10,20)
        self.assertEqual(result,30)
        self.assertEqual(Example.add(self, 0, 3), 3)
        self.assertEqual(Example.add(self, -10, 3), -7)
        self.assertEqual(Example.add(self, 200, 400), 600)

    def test_subtract(self):
        # result=Example.subtract(self,50,90)
        # self.assertEqual(result,-40)
        self.assertEqual(Example.subtract(self,90,50),40)






    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':  # Use to run the test from command line
    unittest.main()
