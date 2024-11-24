import unittest
from com_kalynx_robotuiwrapper.robotuiwrapper import RobotUIWrapper # type: ignore
class TestRobotUiWrapper(unittest.TestCase):

    _sut: RobotUIWrapper = RobotUIWrapper("localhost", 7442)
    def test_set_display_by_id(self):
        self._sut.set_display_by_id(1)
    
    def test_set_primary_display_reference(self):
        self._sut.set_primary_display_reference("Hello")

    def test_move_mouse_to(self):
        self._sut.move_mouse_to(x=100,y=100)

    def test_mouse_position(self):
        val = self._sut.get_mouse_position()
        self.assertIn("x", val.keys())
        self.assertIn("y", val.keys())
 
if __name__ == '__main__':
    unittest.main() 