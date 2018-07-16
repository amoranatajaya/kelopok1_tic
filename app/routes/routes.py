from flask import Flask, render_template, redirect,url_for
from app import app
from app.controllers.mahasiswa import AdminController
from app.models.models import Mahasiswa, MataKuliah

@app.route('/')

@app.route('/brandalogin')
def brandalogin():
    return render_template('login/brandalogin.html', brandalogin=brandalogin)

@app.route('/dash_admin')
def dash_admin():
    return render_template('admin/dash_admin.html', dash_admin=dash_admin)
    
@app.route('/mhs_view')
def mhs_view():
    mhs_view= Mahasiswa.query.all()
    return render_template('admin/mhs_view.html', mhs_view=mhs_view)

@app.route('/mhs_input', methods=['GET','POST'])
def mhs_input():
    return AdminController().mhs_adm()

@app.route('/mk_input', methods=['GET', 'POST'])
def mk_input():
    return AdminController().mk_adm()

@app.route('/mk_view', methods=['GET','POST'])
def mk_view():
    mk_view= MataKuliah.query.all()
    return AdminController().mk_view()


@app.route('/delete/<id>')
def delete(id):
    return AdminController().delete(id)

@app.route('/deletemk/<id>')
def deletemk(id):
    return AdminController().deletemk(id)

@app.route('/dash_mhs')
def dash_mhs():
    return render_template('mahasiswa/dash_mhs.html', dash_mhs=dash_mhs)

@app.route('/krs')
def krs():
    return AdminController().krs()

@app.route('/login_mhs', methods=['GET', 'POST'])
def login_mhs():
    return AdminController().login_mhs()

@app.route('/logout_mhs')
def logout_mhs():
    return AdminController().logout_mhs()

@app.route('/ambil/<id>')
def ambil(id):
    return AdminController().ambil(id)


    
