import os
from flask import Flask, render_template

app = Flask(__name__)

TABLEAU_URL = os.environ.get(
    "TABLEAU_URL",
    "https://public.tableau.com/app/profile/harshvardhan.gupta1425/viz/Global_Fuel_Prices_and_Taxation_Trends_17932843176370/Story1"
)

@app.route("/")
def home():
    return render_template("index.html", tableau_url=TABLEAU_URL)

if __name__ == "__main__":
    app.run(debug=True)
