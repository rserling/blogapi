# Blog Post API Assignment

Hello!

There are some python dependencies which will function in virtualenv, I hope that doesn't break the "out of the box" requirement. 
Required: 
\$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful

Demonstrable thusly:

 * http://63.227.221.94:5000/posts

 * \$ curl -H "Content-Type: application/json" -X POST --data-binary '{"title":"This is Clickbait","body":"Replace this text with your own verbose and eloquent verbiage"}' http://63.227.221.94:5000/post

Known Issues:
 * Lacks a full suite of internal error handling
 * IRL it would probably would have input testing for JSON compliance
