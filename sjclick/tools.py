import datetime
import webbrowser

import dearpygui.dearpygui as dpg
import pytz

tw = pytz.utc


def str_ts(ts):
    return datetime.datetime.strftime(datetime.datetime.fromtimestamp(ts / 10 ** 9, tz=tw), "%Y/%m/%d %H:%M:%S.%f")


def date_range(query_date="None"):
    today = query_date if query_date else datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
    start = int(datetime.datetime.strptime(f"{today} 09:00:00+0000", "%Y-%m-%d %H:%M:%S%z").timestamp())
    end = int(datetime.datetime.strptime(f"{today} 13:30:00+0000", "%Y-%m-%d %H:%M:%S%z").timestamp())
    return start, end


def add_and_load_image(dpg, image_path, parent=None):
    if dpg.load_image(image_path) is None:
        return

    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id)
    else:
        return dpg.add_image(texture_id, parent=parent)


def _hyperlink(text, address):
    b = dpg.add_button(label=text, callback=lambda: webbrowser.open(address))
    dpg.bind_item_theme(b, f"__{text}_hyperlinkTheme")
