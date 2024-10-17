import webview
import os
from py import ApiBridge

CWD: str = os.getcwd()
INDEX_HTML: str = "/index.html"


def start_webview():
    webview.create_window('Test Build', 'file://' +
                          CWD + INDEX_HTML, js_api=ApiBridge)
    webview.start()


def main():
    start_webview()


if __name__ == "__main__":
    main()
