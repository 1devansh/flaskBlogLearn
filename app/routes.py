from app import appInstance

@appInstance.route('/')
def index():
  user = {'username': 'Devansh'}
  return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
  

@appInstance.route('/index')
def indextry():
  return "This is index page"


@appInstance.route('/index.html')
def indextry2():
  return " is this index page?"
