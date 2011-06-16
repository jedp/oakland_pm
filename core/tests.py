from django.utils import unittest
from core.models import *

class ModelsTestCase(unittest.TestCase):
    pass

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelsTestCase)
    return suite

