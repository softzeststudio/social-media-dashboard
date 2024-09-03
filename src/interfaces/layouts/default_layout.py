# src/interfaces/layouts/default_layout.py

class DefaultLayout:
    @staticmethod
    def apply_layout(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Social Media Dashboard", curses.A_BOLD)
        stdscr.refresh()
