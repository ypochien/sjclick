import shioaji

from sjclick import configs
from sjclick.window.tick_chart import TickChart


class SJHub:
    def __init__(self, dpg, api=None):
        self.dpg = dpg
        self.api: shioaji.Shioaji = api
        self.tags = []
        self.create_sjhub()

    def apply_theme(self):
        self.dpg.bind_item_theme(configs.SJHUB_WINDOW_ID, configs.SJHUB_THEME_ID)

    def create_sjhub(self):
        with self.dpg.window(tag=configs.SJHUB_WINDOW_ID,
                             label=configs.SJHUB_WINDOW_TEXT,
                             width=configs.SJCLICK_WINDOW_VIEWPORT_SIZE[0],
                             height=configs.SJCLICK_WINDOW_VIEWPORT_SIZE[1],
                             no_resize=True):
            self.apply_theme()
            self.dpg.set_primary_window(configs.SJHUB_WINDOW_ID, True)
            self.create_sjhub_menu()
            self.create_sjhub_items()

    def create_sjhub_items(self):
        # profit, win-rate, news and add new trade button
        # self.dpg.add_spacer(height=configs.SJHUB_PROFIT_WINRATE_GROUP_SPACERX)
        with self.dpg.group(horizontal=True,
                            parent=configs.SJHUB_WINDOW_ID):
            with self.dpg.group(tag=configs.SJHUB_GROUP_ID):
                self.dpg.add_input_text(tag=configs.SJHUB_INPUT_CODE_ID, on_enter=True,
                                        callback=self.input_code_callback)

    def create_sjhub_menu(self):
        # menu bar
        with self.dpg.menu_bar(label=configs.SJHUB_MENU_SYSTEM_TEXT):
            # logout menu choice
            self.dpg.add_menu_item(label=configs.SJHUB_MENU_LOGOUT_TEXT,
                                   callback=self.logout_menu_callback)

            # exit app menu choice
            self.dpg.add_menu_item(label=configs.SJHUB_MENU_EXIT_TEXT,
                                   callback=self.exit_menu_callback)

    # logs the user out
    def logout_menu_callback(self):
        # close the sjhub window
        self.api.logout()
        self.close_sjhub_win()

        # display login screen
        self.dpg.show_item(configs.LOGIN_WINDOW_ID)

    # stops the program
    def exit_menu_callback(self):
        self.api.logout()
        self.dpg.stop_dearpygui()

    def close_sjhub_win(self):
        self.cleanup_alias()
        self.dpg.delete_item(configs.SJHUB_WINDOW_ID)

    def cleanup_alias(self):
        for tag in self.tags:
            if self.dpg.does_alias_exist(tag):
                self.dpg.remove_alias(tag)

    def input_code_callback(self, sender, keyword, user_data):
        if sender == configs.SJHUB_INPUT_CODE_ID:
            self.tags.append(TickChart(self.dpg, self, keyword).tag)

    def contract(self, stock_symbol):
        contract = self.api.Contracts.Stocks[stock_symbol]
        return contract

    def ticks(self, stock_symbol):
        contract = self.contract(stock_symbol)
        if contract:
            return self.api.ticks(contract, contract.update_date.replace('/', '-'))
        return None

    def snapshot(self, stock_symbol):
        contract = self.contract(stock_symbol)
        if contract:
            return self.api.snapshots([contract])
        return None
