import unittest
from tkinter import Tk
from io import StringIO
import sys

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        # إعداد نافذة Tkinter لاختبار الكود
        self.root = Tk()
        self.converter = Converter(self.root)

    def test_conversion(self):
        # اختبار التحويل من الدولار الأمريكي إلى اليورو
        self.converter.qyma.set("100")
        self.converter.urrnsy.set("usd")
        self.converter.convert()
        self.assertEqual(self.converter.value.get(), "85.00")

    def test_invalid_input(self):
        # اختبار إدخال غير صالح
        self.converter.qyma.set("invalid")
        self.converter.urrnsy.set("usd")
        self.converter.convert()
        self.assertEqual(self.converter.value.get(), "Invalid Input")

    def tearDown(self):
        self.root.quit()

if __name__ == "__main__":
    unittest.main()
