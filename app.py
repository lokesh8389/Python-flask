from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/user/<name>', methods=['GET'])
def hello(name):
  return 'Hello, My name is %s !' % name

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8080)
