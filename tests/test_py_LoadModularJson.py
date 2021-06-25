import sys
sys.path.append('../')

import unittest
from pyLoadModularJson import loadModularJson



cfgFile = 'cfgFiles/delta.json'



cfgExpected = {'param2b': 22,
               'nestedParam2b': {'a': ['a', 'list']},
               'common2b2cparam': 'b',
               'nestedParam2c': {'astr': 'this is new'},
               'param2a': 2,
               'configBase': 'base1.json',
               'nestedParam1': {'a': 3, 'b': ['c', 'd'], 'c': 'base1_added'},
               'nestedParam2a': {'a': 'notaNumber'},
               'param1': 2,
               'alternativeBaseStr': 'base2c.json'}


cfgAltExpected = {'param2b': 98, 
          'nestedParam2b': {'a': -12.2}, 
          'common2b2cparam': 'c', 
          'nestedParam2c': {'astr': 'this is new'}, 
          'param1': 2, 
          'alternativeBaseStr': 'base2c.json', 
          'configBase': 'base1.json', 
          'nestedParam1': {'a': 3, 'b': ['c', 'd']}} 

class TestLoadConfig(unittest.TestCase):

    def testLoadConfig(self):
        

        cfg = loadModularJson(cfgFile)
        self.assertTrue(cfg==cfgExpected,'Expected the parsed config to look like\n{}\n,not\n{}'.format(cfgExpected,cfg))


    def testLoadConfigAltTag(self):
        cfgAlt = loadModularJson(cfgFile,baseTag='alternativeBaseStr')
        self.assertTrue(cfgAlt==cfgAltExpected,'Expected the parsed config with alt string to look like\n{}\n,not\n{}'.format(cfgAltExpected,cfgAlt))



if __name__ == "__main__":
    unittest.main()
