from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from json import dumps
from sqlalchemy import create_engine
# post_id
# title
# body

db_connect = create_engine('sqlite:///blog.db')
app = Flask(__name__)
api = Api(app)

class Posts(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select * from posts")
		result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
		conn.close()
		return jsonify(result)

class Post(Resource):
	def post(self):
		blob = request.get_json(force=True)
		title = blob['title']
		body = blob['body']
		conn = db_connect.connect()
		query = conn.execute("insert into posts (title, body) values (?,?)", (title, body)) 
#		return jsonify(request)
		return blob

#@app.route('/post', methods=['POST'])
#@app.route('/posts', methods=['GET'])
api.add_resource(Posts, '/posts') # Route_1
api.add_resource(Post, '/post') # Route_2

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
#	 app.run()
	 app.run(host='192.168.0.33')
