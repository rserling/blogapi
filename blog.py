from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from json import dumps
from sqlalchemy import create_engine
# CREATE TABLE posts (post_id integer primary key asc autoincrement, title string, body string);

db_connect = create_engine('sqlite:///blog.db')
app = Flask(__name__)
api = Api(app)

class Posts(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select * from posts")
#		return query.cursor.fetchall()
		result = {'posts': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
		conn.close()
		return jsonify(result)

api.add_resource(Posts, '/posts') # Route_1
#api.add_resource(Post, '/post') # Route_2

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	 app.run()
