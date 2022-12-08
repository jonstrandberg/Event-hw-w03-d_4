from flask import render_template, request, redirect 
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='home', events=events)

@app.route('/events', methods=['POST'])
def create():

    date=request.form["date"]
    name=request.form['name']
    guests=request.form['guests']
    room=request.form['room']
    description=request.form['description']
    recurring = request.form['recurring']


    new_event=Event(date, name, guests, room, description, recurring)

    events.append(new_event)
    event_recurring(events)
    return redirect('/events')

def event_recurring(events):
    for event in events:
        if event.recurring == True:
            return "Yes"
    else:
        return "No"
