from flask import Flask, request, session, g, redirect, url_for,abort, render_template, flash
import database as db
app=Flask(__name__)
app.secret_key="@saurabh_sisodia"
obj=db.make_connection()



@app.route('/')
def show_all_entries():
	global obj
	cursor=obj.show_entries()
	entries=[dict(title=row[0],content=row[1]) for row in cursor.fetchall()]
	return render_template("show_entries.html",entries=entries)



@app.route('/add_new_entry',methods=["POST"])
def add_new_entry():
	global obj
	if not session.get('logged_in'):
		abort(401)
	obj.add_entry(request.form)
	flash('New entry was successfully posted')
	return redirect(url_for('show_all_entries'))

@app.route('/login',methods=["POST","GET"])
def login():
	error=None
	if request.method=="POST":
		if request.form['username']!="saurabh_sisodia":
			error="Invalid Username"
		elif request.form['password']!="sonu_152530":
			error="Invalid Password"
		else:
			session['logged_in']=True
			flash("You were logged in")
			return redirect(url_for('show_all_entries'))
	return render_template("login.html",error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash("You Were Logged Out")
	return redirect(url_for('show_all_entries'))

if __name__=="__main__":
	app.run(debug=True)