from flask import Flask, jsonify, request, abort
from runsDAO import runsDAO

app = Flask(__name__, static_url_path='', static_folder='.')


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
    values = (run['date'],run['name'],run['distance'],run['time'])
    newId = runsDAO.create(values)
    run['id'] = newId
    return jsonify(run)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"date\":\"19/6/23\",\"name\":\"Donal\",\"distance\":5,\"time\":25}" http://127.0.0.1:5000/runs/1
@app.route('/runs/<int:id>', methods=['PUT'])
def update(id):
    foundRuns = runsDAO.findByID(id)
    if not foundRuns:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    if 'distance' in reqJson and type(reqJson['distance']) is not float:
        abort(400)
    if 'time' in reqJson and type(reqJson['time']) is not float:
        abort(400)        

    if 'date' in reqJson:
        foundRuns['date'] = reqJson['date']
    if 'name' in reqJson:
        foundRuns['name'] = reqJson['name']
    if 'distance' in reqJson:
        foundRuns['distance'] = reqJson['distance']
    if 'time' in reqJson:
        foundRuns['time'] = reqJson['time']
    values = (foundRuns['date'],foundRuns['name'],foundRuns['distance'],foundRuns['time'],foundRuns['id'])
    runsDAO.update(values)
    return jsonify(foundRuns)
        

#curl -X DELETE "http://127.0.0.1:5000/runs/4"
@app.route('/runs/<int:id>' , methods=['DELETE'])
def delete(id):
    runsDAO.delete(id)
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