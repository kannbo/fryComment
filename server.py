from bottle import *
import datetime
website={"sample":{"page":[{"name":"hello","text":"hello"}],"password":None}}
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
@get('/')
def hello():
    return """
<title>コメント欄作成</title><h1>flyComment</h1>
<form action="/create" method="POST">url
<input name="name" type="text"　maxlength="20"><br>作成パスワード<input name="password" type="text"><br>
<input type="submit" value="作成する">
</form>
<div id="manu">
</div>
<link rel="stylesheet" href="https://kannbo.github.io/fryComment/css.css">
<script src="https://kannbo.github.io/fryComment/main.page.js"></script>
<a href="https://flychats.onrender.com">FlyChat(チャットサービス)</a><a href="https://flyapp.onrender.com">FlyApp(web作成)</a>
"""
@post('/create')
def hello2():
    global website
    try:
        website[request.forms.name]
        print(request.forms.name)
        return """<link rel="stylesheet" href="https://kannbo.github.io/fryComment/css.css2">失敗"""
    except:
        if not "/" in request.forms.name and not request.forms.name=="" and not " " in request.forms.name:
            website[request.forms.name]={"page":{},"password":request.forms.password}
            return f"""<title>成功 | {request.forms.name}</title><link rel="stylesheet" href="https://kannbo.github.io/fryComment/css.css2">成功しかした /comment/{request.forms.name}/id_make"""
        else:
            print(request.forms.name)
            return f"""<link rel="stylesheet" href="https://kannbo.github.io/fryComment/css.css2">失敗"""
@get("/comment/<name>/id_make")
def id_create(name):
    return f"""
<title>作成画面</title>
<form action="/comment/{name}/id_make" method="POST">ID
<input name="name" type="text"　maxlength="20"><br>
作成パスワード<input name="password" type="text"><br>
<input type="submit" value="作成する">
</form>
<div id="manu2">
</div>
<link rel="stylesheet" href="https://kannbo.github.io/fryComment/css.css">
<script src="https://kannbo.github.io/fryComment/main.page.js"></script>
"""
@post("/comment/<name>/id_make")
def id_create_c(name):
    global website
    if not "/" in request.forms.name and not request.forms.name=="" and not " " in request.forms.name and website[name]["password"]==request.forms.password:
        website[name]["page"][request.forms.name]=[]
        return "作成完了"
    else:
        return "エラー"
aaaaa=""
@route(f"/password/list/kannbo/{aaaaa}")
def lists():
    global website
    return website
@route("/comment/<name>/<ids>/json")
def aaaaaa(name,ids):
    global website
    body = {"message": "OK"}
    HTTPResponse(status=200, body=body, headers={"Access-Control-Allow-Origin":"*"})
    return str(website[name]["page"][ids])
@route("/comment/<name>/<ids>/html/<html:path>")
def aaaaaa(name,ids,html):
    global website
    aaaaaaa=""
    body = {"message": "OK"}
    HTTPResponse(status=200, body=body, headers={"Access-Control-Allow-Origin":"*"})
    for i in website[name]["page"][ids]:
        aaaaaaa=aaaaaaa+html.replace("$time",i["time"]).replace("$name",i["name"]).replace("$text",i["text"])
    return aaaaaaa
@post("/comment/<name>/<ids>/add/<path:path>")
def addpage(name,ids,path):
    global website
    website[name]["page"][ids].append({"time":str(datetime.datetime.now()),"name":request.forms.name,"text":request.forms.text})
    return f"""<meta http-equiv="refresh"content="0;URL={path}">"""
@route("/css")
def css():
    return """
chat{
  display:block;
  font-size:150%;
  margin:10% 20% 20% 20%;
}
chat>*{
  width: auto;
}
chat>form>textarea{
  font-size:75%;
　width: 50vh;
　height: 30vh;
  resize: none;
}
chat>form{
  width: 100%;
　height: 100%;
}
flex{
  display:flex;
}
flex>button{
  margin-top:8%;
  margin-left:3%;
  height: 30%;
  font-size:20%;
}
  """

run(host='0.0.0.0', port="10000",)
