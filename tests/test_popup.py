import unittest
from unittest.mock import patch, MagicMock
import webbrowser
import os
from RSS.view.userinterface import RSSticker

class TestPopup(unittest.TestCase):
    def setUp(self):
        self.view = RSSticker()

    def test_loop(self):
        with patch.object(RSSticker,'method') as mock_method:
            view = self.view.loop("""root.update() or root.mainloop()?""")