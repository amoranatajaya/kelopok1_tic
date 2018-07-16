from flask import url_for, redirect, render_template
from app.forms.mahasiswa import MahasiswaSave, MataKuliahSave, LoginForm
from app.models.models import Mahasiswa, MataKuliah
from app import db, login_manager
from flask_login import login_user, logout_user, current_user

class AdminController:
    def mhs_adm(self):
        form = MahasiswaSave()
        if form.validate_on_submit():
            mhs = Mahasiswa(nim=form.nim.data, 
                            nama= form.nama.data.upper(),  
                            jenis_kelamin=form.jenis_kelamin.data, 
                            
                            tmpt_lahir= form.tmpt_lahir.data, 
                            tgl_lahir= form.tgl_lahir.data, 
                            alamat=form.alamat.data, 
                            prodi=form.prodi.data, 
                            password=form.password.data)
            mhs.save()
            return redirect(url_for('mhs_view'))
        return render_template('admin/mhs_input.html', form=form)

    def delete(self, id):
        mhs=Mahasiswa.query.get(id)
        mhs.delete()
        return redirect(url_for('mhs_view'))
    
    def deletemk(self, id):
        mk=MataKuliah.query.get(id)
        mk.deletemk()
        return redirect(url_for('mk_view'))

    def mk_adm(self):
        form = MataKuliahSave()
        if form.validate_on_submit():
            mk = MataKuliah(kd_mk=form.kd_mk.data,
                            nama_mk=form.nama_mk.data.upper(),
                            sks=form.sks.data,
                            semester=form.semester.data , 
                            mhs_id='tersedia')
            mk.save()
            return redirect(url_for('mk_view'))
        return render_template('admin/mk_input.html', form=form)

    def mk_view(self):
        mk_view= MataKuliah.query.all()
        
        return render_template('admin/mk_view.html', mk_view=mk_view)

    def login_mhs(self):
        form = LoginForm()
        if form.is_submitted():
            mhs = Mahasiswa.query.filter_by(nim=form.nim.data).first()
            if mhs:
                login_user(mhs)
                return redirect('krs')
            else:
                return 'Password Salah'
        return render_template('login/login_mhs.html', form=form)

    def logout_mhs(self):
        logout_user()
        return redirect(url_for('login_mhs'))
    
    def ambil(self, id):
        mk = MataKuliah.query.get(id)
        mk.mhs_id = current_user.id
        db.session.commit()
        return redirect(url_for('krs'))
        
    def krs(self):
        krs = MataKuliah().query.all()
        pilihan = MataKuliah().query.filter_by(mhs_id = current_user.id).all()
        return render_template('mahasiswa/krs.html', krs=krs, pilihan=pilihan)
