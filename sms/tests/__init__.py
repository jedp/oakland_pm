from settings import PROJECT_ROOT
from django.utils import unittest
import os
import re

test_file_pat = re.compile('(test_.*)\.py$')

def suite():
    """
    Build a suite from all test files in this dir
    """

    # convert our file path to a module hierarchy for import
    import_path = re.split(PROJECT_ROOT, os.path.dirname(__file__))[1]
    while import_path[0] in ['/', '.']:
        import_path = import_path[1:]
    import_path = re.sub('/', '.', import_path)

    test_modules = []
    for f in os.listdir(os.path.dirname(__file__)):
        if test_file_pat.match(f):
            print "adding:", import_path+'.'+test_file_pat.search(f).groups()[0]
            test_modules.append(
                __import__(import_path+'.'+test_file_pat.search(f).groups()[0]))

    loader = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(loader, test_modules))


