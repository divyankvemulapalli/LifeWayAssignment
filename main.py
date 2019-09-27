from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

messages = []

class Message(Resource):

    def post(self):

        message_json = request.get_json()

        for message in messages:
            if (message["id"] == message_json["id"]):
                return "message with id {} already exists".format(message["id"]), 400

        message = {
            "id": message_json["id"],
            "message": message_json["message"],
            "word_count" :  len(message_json["message"].split(' '))
        }
        messages.append(message)

        word_count = 0

        for message in messages:
            word_count = word_count + message["word_count"]

        return {"count": word_count}, 201



api.add_resource(Message, "/message")

if __name__ =='__main__':
    app.run(debug=True)