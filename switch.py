import requests

class Switch:
    def __init__(self, NOTIFYME_ACCESS_CODE, plug_name="default"):
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
        self.params["notification"] = None
        if "sent" not in response.text:
            print("Error sending notification")
            print(response.text)
            return 0
        return 1
    
    def on(self):
        requests.get(self.url, params={"plug": self.plug_name, "action": "on"})
    
    def off(self):
        requests.get(self.url, params={"plug": self.plug_name, "action": "off"})