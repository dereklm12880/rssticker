import unittest
from unittest.mock import patch, MagicMock
import webbrowser
import os, sys
sys.path.append("../")
from RSS.view import userinterface as ui

class TestPopup(unittest.TestCase):
    def setUp(self):
        self.view = ui.RSSticker()
    
    #def test_loop(self):
        #with patch(ui.RSSticker) as self.mock_method:
            #call = self.mock_method.loop()
            #while (call.assert_called()):
                #pass
                
if __name__ == "__main__":
    unittest.main()
