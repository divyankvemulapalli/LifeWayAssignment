# REST API using Python and Flask

REST service with a single endpoint that accepts a json message with two fields.."id" and "message". (example: { "id": "123", "message": "hello world" }). The endpoint will return a json with a single field "count" that contains the total number of words contained in all the messages received to that point. For example, if the first message contains 3 words it would responsd with count = 3. If the next message contains 5 words it would respond with count = 8. The service will ignore messages with duplicate ids. (i.e. ids that have already been processed)

Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites:
Python 2.7 or above

Installing packages using pip:
pip install Flask
pip install Flask-RESTful

Deployment:
python /main.py

Postman:
URL: http://127.0.0.1:5000/message, 
JSON(raw) : 
{
  "id" : "123",
  "message" : "hello"
}
