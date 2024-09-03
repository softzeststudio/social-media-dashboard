# src/interfaces/tui_manager.py

import curses

class TUIManager:
    def __init__(self, config):
        self.config = config

    def display_dashboard(self, stdscr, api_manager):
        stdscr.clear()

        feeds = api_manager.fetch_feeds()
        row = 0

        # Display Twitter feed
        stdscr.addstr(row, 0, "Twitter Feed:", curses.A_BOLD)
        row += 1
        for tweet in feeds['twitter']:
            stdscr.addstr(row, 0, f"{tweet['user']}: {tweet['text']}")
            row += 1

        row += 1  # Add space between feeds

        # Display Reddit feed
        stdscr.addstr(row, 0, "Reddit Feed:", curses.A_BOLD)
        row += 1
        for post in feeds['reddit']:
            stdscr.addstr(row, 0, f"{post['title']} (by {post['author']})")
            row += 1

        row += 1  # Add space between feeds

        # Display Mastodon feed
        stdscr.addstr(row, 0, "Mastodon Feed:", curses.A_BOLD)
        row += 1
        for toot in feeds['mastodon']:
            stdscr.addstr(row, 0, f"{toot['account']} (by {toot['content']})")
            row += 1

        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting
