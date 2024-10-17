import webview
import os

CWD: str = os.getcwd()
INDEX_HTML: str = "/index.html"

js_func = {
    'alert': 'alert("this is a test")'
}


def create_window():
    webview.create_window('Test Build', 'file://' + CWD + INDEX_HTML)
    webview.start()


def main():
    create_window()


if __name__ == "__main__":
    main()
