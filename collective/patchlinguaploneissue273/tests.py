import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ztc.installProduct('CacheSetup')
ztc.installProduct('CMFSquidTool')


ptc.installProduct('LinguaPlone')

ptc.setupPloneSite(products=['CacheSetup', 'LinguaPlone'],
                   extension_profiles=[])

import collective.patchlinguaploneissue273


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            
            ztc.installPackage(collective.patchlinguaploneissue273)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass

    def pdb(self, *args):
        import pdb;pdb.set_trace();


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='collective.patchlinguaploneissue273',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='collective.patchlinguaploneissue273.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='collective.patchlinguaploneissue273',
        #    test_class=TestCase),

        ztc.FunctionalDocFileSuite(
            'README.txt', package='collective.patchlinguaploneissue273',
            test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
