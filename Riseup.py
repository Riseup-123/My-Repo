from flask import Flask,render_template,request,redirect,url_for,session
from DBConnection import Db
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import datetime
import jwt


app = Flask(__name__)
app.secret_key="riseup"


pic_path = "D:\\python_projects\\Riseup\\static\\pics\\"



def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('hello_world'))



@app.route('/login_value',methods=['post'])
def login_value():
    try:
        username=request.form['email']
        password = request.form['password']
        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        db=Db()

        res=db.selectOne("SELECT * FROM `login` WHERE `username`='"+username+"' AND `password`='"+str(password)+"'")
        if res!=None:
            lid=res['login_id']
            session['lid'] = lid
            auth_token = encode_auth_token(lid)

            nn = auth_token.decode('UTF-8')
            print(type(nn))
            db1=Db()
            db1.insert("INSERT INTO `my_token`(`lid`,`token`,`date`)VALUES('"+str(lid)+"','"+nn+"',curdate())")
            return redirect(url_for('home'))
        else:
            return '<script>alert ("Invalid username or password");window.location="/";</script>'
    except Exception as e:
        return str(e)
@app.route('/home')
def home():
    if session.get('lid') is not None:
        return render_template('admin_home.html')
    else:
        return redirect(url_for('hello_world'))


@app.route('/view_req')
def view_req():
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    db=Db()
    res=db.select("SELECT * FROM `requirments`")
    if len(res)>0:
        return render_template('view_req.html',data=res)
    else:
        return '<script>alert ("No data");window.location="/home";</script>'


@app.route('/view_req_update/<id>')
def view_req_update(id):
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    db=Db()
    db.update("UPDATE `requirments` SET `status`='completed' WHERE `requirments_id`='"+id+"'")
    return '<script>alert ("Updated");window.location="/view_req";</script>'



@app.route('/add_timeline')
def add_timeline():
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    return render_template('add_timeline.html')


@app.route('/add_timeline_value',methods=['post'])
def add_timeline_value():
    name=request.form['name']
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    url = request.form['url']
    pic = request.files['pic']
    db=Db()
    pic.save(pic_path+pic.filename)
    db.insert("INSERT INTO `timeline`(`name`,`date`,`url`,`pic`,month,year)VALUES('"+name+"','"+date+"','"+url+"','"+pic.filename+"','"+month+"','"+year+"')")
    return '<script>alert ("Success");window.location="/home";</script>'


@app.route('/view_timeline')
def view_timeline():
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    db=Db()
    res=db.select("SELECT * FROM `timeline` WHERE `status`='active'")
    if len(res)>0:
        return render_template('view_timeline.html',data=res)
    else:
        return '<script>alert ("No data");window.location="/home";</script>'


@app.route('/delete_timeline/<id>')
def delete_timeline(id):
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    db=Db()
    db.update("UPDATE `timeline` SET `status`='inactive' WHERE `timeline_id`='"+id+"'")
    return '<script>alert ("Deleted");window.location="/view_timeline";</script>'


@app.route('/update_timeline/<id>')
def update_timeline(id):
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    render_template('update_timeline.html',tid=id)


@app.route('/edit_timeline_value',methods=['post'])
def edit_timeline_value():
    name=request.form['name']
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    url = request.form['url']
    tid = request.form['tid']
    db=Db()
    db.update("UPDATE `timeline` SET `name`='"+name+"',`date`='"+date+"',`month`='"+month+"',`year`='"+year+"',`url`='"+url+"' WHERE `timeline_id`='"+tid+"'")
    return '<script>alert ("Updated...");window.location="/home";</script>'


@app.route('/add_news')
def add_news():
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    return render_template('add_news.html')


@app.route('/add_news_value',methods=['post'])
def add_news_value():
    subject=request.form['subject']
    content = request.form['content']
    url = request.form['url']
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    credit = request.form['credit']
    db=Db()
    db.insert("INSERT INTO `news`(`subject`,`content`,`url`,`date`,`credit`,month,year)VALUES('"+subject+"','"+content+"','"+url+"','"+date+"','"+credit+"','"+month+"','"+year+"')")
    return '<script>alert ("Success");window.location="/home";</script>'


@app.route('/view_news')
def view_news():
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    db=Db()
    res=db.select("SELECT * FROM `news` WHERE `status`='active'")
    if len(res)>0:
        return render_template('view_news.html',data=res)
    else:
        return '<script>alert ("No data");window.location="/home";</script>'


@app.route('/delete_news/<id>')
def delete_news(id):
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    db=Db()
    db.update("UPDATE `news` SET `status`='inactive' WHERE `news_id`='"+id+"'")
    return '<script>alert ("Deleted");window.location="/view_news";</script>'


@app.route('/update_news/<id>')
def update_news(id):
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    render_template('update_news.html',nid=id)


@app.route('/edit_news_value',methods=['post'])
def edit_news_value():
    subject=request.form['subject']
    content = request.form['content']
    url = request.form['url']
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    credit = request.form['credit']
    nid = request.form['nid']
    db=Db()
    db.update("UPDATE `news` SET `subject`='"+subject+"',`content`='"+content+"',`url`='"+url+"',`credit`='"+credit+"',`date`='"+date+"',`month`='"+month+"',`year`='"+year+"' WHERE `news_id`='"+nid+"'")
    return '<script>alert ("Updated...");window.location="/home";</script>'



@app.route('/add_mem')
def add_mem():
    if session.get('lid') is None:
        return redirect(url_for('hello_world'))
    return render_template('member_registration.html')


@app.route('/member_reg',methods=['post'])
def member_reg():
    phone = request.form['phone']
    email = request.form['email']
    # password = generate_password_hash(phone, method='sha256')
    password = hashlib.md5(phone.encode())
    password = password.hexdigest()
    db=Db()
    db1=Db()
    rr=db1.selectOne("SELECT * FROM `login` WHERE `username`='"+email+"'")
    if rr!=None:
        return '<script>alert ("Already exist email....");window.location="/home";</script>'
    else:
        lid=db.insert("INSERT INTO `login`(`username`,`password`)VALUES('"+email+"','"+str(password)+"')")

    return '<script>alert ("Success");window.location="/home";</script>'

if __name__ == '__main__':
    app.run()
