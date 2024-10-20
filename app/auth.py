from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from .forms import LoginForm, RegistrationForm
from . import db  

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Formulario válido, procesando registro...")

        # Verificar si el usuario ya existe
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('El nombre de usuario ya está en uso, por favor elige otro.', 'danger')
            return redirect(url_for('auth.register'))

        # Crear un nuevo usuario con contraseña encriptada
        try:
            hashed_password = generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            # Autenticar el usuario después del registro
            login_user(new_user)
            print("Usuario autenticado tras registro:", current_user.is_authenticated)
            flash('¡Registro exitoso! Ahora estás autenticado.', 'success')
            return redirect(url_for('main.home'))  # Redirigir al home autenticado
        except Exception as e:
            db.session.rollback()
            print(f"Error en el registro: {e}")  # Mostrar el error específico en consola
            flash('Ocurrió un error durante el registro. Inténtalo de nuevo.', 'danger')
            return redirect(url_for('auth.register'))

    print("Error en el registro: ", form.errors)  # Mostrar errores de validación
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        # Verificar las credenciales del usuario
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            print("Usuario autenticado:", current_user.is_authenticated)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.home'))  # Redirigir al home autenticado
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Te has desconectado.', 'info')
    return redirect(url_for('main.home'))