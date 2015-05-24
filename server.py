from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse
from orm import crud
import logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%m-%d %H:%M',)
app = Flask(__name__)
api = Api(app)


class VPSSpeedTestResult(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uri', type=str)
        parser.add_argument('hours', type=int)
        args = parser.parse_args()
        try:
            uri=args['uri']
            hours=args['hours']
        except Exception as e:
            uri=''
            hours=0
        result=crud.getLatestResultHoursAgo(uri,hours)
        logging.info('url %s'%uri)
        ret=[]
        for r in result:
            logging.info('speed %s'%r['speed'])
            ret.append({'speed':r['speed'],'monitorTime':r['monitorTime'].strftime('%Y-%m-%d %H:%M:%S %z')})

        return ret

class VPSUrlList(Resource):
    def post(self):
        return crud.getVPSUrlList()

@app.route('/')
def index():
    return send_from_directory('./html','index.html')
@app.route('/js/<string:jsfile>')
def js(jsfile):
    return send_from_directory('./html/js',jsfile)
@app.route('/css/<string:cssfile>')
def css(cssfile):
    return send_from_directory('./html/css',cssfile)

api.add_resource(VPSSpeedTestResult, '/vpstest')
api.add_resource(VPSUrlList, '/vpsurllist')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5100)