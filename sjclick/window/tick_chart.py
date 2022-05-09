from sjclick import configs
from sjclick.tools import str_ts, date_range


class TickChart:
    def __init__(self, dpg, hub, stock_symbol):
        from sjclick.hub import SJHub
        # from dearpygui import _dearpygui as dpg
        self.dpg = dpg
        self.hub: SJHub = hub
        self.stock_symbol: str = stock_symbol
        self.tag = dpg.generate_uuid()
        self._data = {}

        self.create_tick_chart_window()

    def create_tick_chart_window(self):
        # view trade window
        with self.dpg.window(tag=self.tag,
                             label=configs.TICK_CHART_WINDOW_TEXT,
                             width=configs.TICK_CHART_WINDOW_SIZE[0],
                             height=configs.TICK_CHART_WINDOW_SIZE[1],
                             on_close=self.cleanup_alias):
            self.create_tick_chart_window_items()

    def create_tick_chart_window_items(self):
        # data
        self._data['contract'] = self.hub.contract(self.stock_symbol)
        self._data['codename'] = f"{self._data['contract'].code} {self._data['contract'].name}"
        self._data['ticks'] = self.hub.ticks(self.stock_symbol)
        self._data['snapshot'] = self.hub.snapshot(self.stock_symbol)

        data = self._data['snapshot'][0]

        with self.dpg.group(horizontal=True):
            self.dpg.add_spacer(width=configs.TICK_CHART_SPACERX)
            self.dpg.add_text(self._data['contract'].code)
            self.dpg.add_text(self._data['contract'].name)
            self.dpg.add_text(str_ts(data.ts))

        with self.dpg.group(horizontal=True):
            self.dpg.add_spacer(width=configs.TICK_CHART_SPACERX)
            close = self.dpg.add_text(data.close)
            with self.dpg.group():
                self.dpg.add_text("買進")
                self.dpg.add_text("賣出")
            with self.dpg.group():
                self.dpg.add_text(data.buy_price)
                self.dpg.add_text(data.sell_price)
            if data.change_type == 'Down':
                self.dpg.bind_item_theme(close, configs.GREEN_TEXT_COLOR_THEME_ID)
            elif data.change_type == 'Up':
                self.dpg.bind_item_theme(close, configs.RED_TEXT_COLOR_THEME_ID)
            else:
                self.dpg.bind_item_theme(close, configs.FLAT_TEXT_COLOR_THEME_ID)

        with self.dpg.group(horizontal=True):
            with self.dpg.plot(label="Stock Prices", height=350, width=-1, no_title=True):
                # self.dpg.add_plot_legend()
                xaxis = self.dpg.add_plot_axis(self.dpg.mvXAxis, time=True)
                start, end = date_range(self._data['contract'].update_date.replace('/', '-'))
                self.dpg.set_axis_limits(self.dpg.last_item(), start, end)

                with self.dpg.plot_axis(self.dpg.mvYAxis, tag=f"{self.tag}_yaxis") as yaxis:
                    self.dpg.add_hline_series([self._data['contract'].limit_up, self._data['contract'].reference,
                                               self._data['contract'].limit_down])

                    ts = [ts / 10 ** 9 for ts in self._data['ticks'].ts]
                    self.dpg.add_line_series(ts, self._data['ticks'].close,
                                             label=self._data['codename'])
                    self.dpg.set_axis_limits(yaxis, self._data['contract'].limit_down * 0.995,
                                             self._data['contract'].limit_up * 1.005)

                self.dpg.fit_axis_data(xaxis)
        with self.dpg.group(horizontal=True):
            self.dpg.add_checkbox(label="震幅範圍", default_value=False, callback=self.range_callback)

    def range_callback(self, sender, keyword, value):
        value = self.dpg.get_value(sender)
        data = self._data['snapshot'][0]
        if value:
            self.dpg.set_axis_limits(f"{self.tag}_yaxis", data.low, data.high)
        else:
            self.dpg.set_axis_limits(f"{self.tag}_yaxis", self._data['contract'].limit_down * 0.995,
                                     self._data['contract'].limit_up * 1.005)

    def cleanup_alias(self):
        pass
