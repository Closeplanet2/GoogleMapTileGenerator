from UI.GoogleMapsUI import GoogleMapsUI

class GoogleMapsController:
    def __init__(self):
        google_maps_ui = GoogleMapsUI(rs_height=False, rs_width=True)
        google_maps_ui.create_gui()
        google_maps_ui.mainloop()