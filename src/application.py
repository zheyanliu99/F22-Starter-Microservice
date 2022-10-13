from flask import Flask, Response, request
from datetime import datetime
import json
from columbia_student_resource import ColumbiaStudentResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

# CORS(app)
cors = CORS(app, resources={r'/api/*':{'origins':'*'}})


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/api/students/<uni>", methods=["GET"])
def get_student_by_uni(uni):

    result = ColumbiaStudentResource.get_by_key(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    print(result)
    return rsp


@app.route("/api/user/login", methods=["POST"])
def login():
    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    print('AAAAAA')
    print(request.get_json())
    # print(request.form)
    if request.method == 'POST':
        if request.get_json()['email'] == 'test@test.com' and request.get_json()['password'] == '123456':
            result = {'success':True, 'message':'login successful','user_id':'777'}
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else: 
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011, debug=True)

