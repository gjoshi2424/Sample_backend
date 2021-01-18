from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
#from random_username.generate import generate_username
import random
app = Flask(__name__)
CORS(app) #
@app.route('/')
def hello_world():
   return 'Hello, world!'
def generate_id():
   return str(random.randint(1, 10000))
#def generate_id():
 #  return generate_username(0)


users = {
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
	if request.method == 'GET':
		search_username = request.args.get('name')
		search_job = request.args.get('job')
		if search_username and search_job:
			subdict = {'users_list' : []}
			for user in users['users_list']:
				if user['name'] == search_username and user['job'] == search_job:
					subdict['users_list'].append(user)
					return subdict
		elif search_username :
			subdict = {'users_list' : []}
			for user in users['users_list']:
				if user['name'] == search_username:
					subdict['users_list'].append(user)
					return subdict
		return users
	elif request.method == 'POST':
	   temp = generate_id()
	   userToAdd = request.get_json()
	   userToAdd['id'] = temp
	   users['users_list'].append(userToAdd)
	   resp = jsonify(success=True)
	   resp.status_code = 201
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response	
	   return resp
	if request.method == 'DELETE':
		search_id = request.args.get('id')
		if search_id:
			for user in users['users_list']:
				if user['id'] == search_id:
					 users['users_list'].remove(user)
			resp = jsonify(success=True)
			resp.status_code = 204
			return resp
		return users
		#if search_username :
		#	print("gets here")
			#for user in users['users_list']:
			#	if user['id'] == search_username:
			#		users['users_list'].remove(user)



'''
@app.route('/users')
def get_users():
   search_username = request.args.get('name') # accessing the value of parameter 'name'
   if search_username:
      subdict = {'users_list' : []}
      for user in users['users_list']:
         if user['name'] == search_username:
            subdict['users_list'].append(user)
      return subdict
   return users

@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users
'''
