import pytest
import shutil
import os
from fm import utils


class TestUtil():
    def test_createDir(self):
        testDir = '/tmp/test_dir'
        utils.createDir(testDir)
        assert True == os.path.exists(testDir)
        shutil.rmtree(testDir)

    def test_fileExists(self):
        fileName = '/tmp/test_fileExists'
        with open(fileName, 'w') as f:
            f.write('Test %s' % fileName)
        assert os.path.isfile(fileName) == utils.fileExists(fileName)
        utils.silentRemove(fileName)

    def test_touchFile(self):
        fileName = '/tmp/test_touched'
        utils.touchFile(fileName)
        assert True == utils.fileExists(fileName)
        utils.silentRemove(fileName)
