from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from app.models import Question, Answer
from app.forms import QuestionForm, AnswerForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Verificación de autenticación
    print(f"Usuario autenticado: {current_user.is_authenticated}")
    if current_user.is_authenticated:
        questions = Question.query.all()  # Obtener todas las preguntas para usuarios autenticados
        print(f"Nombre de usuario: {current_user.username}")  # Mostrar nombre del usuario autenticado en la consola
        return render_template('home.html', questions=questions)  # Página para usuarios autenticados
    else:
        return render_template('home_guest.html')  # Página para usuarios no autenticados

@main.route('/ask', methods=['GET', 'POST'])
@login_required  # Solo usuarios autenticados pueden hacer preguntas
def ask():
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(question)
        db.session.commit()
        flash('Your question has been posted!', 'success')
        return redirect(url_for('main.home'))
    return render_template('ask.html', form=form)

@main.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(body=form.body.data, question_id=question.id, user_id=current_user.id)
        db.session.add(answer)
        db.session.commit()
        flash('Your answer has been posted!', 'success')
        return redirect(url_for('main.question', question_id=question.id))
    return render_template('question.html', question=question, form=form)
