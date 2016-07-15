# -*- coding:utf-8 -*-
'''
    OsziCar类单元测试.
'''
import unittest

import numpy as np
import matplotlib
matplotlib.use('Agg')

from vaspy.iter import OsziCar


class OsziCarTest(unittest.TestCase):

    def setUp(self):
        #create an instance of OSZICAR file
        self.maxDiff = True

    def test_attrs(self):
        "Make sure load() effects"
        oszicar = OsziCar('./testdata/OSZICAR') 
        for var in oszicar.vars:
            self.assertTrue(hasattr(oszicar, var))

        #should raise an exception for an AttributeError
        self.assertRaises(AttributeError)

    def test_esort(self):
        "Make sure the esort() effects"
        oszicar = OsziCar('./testdata/OSZICAR') 
        srted = oszicar.esort('E0', 2)
        shouldbe = np.array([(-101.21186, 326), (-101.21116, 324)],
                            dtype=[('var', '<f8'), ('step', '<i4')])
        self.assertTrue((srted == shouldbe).all())

    def test_plot(self):
        "Make sure object could plot"
        oszicar = OsziCar('./testdata/OSZICAR') 
        plot = oszicar.plot('E0', mode='save')
        self.assertTrue(isinstance(plot, matplotlib.figure.Figure))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OsziCarTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

