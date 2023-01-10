from flask import Flask, render_template

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
    #df = pd.read_csv("")
    temperature = 23
    # Flask by default will look for html file in "templates" folder
    return {"station": station, "date": date, "temperature": temperature}

# make sure that app runs only from main and not as imported
if __name__ == "__main__":
    app.run(debug=True)

