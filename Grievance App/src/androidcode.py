from flask import *
from src.dbconnection import *
app=Flask(__name__)



@app.route('/logincode',methods=['post'])
def logincode():
    un=request.form['uname']
    ps=request.form['pass']
    qry="select * from login where username=%s and password=%s"
    val=(un,ps)
    res=selectone(qry,val)
    if res is None:
        return jsonify({"task":"invalid"})
    else:
        id=res['lid']
        return jsonify({"task": "valid",id:"id"})

@app.route('/sendcomplaint',methods=['post'])
def sendcomplaint():
    compl=request.form['complaint']
    lid=request.form['lid']
    catid=request.form['ctid']

    qry="INSERT INTO `complaint` VALUES(NULL,%s,%s,CURDATE(),%s,'pending','null')"
    val=(str(id),compl,lid,catid)
    iud(qry,val)
    return jsonify({"task": "valid"})


@app.route('/VIEW_CATA',methods=['post'])
def VIEW_CATA():
    # qry="SELECT * FROM `category` WHERE 'type' =%s"
    qry="SELECT * FROM `category` "

    res=selectall2(qry)
    return jsonify(res)



@app.route('/VIEW_type',methods=['post'])
def VIEW_type():
    qry="SELECT * FROM `category` "
    res=selectall(qry)
    return jsonify(res)




app.run(host="0.0.0.0",port=5000)



