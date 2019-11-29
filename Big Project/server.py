from flask import Flask, jsonify, request, abort
from runsDAO import runsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

runs=[
    { "id":1, "date":"20/11/19", "name":"Amy", "distance":5.01, "time":0.45},
     { "id":2, "date":"18/11/19", "name":"Sean", "distance":5.01, "time":0.46},
    { "id":3, "date":"27/10/19", "name":"David", "distance":10.01, "time":0.87},
]
nextId=4
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/runs"
@app.route('/runs')
def getAll():
    results = runsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/runs/2"
@app.route('/runs/<int:id>')
def findById(id):
    foundRuns = runsDAO.findByID(id)


    return jsonify(foundRuns)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"date\":\"25/11/19\",\"name\":\"David\",\"distance\":7,\"time\":35}" "http://127.0.0.1:5000/runs"
@app.route('/runs', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    run = {
        "date": request.json['date'],
        "name": request.json['name'],
        "distance": request.json['distance'],
        "time": request.json['time']
    }
    
    runs.append(run)
    return jsonify(run)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
# TODO - update::
# @app.route('/runs/<int:id>', methods=['PUT'])
# def update(id):
#     foundRuns = list(filter(lambda t: t['id']== id, runs))
#     if (len(foundRuns) == 0):
#         abort(404)
#     foundRun = foundBooks[0]
#     if not request.json:
#         abort(400)
#     reqJson = request.json
#     if 'distance' in reqJson and type(reqJson['distance']) is not int:
#         abort(400)

#     if 'Title' in reqJson:
#         foundBook['Title'] = reqJson['Title']
#     if 'Author' in reqJson:
#         foundBook['Author'] = reqJson['Author']
#     if 'Price' in reqJson:
#         foundBook['Price'] = reqJson['Price']
    
#     return jsonify(foundBook)
        

#     return "in update for id "+str(id)

#curl -X DELETE "http://127.0.0.1:5000/runs/4"
@app.route('/runs/<int:id>' , methods=['DELETE'])
def delete(id):
    foundRuns = list(filter(lambda t: t['id']== id, runs))
    if (len(foundRuns) == 0):
        abort(404)
    runs.remove(foundRuns[0])
    return jsonify({"done":True})

#TODO: Finish this
# @app.route('/totalruns/<int:id>' , methods=['POST'])
# def addRun(runnerId):
#     return "in add Run for funner" + str(runnerId)
#TODO: Finish this
# @app.route('/totalruns/leaderboard')
# def getleaderBoard():
#     return "in get leaderBoard"



if __name__ == '__main__' :
    app.run(debug= True)