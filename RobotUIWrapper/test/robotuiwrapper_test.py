import unittest
from com_kalynx_robotuiwrapper.robotuiwrapper import RobotUIWrapper
class TestRobotUiWrapper(unittest.TestCase):

    def test_set_display_by_id(self):
        wrapper: RobotUIWrapper = RobotUIWrapper("localhost", 7442)
        wrapper.set_display_by_id(1)

if __name__ == '__main__':
    unittest.main()