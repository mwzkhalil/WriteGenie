from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace-this-with-a-secret-key'
app.config['API_KEY'] = 'your-api-key-here'

from WriteGenie import views
