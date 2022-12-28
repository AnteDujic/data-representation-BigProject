from flask import Flask, jsonify, request, abort
from dao import placesDAO

app = Flask(__name__, static_url_path='', static_folder='html')

# Implementation

#Home Page
@app.route('/')
def index():
    return app.send_static_file('table.html')

# Get all destinations
@app.route('/visited')
def getAll():
    return jsonify(placesDAO.getAll())

# Get a specific destination
@app.route('/visited/<int:id>')
# ISBN
def findByID(id):
    return jsonify(placesDAO.findByID(id))


# Add a new destination
@app.route('/visited', methods = ['POST'])
def create():
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

# Update
@app.route('/visited/<int:id>', methods = ['PUT'])
def update(id):
    foundDestination = placesDAO.findByID(id)
    print(foundDestination)
    if len(foundDestination) == 0:
        return jsonify({}), 404      
    #newDestination = foundDestination
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

# Delete a gym booking record.
@app.route('/visited/<int:id>', methods = ['DELETE'])
def delete(id):
    foundDestination = placesDAO.findByID(id)
    print(foundDestination)
    if len(foundDestination) == 0:
        return jsonify({}), 404
    placesDAO.delete(id)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)

print(request.json['city'])