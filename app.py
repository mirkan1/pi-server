import os
import flask
from switch import Switch

app = flask.Flask(__name__)
app.name = "raspberry-pi"

NOTIFYME_ACCESS_CODE = os.environ.get("NOTIFYME_ACCESS_CODE")
SWITCHER = Switch(NOTIFYME_ACCESS_CODE, "unknown-plug") # Switch

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/api/toggle")
def toggle():
    plug_name = flask.request.args.get("plug")
    if not plug_name:
        return flask.jsonify({"status": "error", "message": "No plug specified"})
    action = flask.request.args.get("action")
    if not action:
        return flask.jsonify({"status": "error", "message": "No action specified"})
    SWITCHER.set_plug_name(plug_name)
    if action == "on":
        SWITCHER.on()
    elif action == "off":
        SWITCHER.off()
    return flask.jsonify({"status": "ok"})

#http://127.0.0.1:1131/api/notify?message=hello
@app.route("/api/notify")
def notify():
    message = flask.request.args.get("message")
    if not message:
        return flask.jsonify({"status": "error", "message": "No message specified"})
    notification_success = SWITCHER.notify_me(message)
    if not notification_success:
        return flask.jsonify({"status": "error", "message": "Error sending notification"})
    return flask.jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=1131)