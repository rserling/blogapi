# Blog Post API Assignment

Hello!

There are some python dependencies which will function in virtualenv, I hope that doesn't break the "out of the box" requirement. 

Required: pip install flask flask-jsonpify flask-sqlalchemy flask-restful

Demonstrable thusly:

 * http://63.227.221.94:5000/posts

 * curl -H "Content-Type: application/json" -X POST --data-binary '{"title":"Posting from remote source","body":"This is a post from the internets (Amazon Linux) to the home system"}' http://63.227.221.94:5000/post
