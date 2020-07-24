from app import appInstance
from flask import render_template, flash, redirect
from app.forms import LoginForm

@appInstance.route('/')
def index():
  user = {'username': 'Devansh'}
  posts =[
    {
      'author': {'username': 'John'},
      'body': 'Beautiful day today'
    },
    {
      'author':{'username': 'Susan'},
      'body': 'The Avengers movie was so cool'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts = posts)
  

@appInstance.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)