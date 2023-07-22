import requests
import os
import dotenv 
dotenv.load_dotenv()

NOTIFYME_ACCESS_CODE = os.environ.get("NOTIFYME_ACCESS_CODE")
# if not ACCESS_CODE:
#     raise Exception("ACCESS_CODE environment variable not set")

class Switch:
    def __init__(self, plug_name="default"):
        self.plug_name = plug_name
        self.url = "https://api.notifymyecho.com/v1/NotifyMe"
        self.params = {
            "notification": None,
            "accessCode": NOTIFYME_ACCESS_CODE
        }
    
    def set_plug_name(self, plug_name):
        self.plug_name = plug_name

    def notify_me(self, message):
        self.params["notification"] = message
        response = requests.get(self.url, params=self.params)
        if "sent" not in response.text:
            print("Error sending notification")
            print(response.text)
        self.params["notification"] = None
    
    def on(self):
        requests.get(self.url, params={"plug": self.plug_name, "action": "on"})
    
    def off(self):
        requests.get(self.url, params={"plug": self.plug_name, "action": "off"})