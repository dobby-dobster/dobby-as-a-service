from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", content="Welcome to Dobby as a Service!")

@app.route("/breed")
def breed():
    return "Dobby is a German Shorthaired Pointer"

@app.route("/age")
def age():
    import datetime
    currentDate = datetime.datetime.now()
    dob = "xx/xx/xxxx"
    deadlineDate= datetime.datetime.strptime(dob,'%m/%d/%Y')
    daysLeft = currentDate - deadlineDate
    years = ((daysLeft.total_seconds())/(365.242*24*3600))
    yearsInt=int(years)
    months=(years-yearsInt)*12
    monthsInt=int(months)
    days=(months-monthsInt)*(365.242/12)
    daysInt=int(days)
    hours = (days-daysInt)*24
    hoursInt=int(hours)
    minutes = (hours-hoursInt)*60
    minutesInt=int(minutes)
    seconds = (minutes-minutesInt)*60
    secondsInt =int(seconds)
    return "Dobby is {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} minutes, {5:d} seconds old.".format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt)

@app.route("/where")
def where():
    import random
    places = ['on the sofa',
              'in the garden',
              'a sleep in bed']
    location = random.sample(places, 1)
    return "Dobby is {0}".format(", ".join(location))

@app.route("/nicknames")
def nicknames():
    names = ['dobster', 'dib dob']
    return "Dobby's nicknames: {0}".format(", ".join(names))

if __name__ == '__main__':
    app.run(debug=True)
