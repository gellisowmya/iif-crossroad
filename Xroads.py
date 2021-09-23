from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/',methods = ['POST', 'GET'])
def login():
      if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('home'))
      return render_template('login.html')
@app.route('/home/')
def home():
    pie_labels = labels
    pie_values = values
    return render_template('home.html')

@app.route('/projects_dashboard/')
def projects_dashboard():
    return render_template('projects_dashboard.html')
    
@app.route('/project_details/')
def project_details():
    return render_template('project_details.html')

@app.route('/Inprogress_projects/')
def Inprogress_projects():
    return render_template('Inprogress_projects.html')
    
@app.route('/Open_projects/')
def Open_projects():
    return render_template('Open_projects.html')
    
@app.route('/Projects_completed/')
def Projects_completed():
    return render_template('Projects_completed.html')
    
@app.route('/Upcoming_projects/')
def Upcoming_projects():
    return render_template('Upcoming_projects.html')
    
@app.route('/create_project/',methods = ['POST', 'GET'])
def create_project():
    if request.method == 'POST':
        user = request.form['project_name']
        return redirect(url_for('create_project_status'))
    return render_template('create_project.html')
    
@app.route('/create_project_status/')
def create_project_status():
    return render_template('create_project_status.html')
    
@app.route('/About/')
def About():
    return render_template('About.html')
   
@app.route('/profile/')
def profile():
    return render_template('profile.html')
if __name__ == '__main__':
    app.run(debug=True)
