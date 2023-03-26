from flask_wtf import FlaskForm
from wtforms import BooleanField,SubmitField

class FilterForm(FlaskForm):

    avable=BooleanField('Наличие',default=False)


ok_filter = SubmitField()