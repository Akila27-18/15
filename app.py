from flask import Flask, render_template, flash, redirect, url_for
from forms import CourseFeedbackForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def feedback():
    form = CourseFeedbackForm()
    if form.validate_on_submit():
        rating = form.rating.data
        if rating < 5:
            flash("We'll improve!", "danger")
        elif rating <= 7:
            flash("Thanks for your feedback!", "warning")
        else:
            flash("Glad you enjoyed the course!", "success")
        return redirect(url_for('feedback'))
    return render_template('feedback.html', form=form)
