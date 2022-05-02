import shioaji as sj
from .config import *
from .window import login_window


class SjClick():
    def __init__(self):
        self.init_dpg()
    
    def init_dpg(self):               
        def init_font():
            with dpg.font_registry():
                with dpg.font("font/Creative.ttc", 20 ,default_font=True) as font:
                    dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
                    dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
                    dpg.add_font_range(0x10000, 0x100ff)
                    dpg.bind_font(font)      
                # with dpg.font("font/unifont_upper.ttf", 20 ,default_font=False) as font:
                    # dpg.bind_font(font)

        
        dpg.create_context()
        dpg.create_viewport()
        dpg.setup_dearpygui()
        dpg.show_metrics()

        # init_font()



        login_window()

    def run(self):
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
        

