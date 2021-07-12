from os import write
from flask import Flask, render_template, request, redirect  
import csv

app = Flask(__name__)

@app.route("/")
def index():
        return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
        return render_template(page_name)

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open ('database.text', mode = 'a') as database:
      file = database.write(f'\n{email},{subject},{message}')  


def write_to_csv(data):
    with open ('database.csv', newline='' ,mode = 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data =  request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something wrong'
        

# @app.route("/index.html")
# def home():
#         return render_template('index.html')


# @app.route("/about.html")
# def about():
#         return render_template('about.html')


# @app.route("/components.html")
# def compo():
#         return render_template('components.html')


# @app.route("/contact.html")
# def contact():
#         return render_template('contact.html')


# @app.route("/project.html")
# def project():
#         return render_template('project.html')


# @app.route("/services.html")
# def services():
#         return render_template('services.html')



# @app.route("/<username>/<int:post_id>")
# def uname(username=None, post_id=None):
#         return render_template('index.html', name=username, post=post_id)
