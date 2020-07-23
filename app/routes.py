from app import appInstance
from flask import render_template

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
  
