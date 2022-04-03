from Flask_server import app
from flask import jsonify 


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return  jsonify([
        {
            "img": "image1.jpg",
            "name": "Ashluxe Men Wear",
            "type": "Hoodie",
            "price":79.06

        },
        {
            "img": "image2.jpg",
            "name": "Ashluxe Women Wear",
            "type": "OverSized Gown",
            "price":32.00
        }
    ])

