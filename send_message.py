import pyautogui

# Getting the maximum coordinates.
max_x, max_y = pyautogui.size()

# Creating the scalars.
x, y = max_x / 1366, max_y / 768


# Creating the Web Whatsapp Bot.
class WebWhatsappBot:
    """This bot would send messages on web."""

    def __init__(self, browser_name):
        """This function is initializing all the variables."""
        self.block = False
        self.message_type = "str"
        self.browser_name = browser_name

    def open(self):
        """This function would open the browser."""
        pyautogui.hotkey("win")
        pyautogui.typewrite(f"apps: {self.browser_name}")
        pyautogui.hotkey("enter")
        pyautogui.sleep(1)
        pyautogui.typewrite("web.whatsapp.com")
        pyautogui.hotkey("enter")

    def send_message(self, message):
        """This function would send the message."""
        if pyautogui.screenshot().getpixel((81 * x, 153 * y)) != (255, 255, 255):
            self.block = True
            print("Something blocked the automation")

        if not self.block:
            pyautogui.click(81 * x, 153 * y)

        if isinstance(message, list):
            self.message_type = "list"


class Telegram:
    pyautogui.click(73, 49)
    """This bot would send messages on telegram desktop."""
    def __init__(self, phone_numbers, message):
        """This function would initialize the variables."""
        pyautogui.hotkey("win")
        pyautogui.typewrite("apps: Telegram")
        pyautogui.hotkey("enter")
        for phone_number in phone_numbers:
            pyautogui.sleep(1)
            pyautogui.typewrite(phone_number)
            pyautogui.hotkey("enter")
            if isinstance(message, str):
                pyautogui.typewrite(message)

            elif isinstance(message, list):
                for line in message:
                    pyautogui.typewrite(line)
                    pyautogui.hotkey('alt', 'enter')
                pyautogui.hotkey("backspace")

            pyautogui.hotkey("enter")
