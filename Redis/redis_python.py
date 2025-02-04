import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')
r.set('user:1:name', 'John Doe')
r.set('user:1:email', 'john.doe@example.com')
r.setex('session_key', 3600, 'session_data')

user_name = r.get('user:1:name')
user_email = r.get('user:1:email')

user_name = user_name.decode('utf-8')
user_email = user_email.decode('utf-8')

keys = ['user:1:name', 'user:1:email']
values = r.mget(keys)
values = [value.decode('utf-8') for value in values]