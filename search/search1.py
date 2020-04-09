from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests

app = Flask(__name__)
api = Api(app)

class Search(Resource):
    def __init__(self):
        pass

    def get(self):
        keyword = request.args.get('keyword')
        with open('data.txt') as json_file:
            data = json.load(json_file)

        print(data)
        for i in data:
            print(i,type(i))
            if i == keyword:
                i['freq']=i['freq']+1
                print("keyword added")
                
            else:
                temp={
                    'keyword': keyword,
                    'freq':1,
                    'time_stamp':'something'
                }
                print(" new keyword added")
        
                with open('data.txt', 'w') as outfile:
                    json.dump(temp, outfile)

api.add_resource(Search,'/')
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
