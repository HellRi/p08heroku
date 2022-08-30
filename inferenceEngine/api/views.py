from flask import Flask, request, make_response

from .tools import Tools

app = Flask(__name__)
tools = Tools()

@app.route('/rest/', methods=['GET', 'POST'])
def incomReq():
    data = request.data

    dataUnSrz = tools.deSerializ(data)

    predMask = tools.predictMask(dataUnSrz)

    result = tools.serializ(predMask)
    print(predMask.shape)
    print(type(result))

    return make_response(result, 200)