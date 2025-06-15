import pyautogui as gui
import requests
import time
import os


def launch_notepad():
    try:
        gui.hotkey('win', 'r')
        time.sleep(1)
        gui.write('notepad')
        gui.press('enter')
        time.sleep(1)
    except Exception as e:
        print("Failed to open Notepad:", e)


def fetch_content(url):
    try:
        response = requests.get(url)
        return response.json()[:10]
    except Exception as e:
        print("Failed to fetch posts:", e)


def write_content(title, body):
    content = f"{title}: \n\n{body}"
    # Clear the text file
    gui.hotkey('ctrl', 'n') # open new tab in notepad
    gui.hotkey('ctrl', 'shift', 'tab') # move to the previous tab in notepad
    gui.hotkey('ctrl', 'w') # close current tab in notepad
    gui.write(content, interval=0.03)
    time.sleep(1)


def save_doc(doc_name):
    folder = "C:\\Users\\allaa\\Desktop\\tjm-project"
    mypath = os.path.join(folder, doc_name)
    print(mypath)
    gui.hotkey('ctrl', 's')
    time.sleep(2)

    gui.write(mypath)
    gui.press('enter')
    time.sleep(1)


def close_notepad():
    gui.hotkey('alt', 'f4')
    time.sleep(0.5)


if __name__ == "__main__":
    posts = fetch_content("https://jsonplaceholder.typicode.com/posts/")
    for post in posts:
        try:
            launch_notepad()
            write_content(post['title'], post['body'])
            save_doc(f"post {post['id']}.txt")
            close_notepad()
        except Exception as e:
            print(f"Failed to process post {post['id']}: {e}")
