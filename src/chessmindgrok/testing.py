import os.path
import chessmindgrok
from zope.app.testing.functional import ZCMLLayer

ftesting_zcml = os.path.join(
    os.path.dirname(chessmindgrok.__file__), 'ftesting.zcml')
FunctionalLayer = ZCMLLayer(ftesting_zcml, __name__, 'FunctionalLayer')
