from flask_wtf import Form, RecaptchaField
from wtforms.widgets.html5 import NumberInput, URLInput
from wtforms.fields.html5 import URLField
from wtforms import SubmitField, HiddenField, TextField, SelectField, SelectMultipleField, IntegerField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, Email, InputRequired, NumberRange, Optional, URL

# Form ORM
class QuizForm(Form):
    geolocation = HiddenField("geolocation", validators=[Optional()])
    test = SelectField('Wurden Sie bereits auf das Coronavirus getestet und wenn ja, wie fiel der Test aus?', 
        choices=[
            ('Nicht durchgeführt', 'Nein'), 
            ('Ergebnis ausstehend', 'Ja, Ergebnis liegt noch nicht vor'), 
            ('Negativ', 'Ja, Ergebnis negativ'),
            ('Positiv', 'Ja, Ergebnis positiv')],
        validators=[InputRequired()] )
    datetest = DateField('Wenn ja, wann fand der Test statt?', format='%Y-%m-%d', validators=[Optional()])
    notherstest = IntegerField('Wieviele Menschen, mit denen Sie Kontakt hatten, wurden positiv getestet?', widget=NumberInput(), validators=[NumberRange(min=0, max=100, message="Bitte Zahl mit Nummern eingeben")])
    symptoms = SelectMultipleField('Markieren Sie die Symptome, die sie haben (zum Markieren mehrerer Optionen am PC Strg-Taste (Ctrl) gedrückt halten):', 
        choices=[
            ('Fieber', 'Fieber'), 
            ('Müdigkeit', 'Müdigkeit'), 
            ('Husten', 'Husten'), 
            ('Niesen', 'Niesen'), 
            ('Gliederschmerzen', 'Gliederschmerzen'), 
            ('Schnupfen', 'Schnupfen'), 
            ('Halsschmerzen', 'Halsschmerzen'), 
            ('Durchfall', 'Durchfall'), 
            ('Kopfschmerzen', 'Kopfschmerzen'), 
            ('Kurzatmigkeit', 'Kurzatmigkeit'),
        ], 
        validators=[InputRequired()], render_kw={"size": "10"})
    dayssymptoms = IntegerField('Seit wievielen Tagen haben Sie Symptome?', widget=NumberInput(), validators=[Optional(), NumberRange(min=0, max=None, message="Bitte Zahl mit Nummern eingeben")])
    notherssymptoms = IntegerField('Wieviele Menschen, mit denen Sie Kontakt hatten, haben ähnliche Symptome?', widget=NumberInput(), validators=[Optional(), NumberRange(min=0, max=100, message="Bitte Zahl mit Nummern eingeben")])

    age = IntegerField('Wie alt sind Sie (Jahre)', widget=NumberInput(), validators=[NumberRange(min=0, max=120, message="Bitte Zahl mit Nummern eingeben")])
    sex = SelectField("Welches Geschlecht haben Sie",
    choices=[
            ('', ''), 
            ('female', 'weiblich'),
            ('male', 'männlich'), 
     ] , validators=[InputRequired()])
    email_addr = TextField('Ihr Benutzername', validators=[InputRequired(message="Bitte geben Sie einen Benutzernamen an")])
    password = PasswordField('Geben Sie ein Passwort ein, falls Sie Ihre Daten später ändern oder löschen wollen. Das Passwort wird auf dem Server nicht-wiederherstellbar verschlüsselt gespeichert.', validators=[InputRequired(message="Bitte geben Sie ein Passwort ein")])
    recaptcha = RecaptchaField()
    submit = SubmitField('Senden')

class DeleteForm(Form):
    email_addr = TextField('Benutzername', validators=[InputRequired(message="Bitte geben Sie einen Benutzernamen an")])
    password = PasswordField('Passwort', validators=[InputRequired(message="Bitte geben Sie ein Passwort ein")])
    recaptcha = RecaptchaField()
    submit = SubmitField('Senden')
    

class LandkreisForm(Form):
    name = HiddenField("name")
    ncases = IntegerField('Wieviele Menschen wurden positiv getestet?', widget=NumberInput(), validators=[NumberRange(min=0, max=100, message="Bitte Zahl mit Nummern eingeben")])
    source = URLField("Bitte geben Sie Ihre Quelle in Form einer Webseite an", validators=[InputRequired(), URL(message="Bitte geben Sie eine gültige Webadresse an")])
    recaptcha = RecaptchaField()
    submit = SubmitField('Senden')
    