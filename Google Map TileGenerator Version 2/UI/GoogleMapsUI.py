from Controller.TkinterController import TkinterController
from Controller.WebsiteController import WebsiteController
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab
from tkinter import Tk, END

class GoogleMapsUI(Tk):
    def __init__(self, title="Google Maps UI", width=1600, height=900, background_color='#211717', rs_height=False, rs_width=False):
        super().__init__()
        self.tkinter_controller = TkinterController()
        self.google_maps_controller = WebsiteController(full_screen=True)
        self.google_maps_webpage = self.google_maps_controller.return_webpage("https://www.google.com/maps")

        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(width=rs_width, height=rs_height)

        self.width = width
        self.height = height
        self.crop = (413, 174, 1871, 1013)
        self.x_increment = 0.01567
        self.y_inrement = -0.0056
        self.last_screenshot = None

    def create_gui(self):
        self.tkinter_controller.place_image(self, "UI/Background/background.png", 0, 0, size=(self.width, self.height))
        self.tkinter_controller.add_button(self, "Pan North!", self.pan_north_callback, 20, 2, 100, self.height - 50)
        self.tkinter_controller.add_button(self, "Pan East!", self.pan_east_callback, 20, 2, 255, self.height - 50)
        self.tkinter_controller.add_button(self, "Pan South!", self.pan_south_callback, 20, 2, 410, self.height - 50)
        self.tkinter_controller.add_button(self, "Pan West!", self.pan_west_callback, 20, 2, 565, self.height - 50)
        self.tkinter_controller.add_button(self, "Search Long / Lat!", self.search_lat_long_callback, 20, 2, 875, self.height - 50)
        self.tkinter_controller.add_button(self, "Take Screenshot!", self.take_screenshot_callback, 20, 2, 1340, self.height - 50)

        self.long_input = self.tkinter_controller.return_entry_field("-3.377482", self.update_long_callback, 24, 720, self.height - 50)
        self.lat_input = self.tkinter_controller.return_entry_field("51.555343", self.update_lat_callback, 24, 720, self.height - 28)
        self.image_dir_input = self.tkinter_controller.return_entry_field('E:\\New Portfolio\\Python\\GoogleMapTileGenerator\\Google Map TileGenerator Version 2\\Images', self.update_image_directory_callback, 50, 1030, self.height - 50)
        self.image_name_input = self.tkinter_controller.return_entry_field("Image Name {lat} {long}", self.update_image_name_callback, 50, 1030, self.height - 28)

        self.update_gui()

    def update_gui(self):
        if not self.last_screenshot is None:
            self.tkinter_controller.place_image(self, self.last_screenshot, 0, 0, size=(int(self.width), self.height - 65))

    def pan_north_callback(self):
        try:
            lat = float(self.lat_input.get()) - self.y_inrement
            self.lat_input.delete(0, END)
            self.lat_input.insert(0, str(lat))
            self.search_lat_long_callback()
        except:
            self.lat_input.delete(0, END)
            self.lat_input.insert(0, f"Error: {self.lat_input.get()}")

    def pan_east_callback(self):
        try:
            long = float(self.long_input.get()) + self.x_increment
            self.long_input.delete(0, END)
            self.long_input.insert(0, str(long))
            self.search_lat_long_callback()
        except:
            self.long_input.delete(0, END)
            self.long_input.insert(0, f"Error: {self.long_input.get()}")

    def pan_south_callback(self):
        try:
            lat = float(self.lat_input.get()) + self.y_inrement
            self.lat_input.delete(0, END)
            self.lat_input.insert(0, str(lat))
            self.search_lat_long_callback()
        except:
            self.lat_input.delete(0, END)
            self.lat_input.insert(0, f"Error: {self.long_input.get()}")

    def pan_west_callback(self):
        try:
            long = float(self.long_input.get()) - self.x_increment
            self.long_input.delete(0, END)
            self.long_input.insert(0, str(long))
            self.search_lat_long_callback()
        except:
            self.long_input.delete(0, END)
            self.long_input.insert(0, f"Error: {self.long_input.get()}")

    def search_lat_long_callback(self):
        self.google_maps_controller.clear_element(id_name="searchboxinput")
        self.google_maps_controller.send_keys_to_element(self.return_query(), id_name="searchboxinput")
        self.google_maps_controller.send_keys_to_element(Keys.RETURN, id_name="searchboxinput")

    def take_screenshot_callback(self):
        screenshot = ImageGrab.grab()
        screenshot = screenshot.crop(self.crop)
        self.last_screenshot = self.image_dir_input.get() + f"/{self.return_image_name()}.png"
        try:
            screenshot.save(self.last_screenshot)
        except: pass
        self.update_gui()

    def update_long_callback(self, long_data):
        pass

    def update_lat_callback(self, lat_data):
        pass

    def update_image_directory_callback(self, image_dir_data):
        pass

    def update_image_name_callback(self, image_name_data):
        pass

    def return_query(self):
        print(f"{self.lat_input.get()}, {self.long_input.get()}")
        return f"{self.lat_input.get()}, {self.long_input.get()}"

    def return_image_name(self):
        image_name = self.image_name_input.get()
        return image_name.replace("{lat}", self.lat_input.get()).replace("{long}", self.long_input.get())