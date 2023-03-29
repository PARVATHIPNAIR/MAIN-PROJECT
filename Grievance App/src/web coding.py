from flask import *
from src.dbconnection import *
app=Flask(__name__)
app.secret_key="cxvbghbjkl"

@app.route("/")
def log():
    return  render_template("loginindex.html")

@app.route('/logincode',methods=['post'])
def logincode():
    un=request.form['textfield']
    ps=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(un,ps)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location='/'</script>'''
    elif res['type']=="admin" :
        return redirect('/adminhome')
    elif res['type']=="student":
        session['lid']=res['lid']
        return redirect('/studenthome')
    elif res['type']=="hostel" :
        session['lid'] = res['lid']
        return redirect('/hostelhome')
    elif res['type']=="staff":
        session['lid'] = res['lid']
        return redirect('/staffhome')
    else:
        return '''<script>alert("invalid");window.location='/'</script>'''

@app.route("/addcategory",methods=['post'])
def Addcategory():
    return  render_template("Add Category.html")


@app.route("/addcategory1",methods=['post'])
def addcategory1():
    category = request.form['textfield']
    type=request.form['textfield2']
    qry3="INSERT INTO category VALUES(NULL,%s,%s)"
    val3=(category,type)
    iud(qry3,val3)
    return '''<script>alert("Added Successfully");window.location='/categorymanagement'</script>'''

@app.route("/delete_category")
def delete_category():
    id=request.args.get('id')
    qry="DELETE FROM `category` WHERE `ctid`=%s"
    iud(qry,id)
    return '''<script>alert("Deleted Successfully");window.location='/categorymanagement#about'</script>'''


@app.route("/addHostel",methods=['post'])
def AddHostel():
    return  render_template("Add Hostel.html")

@app.route("/addHostel1",methods=['post'])
def AddHostel1():
    name = request.form['textfield']
    place = request.form['textfield2']
    pin = request.form['textfield3']
    post = request.form['textfield4']
    phone = request.form['textfield5']
    uname = request.form['textfield6']
    password = request.form['textfield7']
    qry="INSERT INTO login VALUES(NULL,%s,%s,'hostel')"
    val=(uname,password)
    id=iud(qry,val)
    qry1="INSERT INTO hostel VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),name,place,pin,post,phone)
    iud(qry1, val1)
    return '''<script>alert("Added Successfully");window.location='/hostel#about'</script>'''



@app.route("/edit_Hostel")
def edit_Hostel():
    id=request.args.get('id')
    session['EH_id']=id
    qry="SELECT * FROM `hostel` WHERE `lid`=%s"
    res=selectone(qry,id)

    return  render_template("edit_Hostel.html",val=res)

@app.route("/edit_Hostel1",methods=['post'])
def edit_Hostel1():
    name = request.form['textfield']
    place = request.form['textfield2']
    pin = request.form['textfield3']
    post = request.form['textfield4']
    phone = request.form['textfield5']

    qry1="UPDATE `hostel` SET `name`=%s,`place`=%s,`pin`=%s,`post`=%s,`phone`=%s WHERE `lid`=%s"
    val1=(name,place,pin,post,phone,session['EH_id'])
    iud(qry1, val1)
    return '''<script>alert("Edit Successfully");window.location='/hostel#about'</script>'''







@app.route("/delete_Hostel")
def delete_Hostel():
    id=request.args.get('id')
    qry="DELETE FROM `hostel` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry1,id)
    return '''<script>alert("Deleted Successfully");window.location='/hostel#about'</script>'''



@app.route("/addStaff",methods=['post','get'])
def AddStaff():
    return  render_template("Add Staff.html")

@app.route("/addStaff1",methods=['post'])
def addStaff1():
    firstname = request.form['textfield']
    lastname = request.form['textfield2']
    department=request.form['select']
    email = request.form['textfield4']
    phone = request.form['textfield5']
    username=request.form['textfield7']
    password=request.form['textfield6']
    qry="INSERT INTO login VALUES(NULL,%s,%s,'staff')"
    val=(username,password)

    id=iud(qry, val)
    qry4="INSERT INTO staff VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    val4=(str(id),firstname,lastname,department,email,phone)

    iud(qry4, val4)
    return '''<script>alert("Added Successfully");window.location='/staffmanagement#about'</script>'''

@app.route("/edit_staff")
def edit_staff():
    id=request.args.get('id')
    session['ES_id']=id
    qry="SELECT * FROM `staff` WHERE `lid`=%s"
    res=selectone(qry,id)
    return  render_template("edit_Staff.html",val=res)

@app.route("/edit_staff1",methods=['post'])
def edit_staff1():
    firstname = request.form['textfield']
    lastname = request.form['textfield2']
    department=request.form['select']
    email = request.form['textfield4']
    phone = request.form['textfield5']
    qry4="UPDATE `staff` SET `firstname`=%s,`lastname`=%s,`Department`=%s,`email`=%s,`phone`=%s WHERE `lid`=%s"
    val4=(firstname,lastname,department,email,phone,session['ES_id'])
    iud(qry4, val4)
    return '''<script>alert("Edit Successfully");window.location='/staffmanagement#about'</script>'''







@app.route("/delete_staff")
def delete_staff():
    id=request.args.get('id')
    qry="DELETE FROM `staff` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry,id)
    return '''<script>alert("Deleted Successfully");window.location='/staffmanagement#about'</script>'''

@app.route("/addStudent",methods=['post'])
def AddStudent():
    return  render_template("Add Student.html")

@app.route("/addStudent1",methods=['post'])
def AddStudent1():
    firstname = request.form['textfield']
    lastname = request.form['textfield2']
    gender=request.form['radiobutton']
    age = request.form['textfield3']
    department = request.form['select']
    year = request.form['select2']
    email = request.form['textfield4']
    phone = request.form['textfield5']
    type= request.form['select3']
    username=request.form['textfield6']
    password=request.form['textfield7']
    qry = "INSERT INTO login VALUES(NULL,%s,%s,'student')"
    val = (username, password)
    id = iud(qry, val)

    qry2="INSERT INTO student VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val2=(str(id),firstname,lastname,age,gender,department,year,email,phone,type)
    iud(qry2, val2)
    return '''<script>alert("Added Successfully");window.location='/studentmanagement#about'</script>'''


@app.route("/editstudent")
def editstudent():
    id=request.args.get('id')
    session['EST_id']=id
    qry="SELECT * FROM `student` WHERE `lid`=%s"
    res=selectone(qry,id)
    return  render_template("edit_Student.html",val=res)

@app.route("/editstudent1",methods=['post'])
def editstudent1():
    firstname = request.form['textfield']
    lastname = request.form['textfield2']
    age = request.form['textfield3']
    department = request.form['select']
    year = request.form['select2']
    email = request.form['textfield4']
    phone = request.form['textfield5']

    qry2="UPDATE `student` SET `first name`=%s, `last name`=%s,`Age`=%s,`department`=%s,`year`=%s,`email`=%s,`phone`=%s WHERE `lid`=%s"
    val2=(firstname,lastname,age,department,year,email,phone,session['EST_id'])
    iud(qry2, val2)
    return '''<script>alert("Edit Successfully");window.location='/studentmanagement#about'</script>'''






@app.route("/delete_student")
def delete_student():
    id=request.args.get('id')
    qry="DELETE FROM `student` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry1,id)
    return '''<script>alert("Deleted Successfully");window.location='/studentmanagement#about'</script>'''





@app.route("/adminhome")
def Adminhome():
    return  render_template("Admin Home.html")

@app.route("/categorymanagement")
def CategoryManagement():
    q = "SELECT * FROM `category`"
    res = selectall(q)
    return  render_template("Category Management.html",val=res)


@app.route("/complaints")
def Complaints():
    return  render_template("complaints.html")

@app.route("/hostel")
def Hostel():
    q="SELECT * FROM `hostel`"
    res=selectall(q)
    return  render_template("Hostel.html",val=res)

@app.route("/hostelhome")
def HostelHome():
    return  render_template("Hostel Home.html")

@app.route("/manageNotifications")
def ManageNotifications():
    return  render_template("Manage Notification.html")


@app.route("/postComplaints")
def PostComplaints():
    q="SELECT DISTINCT `type` FROM `category`"
    res=selectall(q)
    return  render_template("Post Complaints.html",val=res)

@app.route('/select_category/<d_id>')
def select_category(d_id):

    res = selectall("select * from `category` where `type`='" + str(d_id) + "'")
    print(res)
    return render_template("get_category.html", data=res)

@app.route("/addcomplaint",methods=['post'])
def addcomplaint():
    comp=request.form['textarea']
    ctid=request.form['select2']
    qry="INSERT INTO `complaint` VALUES(NULL,%s,%s,CURDATE(),%s,'pending','null')"
    val=(session['lid'],comp,ctid)
    iud(qry,val)
    return '''<script>alert("Sent");window.location='/studenthome'</script>'''




@app.route("/registerstudent")
def RegisterStudent():
    return  render_template("Register Student.html")

@app.route("/registerstudent1",methods=['post'])
def RegisterStudent1():
    firstname=request.form['textfield']
    lasrname = request.form['textfield2']
    age = request.form['textfield3']
    department = request.form['select']
    year=request.form['select2']
    email = request.form['textfield4']
    phone = request.form['textfield5']
    type=request.form['select3']
    username = request.form['textfield6']
    password = request.form['textfield7']
    qry = "INSERT INTO login VALUES(NULL,%s,%s,'student')"
    val = (username, password)
    id = iud(qry, val)
    qry6 = "INSERT INTO student VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val6 = (str(id),firstname,lasrname, age, department,year,email,phone,type)
    iud(qry6, val6)
    return '''<script>alert("Added Successfully");window.location='/'</script>'''


@app.route("/reportanalysis")
def ReportAnalysis():
    return  render_template("Report and Analysis.html")

@app.route("/sendnotifications")
def SendNotifications():
    return  render_template("Send Notification.html")

@app.route("/sendnotifications1",methods=['post'])
def SendNotifications1():
    noti = request.form['textfield']
    qry="INSERT INTO `notification` VALUES(NULL,CURDATE(),%s)"
    iud(qry,noti)
    return '''<script>alert("Successfull");window.location='adminhome'</script>'''




@app.route("/sendreply")
def SendReply():
    id=request.args.get('id')
    session['cid']=id
    return  render_template("Send Reply.html")

@app.route("/sendreplycode",methods=['post'])
def sendreplycode():
    reply=request.form['textarea']
    q="INSERT INTO `reply` VALUES(NULL,%s,%s,CURDATE())"
    v=(session['cid'],reply)
    iud(q,v)
    qry="UPDATE  `complaint` SET `status`='completed' WHERE `cid`=%s"
    val=(  session['cid'])
    iud(qry,val)
    return '''<script>alert("Successfull");window.location='viewcomplaints'</script>'''



@app.route("/staffhome")
def StaffHome():
    return  render_template("Staff Home.html")

@app.route("/staffmanagement")
def StaffManagement():
    q="SELECT * FROM `staff`"
    res=selectall(q)
    return  render_template("staff management.html",val=res)

@app.route("/studenthome")
def StudentHome():
    return  render_template("Student Home.html")

@app.route("/studentmanagement")
def StudentManagement():
    q="SELECT * FROM `student`"
    res=selectall(q)
    return  render_template("Student management.html",val=res)

@app.route("/verifstudent")
def VerifyStudent():
    return  render_template("verify students.html")

@app.route("/viewcategory")
def ViewCategory():
    return  render_template("View Category.html")


@app.route("/viewcomplaints")
def ViewComplaints():


    return  render_template("View Complaints.html")


@app.route("/viewcomplaints1",methods=['post','get'])
def ViewComplaints1():
    type=request.form['select']
    if type == 'Student':
        qry="SELECT `complaint`.*,`student`.`first name` as fname,category.category FROM `student` JOIN`complaint` ON `complaint`.`lid`=`student`.`lid` JOIN `category` ON `category`.`ctid`=`complaint`.`ctid`"
        res=selectall(qry)
        return  render_template("View Complaints.html",val=res)
    elif type == 'Staff' :
        qry="SELECT `complaint`.*,`staff`.`firstname` as fname,category.category FROM `staff` JOIN`complaint` ON `complaint`.`lid`=`staff`.`lid` JOIN `category` ON `category`.`ctid`=`complaint`.`ctid`"
        res=selectall(qry)
        return render_template("View Complaints.html", val=res)
    elif type == 'Hostel':
        qry="SELECT `complaint`.*,`hostel`.`name` as fname,category.category FROM `hostel` JOIN `complaint` ON `complaint`.`lid`=`hostel`.`lid` JOIN `category` ON `category`.`ctid`=`complaint`.`ctid`"
        res=selectall(qry)
        return render_template("View Complaints.html", val=res)
    else:
        return render_template("View Complaints.html")
    return '''<script>alert("Successfull");window.location='viewcomplaints'</script>'''

@app.route("/viewcomplaintshostel")
def ViewComplaintshostel():


    return  render_template("View Complaintshostel.html")


@app.route("/viewcomplaintshostel1",methods=['post','get'])
def ViewComplaintshostel1():
    type=request.form['select']
    if type == 'Student':
        qry="SELECT `complaint`.*,`student`.`first name` as fname,category.category FROM `student` JOIN`complaint` ON `complaint`.`lid`=`student`.`lid` JOIN `category` ON `category`.`ctid`=`complaint`.`ctid`"
        res=selectall(qry)
        return  render_template("View Complaintshostel.html",val=res)
    elif type == 'Staff' :
        qry="SELECT `complaint`.*,`staff`.`firstname` as fname,category.category FROM `staff` JOIN`complaint` ON `complaint`.`lid`=`staff`.`lid` JOIN `category` ON `category`.`ctid`=`complaint`.`ctid`"
        res=selectall(qry)
        return render_template("View Complaintshostel.html", val=res)
    elif type == 'Hostel':
        qry="SELECT `complaint`.*,`hostel`.`name` as fname,category.category FROM `hostel` JOIN `complaint` ON `complaint`.`lid`=`hostel`.`lid` JOIN `category` ON `category`.`ctid`=`complaint`.`ctid`"
        res=selectall(qry)
        return render_template("View Complaintshostel.html", val=res)
    else:
        return render_template("View Complaintshostel.html")

    return '''<script>alert("Successfull");window.location='viewcomplaintshostel'</script>'''







@app.route("/viewnotification")
def ViewNotification():
    return  render_template("View Notifications.html")

@app.route("/viewreply")
def ViewReply():
    q="SELECT * FROM `complaint` left JOIN `reply` ON `complaint`.`cid`=`reply`.`cid` WHERE `complaint`.`lid`=%s"
    res=selectall2(q,session['lid'])
    return  render_template("View Reply.html", val=res)

@app.route("/viewstudents")
def ViewStudstudentents():
    q = "SELECT * FROM `student` WHERE `type`='Hosteler'"
    res = selectall(q)
    return render_template("View Students.html", val=res)

    return  render_template("View Students.html")

@app.route("/viewstatus")
def ViewStatus():
    q = "SELECT `complaint`.*,`category`.`ctid`,`category`.`category` FROM `category` JOIN `complaint` ON `complaint`.`ctid`=`category`.`ctid` WHERE `category`.`type`='Hostel'"
    res = selectall(q)
    return  render_template("View Status.html",val=res)

@app.route("/register")
def register():
    return  render_template("Register.html")


app.run(debug=True)