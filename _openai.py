import time
import pyautogui
import pyperclip
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

ICON_POS = (928, 1045)
SELECT_START = (725, 159)
SELECT_END = (1817, 895)

WAIT_TIME = 5   


def get_latest_chat():
    pyautogui.click(*ICON_POS)
    time.sleep(1)

    pyautogui.moveTo(*SELECT_START)
    pyautogui.dragTo(*SELECT_END, duration=0.5, button="left")
    time.sleep(0.3)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)

    return pyperclip.paste()


def generate_reply(chat_text):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Nithin. You are from India, coder, "
                    "you speak Telugu + English casually. "
                    "Reply naturally like WhatsApp chat."
                )
            },
            {
                "role": "user",
                "content": chat_text
            }
        ]
    )

    return completion.choices[0].message.content


def send_reply(reply):

    pyperclip.copy(reply)
    time.sleep(0.2)

    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)

    pyautogui.press("enter")



print("Bot started... Move mouse to top-left corner to stop.")

while True:
    try:
        chat = get_latest_chat()
        print("Chat:", chat)

        reply = generate_reply(chat)
        print("Reply:", reply)

        send_reply(reply)

        time.sleep(WAIT_TIME)

    except Exception as e:
        print("Error:", e)
        time.sleep(3)
