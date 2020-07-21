from flask import flash, redirect, url_for, render_template
from myexercise import app, db
from myexercise.models import Message
from myexercise.forms import HelloForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name) #实例化模型类
        db.session.add(message)
        db.session.commit()
        flash('Your wish has been sent to Pony马!')
        return redirect(url_for('index'))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form,messages=messages)

