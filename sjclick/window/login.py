import shioaji

from sjclick import configs, tools
from . import loading, dialog
from ..hub import SJHub
from ..tools import _hyperlink


class Login:
    def __init__(self, dpg):
        self.dpg = dpg
        self.api = shioaji.Shioaji()
        self.userid = None
        self.password = None
        self.create_login_win()

    def create_login_win(self):
        with self.dpg.window(tag=configs.LOGIN_WINDOW_ID,
                             width=configs.LOGIN_WINDOW_VIEWPORT_SIZE[0],
                             height=configs.LOGIN_WINDOW_VIEWPORT_SIZE[1],
                             pos=configs.LOGIN_WINDOW_POS_VALUE,
                             no_title_bar=True,
                             no_move=True,
                             no_resize=True):
            self.create_login_items()
            # self.apply_fonts()
            # self.apply_themes()

    def apply_fonts(self):
        self.dpg.bind_item_font(configs.LOGIN_HEADER_ID, configs.HEADER_FONT_THEME_ID)

    def apply_themes(self):
        self.dpg.bind_item_theme(configs.LOGIN_WINDOW_ID, configs.LOGIN_THEME_ID)

    def create_login_items(self):
        with self.dpg.group(horizontal=True):
            # logo
            tools.add_and_load_image(self.dpg, configs.SJCLICK_LOGO_PATH)

            # header text
            self.dpg.add_text(tag=configs.LOGIN_HEADER_ID,
                              default_value=configs.LOGIN_HEADER_TEXT)

        # userid input
        with self.dpg.group(horizontal=True):
            # userid field
            self.dpg.add_input_text(tag=configs.LOGIN_INPUT_USER_ID,
                                    hint=configs.LOGIN_INPUT_USERID_TEXT)

            # login button
            self.dpg.add_button(tag=configs.LOGIN_INPUT_BTN_ID,
                                label=configs.LOGIN_INPUT_BTN_TEXT,
                                callback=self.login_callback)

        # pass input
        with self.dpg.group(horizontal=True):
            self.dpg.add_input_text(tag=configs.LOGIN_INPUT_PASS_ID,
                                    hint=configs.LOGIN_INPUT_PASS_TEXT,
                                    password=True)

        with self.dpg.group(horizontal=True):
            _hyperlink("線上開戶", "https://www.sinotrade.com.tw/openact?strProd=0002&strWeb=0001")

    def login_callback(self):
        loading.show_loading()

        # enter userid and password
        self.userid = self.dpg.get_value(configs.LOGIN_INPUT_USER_ID)
        self.password = self.dpg.get_value(configs.LOGIN_INPUT_PASS_ID)
        try:
            self.api.login(self.userid, self.password)
            SJHub(self.dpg, self.api)
            self.dpg.hide_item(configs.LOGIN_WINDOW_ID)
            loading.hide_loading()

        except Exception as msg:
            loading.hide_loading()
            rtn = eval(str(msg.args[0]['response']))
            err_msg = f"{rtn['detail']} at {rtn['ip_address']}"
            dialog.Dialogs(self.dpg, err_msg, self)
            self.reset_input_fields()

    def reset_input_fields(self):
        self.dpg.set_value(configs.LOGIN_INPUT_USER_ID, "")
        self.dpg.set_value(configs.LOGIN_INPUT_PASS_ID, "")
