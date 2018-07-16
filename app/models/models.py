from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Mahasiswa.query.get(user_id)

class Mahasiswa(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    nim = db.Column(db.String(10), nullable=True)
    nama = db.Column(db.String(50), nullable =False)
    jenis_kelamin = db.Column(db.String(50), nullable=False)
    tmpt_lahir = db.Column(db.String(30), nullable=False)
    tgl_lahir = db.Column(db.String(20), nullable=True)
    alamat = db.Column(db.String(100), nullable=False)
    prodi = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class MataKuliah(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    kd_mk = db.Column(db.String(10), nullable=True)
    nama_mk = db.Column(db.String(50), nullable =False)
    sks = db.Column(db.String(10), nullable=False)
    semester = db.Column(db.String(10),nullable=False)
    mhs_id = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def deletemk(self):
        db.session.delete(self)
        db.session.commit()

  