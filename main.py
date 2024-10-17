import webview
import threading
import asyncio
import os

CWD: str = os.getcwd()
INDEX_HTML: str = "/index.html"


def start_webview():
    webview.create_window('Test Build', 'file://' + CWD + INDEX_HTML)
    webview.start()


def main():
    start_webview()


if __name__ == "__main__":
    main()
