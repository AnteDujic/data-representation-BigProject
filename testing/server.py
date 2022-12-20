from flask import Flask, jsonify
# import dao

app = Flask(__name__, static_url_path='', static_folder='html')

# Implementation

places = [
    {
        'city':'Zadar',
        'date': 'Jan 2015',
        'rating': 'Brilliant',
    }
]




if __name__ == "__main__":
    app.run (debug = True)