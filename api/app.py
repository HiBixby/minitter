from flask import Flask, request, jsonify

app               = Flask(__name__)
app.users         = {}
app.id_count      = 1
app.tweets        = []


@app.route("/")
def index():
  return "Hello Flask!" 
  
@app.route("/ping",methods=['GET'])
def ping():
  return "pong"

@app.route("/sign-up",methods=['POST'])
def sign_up():
  new_user                    = request.json
  new_user["id"]              = app.id_count
  app.users[app.id_count]     = new_user
  app.id_count                = app.id_count + 1
  return jsonify(new_user)


@app.route('/tweet', methods=['POST'])
def tweet():
  payload=request.json
  user_id=int(payload['id'])
  tweet=payload['tweet']

  if user_id not in app.users:
    return '사용자가 존재하지 않습니다',400

  if len(tweet)>300:
    return '300자를 초과했습니다',400

  user_id=int(payload['id'])

  app.tweets.append({
    'user_id':user_id,
    'tweet': tweet
  })
  return '',200



app.run(host='0.0.0.0', port=5000)