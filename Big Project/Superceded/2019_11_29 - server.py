from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

runners=[
    { "id":1, "name":"Amy", "totalRuns":5},
    { "id":2, "name":"Sean", "totalRuns":10},
    { "id":3, "name":"David", "totalRuns":15},
    { "id":4, "name":"Jessica", "totalRuns":20},
    { "id":5, "name":"Una", "totalRuns":25},
    { "id":6, "name":"Padraic", "totalRuns":30},
]
nextId=7

#curl "http://127.0.0.1:5000/runners"
@app.route('/runners')
def getAll():
    return jsonify(runners)

#curl "http://127.0.0.1:5000/runners/2"
@app.route('/runners/<int:id>')
def findById(id):
    foundRunners = list(filter(lambda t: t['id'] == id, runners))
    if len(foundRunners) == 0:
        return jsonify ({}) , 204

    return jsonify(foundRunners[0])

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Mary\",\"totalRuns\":7}" "http://127.0.0.1:5000/runners"
@app.route('/runners', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    # other checking 
    runner = {
        "id": nextId,
        "name": request.json['name'],
        "totalRuns": request.json['totalRuns']
    }
    nextId += 1
    runners.append(runner)
    return jsonify(runner)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
# TODO - update::
# @app.route('/runners/<int:id>', methods=['PUT'])
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

#curl -X DELETE "http://127.0.0.1:5000/runners/8"
@app.route('/runners/<int:id>' , methods=['DELETE'])
def delete(id):
    foundRunners = list(filter(lambda t: t['id']== id, runners))
    if (len(foundRunners) == 0):
        abort(404)
    runners.remove(foundRunners[0])
    return jsonify({"done":True})

# curl  -i -H "Content-Type:application/json" -X POST -d "{\"runs\":200}" "http://127.0.0.1:5000/runs/2
@app.route('/runs/<int:runnerId>', methods = ['POST'])
def addRun(runnerId):
    foundRunners=list(filter(lambda t : t['id']==runnerId, runners))
    if len(foundRunners)== 0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'runs' in request.json or type(request.json['runs']) is not int:
        abort(401)
    newRuns = request.json['runs']

    foundRunners[0]['totalRuns'] += newRuns


    return jsonify(foundRunners[0])

@app.route('/runs/leaderboard')
def getleaderBoard():
    runners.sort(key=lambda x: x['totalRuns'], reverse=True)

    return jsonify(runners)



if __name__ == '__main__' :
    app.run(debug= True)