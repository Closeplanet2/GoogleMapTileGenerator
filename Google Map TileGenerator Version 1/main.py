from Controller.WebsiteController import SeliumWebsiteController
from Controller.GUIController import ControlWindow
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab
import os
import time

#51.58334300000001_-3.346142699999999

class NewGoogleMaps:
    def __init__(self):
        self.lat = 51.555343
        self.long = -3.377482
        self.crop = (413, 174, 1871, 1013)
        self.x_increment = 0.01567
        self.y_inrement = -0.0056
        self.seliumController = SeliumWebsiteController(full_screen=True)
        self.seliumController.ReturnWebpage("https://www.google.com/maps", use_soup=False)
        self.StartControlWindow()

    def StartControlWindow(self):
        self.control_window = ControlWindow(geometry="200x225")
        self.control_window.create_button("Pan North!", self.pan_north)
        self.control_window.create_button("Pan South!", self.pan_south)
        self.control_window.create_button("Pan East!", self.pan_east)
        self.control_window.create_button("Pan West!", self.pan_west)
        self.control_window.create_button("Take Screenshot!", self.take_screenshot)
        self.control_window.mainloop()

    def ReturnSearchQuery(self):
        return f"{self.lat}, {self.long}"

    def MoveMap(self, query):
        self.seliumController.ClearInputField(id_name="searchboxinput")
        self.seliumController.EnterInputField(query, id_name="searchboxinput")
        self.seliumController.EnterInputField(Keys.RETURN, id_name="searchboxinput")

    def pan_north(self):
        self.lat = self.lat - self.y_inrement
        self.MoveMap(self.ReturnSearchQuery())

    def pan_south(self):
        self.lat = self.lat + self.y_inrement
        self.MoveMap(self.ReturnSearchQuery())

    def pan_east(self):
        self.long = self.long + self.x_increment
        self.MoveMap(self.ReturnSearchQuery())

    def pan_west(self):
        self.long = self.long - self.x_increment
        self.MoveMap(self.ReturnSearchQuery())

    def take_screenshot(self):
        snapshot = ImageGrab.grab()
        snapshot = snapshot.crop(self.crop)
        try:
            snapshot.save(f"Images/{self.lat}_{self.long}.png")
        except:
            print("Screenshot loaded in CAD!")

googlemaps = NewGoogleMaps()





