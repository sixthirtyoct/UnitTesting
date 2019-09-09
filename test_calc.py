import unittest
import maincode


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is a setUpClass(camelcase). It will be executed only once in the start.")

    @classmethod
    def tearDownClass(cls):
        print("This is a tearDownClass(camelcase). It will be executed only once in the end.")

    def setUP(self):
        print("This is a setUp method which runs everytime before test method. Not required here tho!")

    def tearDown(self):
        print("Runs after end of every test method. Used to destroy objects if created any.")

    # Test Methods
    def test_add(self):
        self.assertEqual(maincode.add(10,2),12)
        self.assertEqual(maincode.add(0,0),0)
        self.assertEqual(maincode.add(1,-2),-1)
        #self.assertEqual(maincode.add(100000000,20000000000000000000000000000),0) #Will fail this

    def test_mul(self):
        self.assertEqual(maincode.multiply(10,2),20)
        self.assertEqual(maincode.multiply(-1,-2),2)

    def test_div(self):
        self.assertEqual(maincode.divide(10,2),5)
        self.assertEqual(maincode.divide(-1,-2),0.5)
        with self.assertRaises(ValueError):
            maincode.divide(4,0)






if __name__ == "__main__":
    unittest.main()
