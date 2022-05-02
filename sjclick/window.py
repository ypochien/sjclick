# import config
from .config import *

def login_window():
    with dpg.window(label="Shioaji"):
        # dpg.set_window_pos("Settings", 700, 0)
        dpg.add_text("登入 Shioaji")
        dpg.add_input_text(label="登入ID")
        dpg.add_input_text(label="密碼")#,password=True)
        dpg.add_button(label="登入")
        dpg.add_text("FFT Resolution")
        with dpg.group():            
            dpg.add_button()
        # dpg.add_label_text("fft_size", label="FFT Length")
        dpg.add_text("Persistance")

        # dpg.add_label_text("per_decay", label="Decay")