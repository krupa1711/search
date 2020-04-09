from flask import Flask, request
from flask_restful import Resource, Api
import json
import requests
import csv


app = Flask(__name__)
api = Api(app)

class Search(Resource):
    def __init__(self):
        pass

    def get(self):
        keyword = request.args.get('keyword')
        results = []
        flag=True
        with open('example.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                results.append(row)
            
        for i in results:
            if i.get('keyword') == keyword:
                flag=True
                break 
            else:
                flag=False 
                

        if(flag):
            i['frequency']=int(i['frequency'])+1
            with open('example.csv', 'w', newline='') as csvfile:
                fieldnames = ['keyword', 'frequency', 'time_stamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for j in results:
                    writer.writerow(j)                
        else:
            temp={
                'keyword': keyword,
                'frequency':1,
                'time_stamp':'something'
            }
                    
            with open('example.csv', 'a+',newline='') as csvfile:
                fieldnames = ['keyword', 'frequency', 'time_stamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(temp)
            
        return True



api.add_resource(Search,'/search')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005,debug=True)
