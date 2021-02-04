from flask import (Flask , redirect, url_for, render_template, flash)
from form import TaskForm

from celery import Celery

from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

mail = Mail(app)

client = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
client.conf.update(app.config)


@client.task
def send_email(to, subject, template, **kwargs):
    with app.app_context():
        msg = Message('ping',sender='admin@hh.co', recipients=[data['email']])
        msg.body = data['message']
        mail.send(msg)
        
        

@app.route("/", methods=['GET', 'POST'])
def index():

    form = TaskForm()

    if form.validate_on_submit():
        data = {}
        data['email'] = form.email.data
        data['firstname'] = form.firstname.data
        data['lastname'] = form.lastname.data
        data['message'] = form.message.data
        duration = int(form.duration.data)
        duration_unit = form.duration_unit.data

        if duration_unit == 'minutes':
            duration = 60
        elif duration_unit == 'hours':
            duration = 3600
        elif duration_unit == 'days':
            duration = 86400
        

        send_mail.apply_async(args=[data], cuntdown = duration )
        flash(f"Email will be sent to  {data['email']} in {duration} {duration_unit}")

        return redirect(url_for('index'))

    return render_template('index.html', form = form )



if __name__ == '__main__':
    app.run(debug=True)

