# src/interfaces/themes/default_theme.py

class DefaultTheme:
    TITLE_COLOR = 1
    HIGHLIGHT_COLOR = 2
    NORMAL_COLOR = 3

def apply_theme():
    curses.init_pair(DefaultTheme.TITLE_COLOR, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(DefaultTheme.HIGHLIGHT_COLOR, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(DefaultTheme.NORMAL_COLOR, curses.COLOR_WHITE, curses.COLOR_BLACK)
