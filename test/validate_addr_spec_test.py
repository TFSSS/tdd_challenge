import unittest
from validate_addr_spec import ValidateAddrSpec
import io

class ValidateAddrSpecTest(unittest.TestCase):
    def testCreate(self):
        self.lineText(".","ng")
        self.lineText("@","ng")
        self.lineText("bc@","ng")
        self.lineText("bc@example.commmm","ng")
        self.lineText("@example.commmm","ng")
        self.lineText("example@com","ng")
        self.lineText("example@com.","ng")
        self.lineText(".@example.com","ok")
        self.lineText("a.@example.com","ok")
        self.lineText("a.@example.com","ok")

        self.lineText("bc@example.com","ok")

    def lineText(self, txt, expecttxt):
        outputtxt = io.StringIO()
        iotext = io.StringIO(txt)
        emailTest = ValidateAddrSpec(iotext,outputtxt)
        emailTest.outputtxt()
        self.assertEqual(emailTest.outputtxt.getvalue(), expecttxt)