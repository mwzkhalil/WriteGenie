from flask import render_template, redirect, url_for, flash
from WriteGenie import app
from WriteGenie.forms import TextInputForm
from WriteGenie.api import suggest_alternatives

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextInputForm()
    if form.validate_on_submit():
        text = form.text.data
        suggestions = suggest_alternatives(text)
        flash("Here are some alternative words and phrases for your text:")
        flash(suggestions)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')
