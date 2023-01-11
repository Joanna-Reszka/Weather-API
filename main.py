from flask import Flask, render_template
import pandas as pd
# Flask - webframework that will manage multiple webpages
# Create Flask website object
app = Flask("__name__")
# Connect html pages with  Flask website object
# function decorator
@app.route('/')
def home():
    # Flask by default will look for html file in "templates" folder
    return render_template('home.html')
#<station>/<date> means that those parameters are typed in by user
@app.route('/api/v1/<station>/<date>')
def about(station,date):
    filename = ("data_small/TG_STAID" + str(station).zfill(6) + ".txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # .zfill fills zeros within given range until nr eg if 5 places and you give
    # nr 45 will fill 00045
    temperature= df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    # Flask by default will look for html file in "templates" folder
    return {"station": station, "date": date, "temperature": temperature}

# make sure that app runs only from main and not as imported
if __name__ == "__main__":
    app.run(debug=True)
    #if running more apps can specify different port than 5000,
    #eg 5001:
    #app.run(debug=True, port=5001)

