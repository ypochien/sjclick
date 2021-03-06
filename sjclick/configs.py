# import dearpygui.dearpygui as dpg

# desc: configs contains values that are referenced in other classes to prevent hardcode

# ids======================================================================

# #fonts
DEFAULT_FONT_THEME_ID = "Default Font"
HEADER_FONT_THEME_ID = "Header Font"

# #themes
DEFAULT_THEME_ID = "Default Theme"
RED_TEXT_COLOR_THEME_ID = "Red Text"
FLAT_TEXT_COLOR_THEME_ID = "Yellow Text"
GREEN_TEXT_COLOR_THEME_ID = "Green Text"

# #dialog
DIALOG_WINDOW_ID = "Dialog Window"
DIALOG_CONFIRMATION_BTN_ID = "Dialog Window Confirmation Button"
DIALOG_THEME_ID = "Dialog Theme"

# #loading
LOADING_WINDOW_ID = "Loading Window"

# #login
LOGIN_THEME_ID = "Login Theme"
LOGIN_HEADER_ID = "Login Header"
LOGIN_WINDOW_ID = "Login Window"
LOGIN_INPUT_USER_ID = "Login User ID"
LOGIN_INPUT_PASS_ID = "Login Password"
LOGIN_INPUT_BTN_ID = "Login Button"
LOGIN_SIMULATION_BTN_ID = "Simulation Mode"

# # sjhub
SJHUB_WINDOW_ID = "SJHub Window"
SJHUB_THEME_ID = "SJHub Theme"
SJHUB_GROUP_ID = "SHHub Group"
SJHUB_INPUT_CODE_ID = "SJHub Input Code"

# # one chart
TICK_CHART_WINDOW_ID = f"Tick Chart Window"

# value======================================================================

SMALL_VIEWPORT_ICON_PATH = "images/icons/small_sjclick_icon.ico"
SJCLICK_LOGO_PATH = "images/small_logo.png"
CHINESE_FONT_PATH = "font/jf-jinxuan-3.0-medium.otf"
SJCLICK_VIEWPORT_TITLE = "Shioaji - Click Trade!"
FONT_SCALE = 1.25

# height and width values
SJCLICK_WINDOW_VIEWPORT_SIZE = (1700, 800)

# # loading
LOADING_WINDOW_VIEWPORT_SIZE = (SJCLICK_WINDOW_VIEWPORT_SIZE[0] / 6,
                                SJCLICK_WINDOW_VIEWPORT_SIZE[1] / 6.5)

LOADING_WINDOW_CENTER_WINDOW_POS = [SJCLICK_WINDOW_VIEWPORT_SIZE[0] / 2 - LOADING_WINDOW_VIEWPORT_SIZE[0] / 2,
                                    SJCLICK_WINDOW_VIEWPORT_SIZE[1] / 2 - LOADING_WINDOW_VIEWPORT_SIZE[1] / 2]

# # login
LOGIN_WINDOW_VIEWPORT_SIZE = (SJCLICK_WINDOW_VIEWPORT_SIZE[0] / 6,
                              SJCLICK_WINDOW_VIEWPORT_SIZE[1] / 5.5)
LOGIN_WINDOW_POS_VALUE = [SJCLICK_WINDOW_VIEWPORT_SIZE[0] / 2 - LOGIN_WINDOW_VIEWPORT_SIZE[0] / 2,
                          SJCLICK_WINDOW_VIEWPORT_SIZE[1] / 2 - LOGIN_WINDOW_VIEWPORT_SIZE[1] / 1.8]

# # dialog
DIALOG_WINDOW_VIEWPORT_SIZE = (SJCLICK_WINDOW_VIEWPORT_SIZE[0] / 3,
                               SJCLICK_WINDOW_VIEWPORT_SIZE[1] / 6)
DIALOG_CENTER_WINDOW_POS = [SJCLICK_WINDOW_VIEWPORT_SIZE[0] / 2 - DIALOG_WINDOW_VIEWPORT_SIZE[0] / 2,
                            SJCLICK_WINDOW_VIEWPORT_SIZE[1] / 2 - DIALOG_WINDOW_VIEWPORT_SIZE[1] / 2]
DIALOG_MESSAGE_WRAP_COUNT = 500

# # One Chart
TICK_CHART_WINDOW_SIZE = (565, 520)

# windows Text value
# # dialog
DIALOG_CONFIRMATION_BTN_TEXT = "??????"
DIALOG_SUCCESS_TEXT = "??????"

# # loading
LOADING_TEXT = "?????????......?????????"
LOADING_WINDOW_TEXT_SPACERY = LOADING_WINDOW_VIEWPORT_SIZE[1] / 4
LOADING_WINDOW_TEXT_SPACERX = LOADING_WINDOW_VIEWPORT_SIZE[0] / 8

# # Login
LOGIN_HEADER_TEXT = "SJClick | Login"
LOGIN_FAILED_MSG_TEXT = "[ERROR] Invalid Login UserID or Password"
LOGIN_INPUT_USERID_TEXT = "????????????ID"
LOGIN_INPUT_PASS_TEXT = "????????????"
LOGIN_INPUT_BTN_TEXT = "??????"
# LOGIN_SIMULATION_BTN_TEXT = "????????????"


# sjhub
SJHUB_VIEWPORT_TITLE = "SJHub - Record Your Trades!"
SJHUB_WINDOW_TEXT = "(SJHub) Investment Tracker"
SJHUB_NEWS_BTN_TEXT = "News"
SJHUB_DISPLAY_TOTAL_PROFIT_TEXT = "Net Profit: "
SJHUB_DISPLAY_WIN_RATE_TEXT = "Win-Rate %: "
SJHUB_CLOSED_TRADES_TEXT = "Closed Trades"
SJHUB_OPEN_TRADES_TEXT = "Open Trades"
SJHUB_OPEN_TRADES_CRYPTO_STOCK_TABLE_TEXT = "Stock/Crypto"
SJHUB_OPEN_TRADES_OPTION_TABLE_TEXT = "Option"
SJHUB_VIEW_TRADE_BTN_TEXT = "View"
SJHUB_OPEN_TRADES_ROW_TEXT = "open_trade row "
SJHUB_CLOSED_TRADES_ROW_TEXT = "closed_trade row "
SJHUB_SELL_TEXT = "Sell"
SJHUB_REMOVE_TEXT = "X"
SJHUB_ADD_BTN_TEXT = "Add Trade"
SJHUB_MENU_SYSTEM_TEXT = "System"
SJHUB_MENU_LOGOUT_TEXT = "Logout"
SJHUB_MENU_EXIT_TEXT = "Exit App"
SJHUB_SELL_BTN_WIDTH = 90
SJHUB_VIEW_CLOSED_TRADE_BTN_WIDTH = 72
SJHUB_VIEW_OPEN_TRADE_BTN_WIDTH = 92
SJHUB_PROFIT_WINRATE_GROUP_SPACERY = 25
SJHUB_CLOSED_OPEN_TRADES_GROUP_SPACERY = 25
SJHUB_PROFIT_WINRATE_GROUP_SPACERX = SJCLICK_WINDOW_VIEWPORT_SIZE[0] / 3.6
SJHUB_OPEN_REMOVE_SPACERX = 25
SJHUB_CLOSED_REMOVE_SPACERX = 15

# # One Chart
TICK_CHART_WINDOW_TEXT = "???????????????"
TICK_CHART_SPACERY = 5
TICK_CHART_SPACERX = 10
