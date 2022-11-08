from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SearchField, TextAreaField, TelField

class PostForm(FlaskForm):
    title = StringField('Title here')
    publish = BooleanField("Publish Now!")
    # content = CKEditorField("Content here")
    content = TextAreaField("Content here")
    submit = SubmitField()
