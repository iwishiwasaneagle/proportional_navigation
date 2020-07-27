import proportional_navigation as PN
import unittest

class TestExceptions(unittest.TestCase):
    def test_invalidPNGainInput(self):
        with self.assertRaises(PN.InvalidProportionalGainError):
            PN.PN(PN.HeadingVelocity(0,0,0,0),PN.GlobalVelocity(0,0,0,0),0)

        with self.assertRaises(TypeError):
            PN.PN(PN.HeadingVelocity(0,0,0,0),PN.GlobalVelocity(0,0,0,0),"str")

    def test_invalidHeadingVelocityBody(self):
        with self.assertRaises(TypeError):
            PN.PN("str",PN.HeadingVelocity(0,0,0,0),1)
        with self.assertRaises(TypeError):
            PN.PN(PN.HeadingVelocity(0,0,0,0),"str",1)

    def test_invalidGlobalVelocityBody(self):
        with self.assertRaises(TypeError):
            PN.PN("str",PN.GlobalVelocity(0,0,0,0),1)
        with self.assertRaises(TypeError):
            PN.PN(PN.GlobalVelocity(0,0,0,0),"str",1)
    
    def test_invalidPNOptions(self):
        with self.assertRaises(TypeError):
            PN.PN(PN.HeadingVelocity(0,0,0,0),PN.GlobalVelocity(0,0,0,0),1,options="str")

    def test_sameCoords(self):
        with self.assertRaises(PN.exceptions.OutOfBoundsRangeError):
            PN.PN(PN.HeadingVelocity(0,0,0,0),PN.GlobalVelocity(0,0,0,0)).calculate()
        

class TestPNOptions(unittest.TestCase):
    def test_optionsCreate(self):
        self.assertIsInstance(PN.PNOptions(), PN.PNOptions)
    
    def test_optionsExist(self):
        opt = PN.PNOptions(return_R=True,return_Rdot=True,return_Vc=True,return_lambda=True,return_lambdad=True)
        self.assertEqual(opt.return_R,True)
        self.assertEqual(opt.return_Rdot,True)
        self.assertEqual(opt.return_Vc,True)
        self.assertEqual(opt.return_lambda,True)
        self.assertEqual(opt.return_lambdad,True)
    
    def test_optionsWork(self):
        opt1 = PN.PNOptions(return_R=True,return_Rdot=True,return_Vc=True,return_lambda=True,return_lambdad=True)
        ret1 = PN.PN(PN.HeadingVelocity(10,1,0,0),PN.GlobalVelocity(0,10,10,0),options=opt1).calculate()
        self.assertTrue("R" in ret1.keys())
        self.assertTrue("Rdot" in ret1.keys())
        self.assertTrue("Vc" in ret1.keys())
        self.assertTrue("lambda" in ret1.keys())
        self.assertTrue("lambdad" in ret1.keys())
        self.assertTrue("nL" in ret1.keys())    

        opt2 = PN.PNOptions(return_R=True,return_Rdot=True,return_Vc=False,return_lambda=True,return_lambdad=False)
        ret2 = PN.PN(PN.HeadingVelocity(10,1,0,0),PN.GlobalVelocity(0,10,10,0),options=opt2).calculate()
        self.assertTrue("R" in ret2.keys())
        self.assertTrue("Rdot" in ret2.keys())
        self.assertFalse("Vc" in ret2.keys())
        self.assertTrue("lambda" in ret2.keys())
        self.assertFalse("lambdad" in ret2.keys())
        self.assertTrue("nL" in ret2.keys())

        ret3 = PN.PN(PN.HeadingVelocity(10,1,0,0),PN.GlobalVelocity(0,10,10,0)).calculate()
        self.assertIsInstance(ret3,float)

if __name__ == '__main__':
    unittest.main()