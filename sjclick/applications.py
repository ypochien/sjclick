import dearpygui.dearpygui as dpg

from sjclick import configs
from sjclick import window


def create_dpg_fonts():
    with dpg.font_registry():
        with dpg.font(configs.CHINESE_FONT_PATH, size=16, tag=configs.DEFAULT_FONT_THEME_ID, default_font=True) as font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x10000, 0x100FF)
        dpg.bind_font(font)
        dpg.bind_font(configs.DEFAULT_FONT_THEME_ID)


def create_dpg_themes():
    # default theme
    with dpg.theme(tag=configs.DEFAULT_THEME_ID):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 12, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (0, 95, 115), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 95, 115), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (0, 95, 115), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (0, 95, 115), category=dpg.mvThemeCat_Core)

    with dpg.theme(tag=configs.GREEN_TEXT_COLOR_THEME_ID):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (163, 239, 97), category=dpg.mvThemeCat_Core)

    with dpg.theme(tag=configs.RED_TEXT_COLOR_THEME_ID):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (242, 65, 65), category=dpg.mvThemeCat_Core)

    with dpg.theme(tag=configs.FLAT_TEXT_COLOR_THEME_ID):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (240, 200, 65), category=dpg.mvThemeCat_Core)

    # login theme
    with dpg.theme(tag=configs.LOGIN_THEME_ID):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 15, 7, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 7, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 20, 20, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 17, category=dpg.mvThemeCat_Core)

    dpg.bind_theme(configs.DEFAULT_THEME_ID)


class SjClick:
    @staticmethod
    def run():
        dpg.create_context()
        dpg.create_viewport(title=configs.SJCLICK_VIEWPORT_TITLE,
                            width=configs.SJCLICK_WINDOW_VIEWPORT_SIZE[0],
                            height=configs.SJCLICK_WINDOW_VIEWPORT_SIZE[1])
        dpg.setup_dearpygui()
        dpg.set_global_font_scale(configs.FONT_SCALE)
        dpg.set_viewport_small_icon(configs.SMALL_VIEWPORT_ICON_PATH)

        create_dpg_fonts()

        create_dpg_themes()

        window.loading.launch_loading()
        window.login.Login(dpg)
        dpg.show_metrics()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
