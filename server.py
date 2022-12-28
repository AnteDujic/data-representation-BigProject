# Module: Data Representation
# Author: Ante Dujic

from flask import Flask, jsonify, request, abort, render_template, session, url_for, g, redirect
from dao import placesDAO

################################################################################################
# Autentification
# REF: https://www.youtube.com/watch?v=2Zz97NVbH0U&ab_channel=PrettyPrinted
################################################################################################

# User object
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

# Setting available users
users = []
users.append(User(id=1, username='Ante', password='student'))
users.append(User(id=2, username='Andrew', password='lecturer'))


app = Flask(__name__, static_url_path='', static_folder='staticpages', template_folder="pages")
app.secret_key = 'datarepresentation'

# Storing current user
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

# Route to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            # Logout any user
            session.pop('user_id', None)

            # Get input from login form
            username = request.form['username']
            password = request.form['password']

            # Autentification
            try:
                user = [x for x in users if x.username == username][0]
                if user and user.password == password:
                    session['user_id'] = user.id
                    return redirect(url_for('profile'))
            except:
                return render_template(url_for('/login.html'))

        return render_template('/login.html')
    except:
        return render_template('/login.html')

# Route to user home page
@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('/profile.html')

# Logout current user
@app.route("/logout")
def logout():
    session.clear()
    return render_template('/login.html')

################################################################################################
################################################################################################

# Initial page
@app.route('/')
def initial():
    return render_template('/login.html')

# Route to visited destinations page (own API)
@app.route('/index')
def index():
    # Checks if user is authenticated.
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template('/index.html')

# Route to destinations details page (wild API)
@app.route('/indexOne')
def indexOne():
    # Checks if user is authenticated.
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template('/indexOne.html')

# CRUD OPERATIONS
# Get all destinations
@app.route('/visited')
def getAll():
    if not g.user:
        return redirect(url_for('login'))
    return jsonify(placesDAO.getAll())

# Get a specific destination (by id)
@app.route('/visited/<int:id>')
def findByID(id):
    if not g.user:
        return redirect(url_for('login'))
    return jsonify(placesDAO.findByID(id))


# Add a new destination
@app.route('/visited', methods = ['POST'])
def create():
    if not g.user:
        return redirect(url_for('login'))
    if not request.json:
        abort(400)
    visit = {
    "city": request.json['city'], 
    "dov": request.json["dov"], 
    "hospitality": request.json["hospitality"],
    "food": request.json["food"],
    "transport": request.json["transport"],
    "attractions": request.json["attractions"],
    "entertainment": request.json["entertainment"]
    }
    values = (visit["city"],visit["dov"],visit["hospitality"],visit["food"],visit["transport"],visit["attractions"], visit["entertainment"])
    newId = placesDAO.create(values)
    visit["id"] = newId
    return jsonify(values)

# Update existing destination (by id)
@app.route('/visited/<int:id>', methods = ['PUT'])
def update(id):
    if not g.user:
        return redirect(url_for('login'))

    foundDestination = placesDAO.findByID(id)
    
    if len(foundDestination) == 0:
        return jsonify({}), 404      
    
    if "city" in request.json:
        foundDestination['city'] = request.json['city']
    if 'dov' in request.json:
        foundDestination['dov'] = request.json['dov']
    if 'hospitality' in request.json:
            foundDestination['hospitality'] = request.json['hospitality']
    if 'food' in request.json:
            foundDestination['food'] = request.json['food']
    if 'transport' in request.json:
        foundDestination['transport'] = request.json['transport']
    if 'attractions' in request.json:
            foundDestination['attractions'] = request.json['attractions']
    if 'entertainment' in request.json:
            foundDestination['entertainment'] = request.json['entertainment']
    newDestination = (foundDestination['city'], foundDestination['dov'], foundDestination['hospitality'], foundDestination['food'], foundDestination['transport'], foundDestination['attractions'], foundDestination['entertainment'], foundDestination['id'])
    placesDAO.update(newDestination)
    return jsonify(foundDestination)

# Delete existing destination (by id)
@app.route('/visited/<int:id>', methods = ['DELETE'])
def delete(id):

    if not g.user:
        return redirect(url_for('login'))
    foundDestination = placesDAO.findByID(id)

    if len(foundDestination) == 0:
        return jsonify({}), 404
    
    placesDAO.delete(id)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)
