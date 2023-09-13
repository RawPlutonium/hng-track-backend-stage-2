from flask import Flask, request, send_file, send_from_directory
from flask_restful import Resource, Api
from pymongo import MongoClient
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)

# Connect to MongoDB
client = MongoClient("mongodb+srv://lgithigi:90293269HNGMongo!@hng.uclfm5h.mongodb.net/?retryWrites=true&w=majority")
db = client["personsdb"]
persons_collection = db["persons"]

class Person(Resource):
    def get(self, user_id):
        # Retrieve a person by user_id
        person = persons_collection.find_one({"_id": user_id})
        if person:
            return person, 200
        else:
            return "Person not found", 404

    def put(self, user_id):
        # Update details of an existing person
        data = request.get_json()
        result = persons_collection.update_one({"_id": user_id}, {"$set": data})
        if result.modified_count > 0:
            return "Person updated successfully", 200
        else:
            return "Person not found", 404

    def delete(self, user_id):
        # Remove a person
        result = persons_collection.delete_one({"_id": user_id})
        if result.deleted_count > 0:
            return "Person deleted successfully", 200
        else:
            return "Person not found", 404

class CreatePerson(Resource):
    def post(self):
        # Create a new person
        data = request.get_json()
        persons_collection.insert_one(data)
        return "Person created successfully", 201

api.add_resource(Person, '/api/<string:user_id>')
api.add_resource(CreatePerson, '/api')

# Serve Swagger UI HTML file
@app.route('/swagger/')
def render_swagger_ui():
    return send_file('index.html')

# Serve Swagger UI static assets
@app.route('/swagger/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
