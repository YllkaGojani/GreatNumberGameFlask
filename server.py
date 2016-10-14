from flask import Flask,render_template,request,redirect,session,flash
import random
app = Flask(__name__)
app.secret_key = 'ThiIsSecret'


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/num', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    session['number'] = 55 
    #session['number'] = random.randrange(0, 101)

    print guess,"random "+ str(session['number'])
    if guess < session['number']:
        flash("Too low!")
        session['color'] = 'red'
    elif guess > session['number']:
        flash("Too High!")
        session['color'] = 'red'
    else:
        flash(str(guess)+" was the number!")
        session['color'] = 'green'
    return redirect('/')

@app.route('/reset')
def reset():
    session['number'] = random.randrange(0, 101)
    return redirect('/')
				
app.run(debug=True)	