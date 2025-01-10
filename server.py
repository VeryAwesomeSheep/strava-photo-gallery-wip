from flask import Flask, render_template, request, url_for, redirect
from stravalib.client import Client
from utils.storage import (
  read_activities,
)
from utils.data_fetch import (
  get_all_activities,
)

app = Flask(__name__)
app.config.from_envvar("APP_SETTINGS")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/login")
def login():
  c = Client()
  authorize_url = c.authorization_url(
    client_id=app.config["STRAVA_CLIENT_ID"],
    redirect_uri=url_for("dashboard", _external=True),
    approval_prompt="auto",
  )
  return redirect(authorize_url)

@app.route("/dashboard")
def dashboard():
  '''error = request.args.get("error")
  if error:
    return render_template("login_error.html", error=error)

  code = request.args.get("code")
  if not code:
    return redirect(url_for("home"))

  client = Client()
  access_token = client.exchange_code_for_token(
    client_id=app.config["STRAVA_CLIENT_ID"],
    client_secret=app.config["STRAVA_CLIENT_SECRET"],
    code=code,
  )
  strava_athlete = client.get_athlete()

  activities = read_activities(strava_athlete.id)'''
  activities = read_activities(29835910)

  return render_template(
    "dashboard.html",
    activities=activities,
  )

@app.route("/test")
def test():
  #print(deleteAthleteData(1234))
  pass

if __name__ == "__main__":
  app.run(debug=True)