#https://stackoverflow.com/questions/7206807/whats-the-recommended-way-to-unittest-python-gui-applications
#http://unpythonic.blogspot.com/2007/03/unit-testing-pygtk.html

import unittest
import time
import gtk
from unittest.mock import MagicMock
from unittest.mock import patch
sys.path.append("../")
from Rss.view import viewfile


class test_Gui(unittest.TestCase):
      """Automatically called to set up each test case below"""
        # do whatever you want to set things up before these test cases

    def setUp(self):
         super(MyView, self).__init__()
      self._button  = gtk.Button('Click Me')
      self._label = gtk.Label()
      self.pack_start(self._button)
      self.pack_start(self._label)
      self._count = 0
      self._button.connect('clicked', self.on_button_clicked)
      self. 
    
    def tearDown(self):
        pass
        
    def build(self):
        self.canvas= tk.canvas(root,self.x_root, self.y_root)

    def refresh(self):
       """ self.display_frame.destroy()
        self.display_frame = tk.Frame(self)
        self.display_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
        for ndex, item in enumerate(self.data):
            tk.Label(self.display_frame, text=r"Order #{} is ready for {}.".format(item[0], item[1])).grid(row=ndex, column=1)
            tk.Button(self.display_frame, text=r"Remove Ticket".format(item[0], item[1]), command=lambda x=ndex: self.remove_ticket(x)).grid(row=ndex, column=0)
 """
        self.after(6000, self.timed_refresh) #refresh after 6 seconds
          self.refresh()

if __name__ == '__main__':
    main()