from flask_wtf import FlaskForm
from wtforms import BooleanField,SubmitField,IntegerRangeField,SelectField,RadioField
from wtforms.validators import NumberRange
import datetime

class FilterForm(FlaskForm):

    avable = BooleanField(' Наличие игры',default=False)
    min_price = IntegerRangeField(validators=[NumberRange(min=0, max=9999)],default=9999)
    max_price = IntegerRangeField(validators=[NumberRange(min=1, max=10000)],default=10000)
    
    min_people = IntegerRangeField(validators=[NumberRange(min=0, max=99)],default=99)
    max_people = IntegerRangeField(validators=[NumberRange(min=1, max=100)],default=100)

    min_time_game = IntegerRangeField( validators=[NumberRange(min=0, max=599)],default=599)
    max_time_game = IntegerRangeField( validators=[NumberRange(min=1, max=600)],default=600)

    min_age = IntegerRangeField( validators=[NumberRange(min=0, max=79)],default=79)
    max_age = IntegerRangeField( validators=[NumberRange(min=1, max=80)],default=80)

    cards = BooleanField(' карты',default=True)
    cubes = BooleanField(' кубики',default=True)
    tiles = BooleanField(' тайлы',default=True)
    fields = BooleanField(' поле',default=True)
    chips = BooleanField(' фишки',default=True)
    tokens = BooleanField(' токены, каунтеры ',default=True)
    card_holders = BooleanField(' держатели для карт/фишек',default=True)
    add_elements = BooleanField(' дополнительные элементы',default=True)
    brand = SelectField("Бренд (Производитель):",choices=[('Все бренды'),('и еще что-то')])
    depend_lang = BooleanField('Зависимость от языка',default=False)
    lang = RadioField('язык',choices=[('русский'),('украинский'),('английский'),('другой')])
    game_or_add = RadioField(choices=[('Игра'),('Дополнение')],default='Игра')
    state = RadioField('Cостояние игры:',choices=[('новая'),('б/у')],default='новая')
    year_realise = SelectField("Год выпуска:",choices=[('Все')]+[(str(year_item)) for year_item in range(int(datetime.datetime.now().year),2000,-1)])
    edit_number = RadioField('Номер издания:',choices=[('любое'),('1'),('2'),('3'),('4'),('5')],default='любое')
    author =  SelectField("Автор:",choices=[('Все'),('Пушкин'),('Андерсен'),('Маршак')])    
    type_game = RadioField(choices=[('любой'),('стратегия'),('на память'),('ассоциации'),('бродилка'),('амери'),('евро'),('ДнД'),('абстрактные')],default='любой')

    re_gamers = IntegerRangeField( validators=[NumberRange(min=1, max=7)],default=7)
    random_game = IntegerRangeField( validators=[NumberRange(min=1, max=7)],default=4)
    level_input = IntegerRangeField( validators=[NumberRange(min=1, max=7)],default=1)
    intricacy_game = IntegerRangeField( validators=[NumberRange(min=1, max=7)],default=1)
    intricacy_rule = IntegerRangeField( validators=[NumberRange(min=1, max=7)],default=1)
    rating = IntegerRangeField( validators=[NumberRange(min=1, max=7)],default=7)

    
    


    


    ok_filter = SubmitField('Применить')