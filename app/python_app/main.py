from flask import Flask, send_from_directory, send_file
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = Flask(__name__,)# static_folder='../react_app/build/')

@app.route("/api/collide/")
def collide():
    # print("Called api route")
    client = MongoClient(
        'mongodb://apicollider:A#-G?cc_zGHr.PaWDr8m@mongo:27017/apicollider')
    db = client.apicollider
    apic = db.apis
    document = apic.aggregate([{'$sample': {'size': 2}}])
    apis = []
    for doc in document:
        apis.append(doc)

    # print(apis[0]['title'])
    clean = {'left': {'title': apis[0]['title'], 'description': apis[0]['description']},
             'right': {'title': apis[1]['title'], 'description': apis[1]['description']}}
    apis_json = dumps(clean)
    # apis_json = dumps({'test': 'success'})
    response = app.response_class(
        response=apis_json,
        status=200,
        mimetype='application/json'
    )
    return response

# @app.route("/")
# def main():
#     index_path = os.path.join(app.static_folder, 'index.html')
#     print("Called index route")
#     return send_file(index_path)


# # Everything not declared before (not a Flask route / API endpoint)...
# @app.route('/<path:path>')
# def route_frontend(path):
#     print("Called file route")
#     # ...could be a static file needed by the front end that
#     # doesn't use the `static` path (like in `<script src="bundle.js">`)
#     file_path = os.path.join(app.static_folder, path)
#     if os.path.isfile(file_path):
#         return send_file(file_path)
#     # ...or should be handled by the SPA's "router" in front end
#     else:
#         index_path = os.path.join(app.static_folder, 'index.html')
#         return "ERROR"#send_file(index_path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
