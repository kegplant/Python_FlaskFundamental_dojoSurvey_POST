from flask import Flask, render_template, request, redirect, flash,session
app = Flask(__name__)
app.secret_key='piece of shit'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
  names=request.form['name']
  if len(names)<1:
    flash('Name cannot be empty!')
    return redirect('/')
  if len(request.form['comment'])<1:
    flash('Comment cannot be empty!')
    return redirect('/')
  elif len(request.form['comment'])>120:
    flash('Please keep comments under 120 characters.')
    return redirect('/')
  return render_template('result.html', info=request.form)

app.run(debug=True)