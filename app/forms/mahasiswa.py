from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import ValidationError, DataRequired
from wtforms.fields.html5 import DateField

class MahasiswaSave(FlaskForm):
    msg = 'data tidak boleh kosong'
    nim = StringField('NIM', validators=[DataRequired(message=msg)])
    nama = StringField('Nama', validators=[DataRequired(message=msg)])
    jenis_kelamin = StringField('Jenis Kelamin', validators=[DataRequired(message=msg)])
    tmpt_lahir = StringField('Tempat Lahir', validators=[DataRequired(message=msg)])
    tgl_lahir = StringField('Tanggal Lahir', validators=[DataRequired(message=msg)])
    alamat =StringField('Alamat', validators=[DataRequired(message=msg)])
    prodi =StringField('Prodi', validators=[DataRequired(message=msg)])
    password =PasswordField('Password', validators=[DataRequired(message=msg)])
    submit = SubmitField('Simpan')

class MataKuliahSave(FlaskForm):
    msg = 'data tidak boleh kosong'
    kd_mk = StringField('Kode MK', validators=[DataRequired(message=msg)])
    nama_mk = StringField('Nama MK', validators=[DataRequired(message=msg)])
    sks = StringField('SKS', validators=[DataRequired(message=msg)])
    semester = StringField('Semester', validators=[DataRequired(message=msg)])
    submit = SubmitField('Simpan')

class LoginForm(FlaskForm):
    nim = StringField('NIM', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField ('Login')