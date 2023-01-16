from flask import Flask, render_template , request , session ,jsonify,Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from dateutil.relativedelta import relativedelta
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
import os 
import io
import xlwt
import json


# http://localhost:8080/phpmyadmin/

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

if params['local_server']:
	app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)
app.secret_key = params['secret_key']
app.config['UPLOAD_FOLDER'] = params['UPLOAD_FOLDER']

# pdyypnwmzcdebfbx

# def create_ID(transporter,role,):


@app.route("/")
def home():
    user_id = request.cookies.get('YourSessionCookie')
    if user_id:
        user = params['User']
        if user:
            # Success!
            return render_template('dashboard.html')
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))



# login page
@app.route("/login", methods = ['GET','POST'])
def login():
	msg = "user or passwrod did not match"
	if request.method == 'POST':
		username = request.form['user']
		password = request.form['pass']
		if (username == params['User'] and password == params['PWD']):
			session['user'] = username
			emp = employee.query.all()
			for i in emp :
				try :
					print(i.Drive_License_Validity)
					# if i.Drive_License_Validity is not '0000-00-00':
					if datetime.strptime(str(i.Drive_License_Validity), '%y-%m-%d') < datetime.now():
						act = activity.query.filter_by(Unique_ID =  i.Unique_ID).first()
						act.Avaialbility= 'No'
						db.session.commit()
				except:
					pass
			response = redirect(url_for("dashboard"))
			response.set_cookie('YourSessionCookie', username)
			return response
		else :
			flash("User or Password not correct", "error")
			return render_template("login.html")

	return render_template("login.html")




@app.route("/logout")
def logout():
	try :
		session.pop('user')
	except :
		return render_template("login.html")
	return render_template("login.html")



@app.route("/dashboard")
def dashboard():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	return render_template('dashboard.html')
	




# shipment form
@app.route("/shipment", methods = ['GET','POST'])
def shipment():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))

	Driver = activity.query.filter_by(Role='Driver', On_Shipment = 'No',Avaialbility = 'Yes' , Active = 'Yes')
	Dispatcher = activity.query.filter_by(Role='Dispatcher', On_Shipment = 'No',Avaialbility = 'Yes', Active= 'Yes')
	Transport = transport.query.all()
	print("Driver")
	print(Driver)

	if request.method == 'POST':
		s= []
		ShipmentNo = request.form['Shipment_No']
		Vehicle_No = request.form['Vehicle_No']
		Shipment_Type = request.form['Shipment_Type']
		Pilot_unique_ID = request.form['Pilot_unique_ID']
		Copilot_unique_ID = request.form['Copilot_unique_ID']
		Dispatcher_unique_ID = request.form['Dispatcher_unique_ID']
		Transporter = request.form['Transporter']


		post = shipment.query.filter_by(Shipment_No=ShipmentNo).first()

		if Copilot_unique_ID :
			s.append(Pilot_unique_ID)
			s.append(Copilot_unique_ID)
			s.append(Dispatcher_unique_ID)
		else:
			s.append(Pilot_unique_ID)
			Copilot_unique_ID = 'No'
			s.append(Dispatcher_unique_ID)
			

		if post :
			flash("Shipment number already exist", "error")
			return redirect(request.path,code=302) 
		else:
			print("Shipment_Type")
			print(Shipment_Type)
			entry = shipment(Shipment_No = ShipmentNo, Vehicle_No= Vehicle_No, Shipment_Type= Shipment_Type,
				Pilot_unique_ID= Pilot_unique_ID,Copilot_unique_ID= Copilot_unique_ID,
				Dispatcher_unique_ID= Dispatcher_unique_ID,Transporter= Transporter, Add_Time= datetime.now())
			 # , End_Time = datetime.now())
				 # ,Add_Time= Add_Time, End_Time= End_Time)

			print(entry)
			db.session.add(entry)
			db.session.commit()
			print(s)
			for i in s:
				print()
				post = activity.query.filter_by(Unique_ID=i).first()
				print("poastaaaa")
				print(post.On_Shipment)
				post.On_Shipment= 'Yes'
				db.session.commit()
			flash("Shipping Successful")
			return redirect(request.path,code=302) 
	return render_template("shipment.html", Driver=Driver , Dispatcher=Dispatcher , Transport =Transport)


SNo = None


# complete
# add ship end time
@app.route("/end_ship", methods = ['POST','GET'])
def end_ship():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	print("yuppiess")
	global SNo
	if request.method == 'POST':
		SNo = request.form['sno']
		print("post")
		print(SNo)
		post = shipment.query.filter_by(Shipment_No=SNo).first()
		if SNo and post:
			# post = shipment.query.filter_by(Shipment_No=SNo).first()
			post.End_Time = datetime.now()
			return render_template("end_ship.html", shipment=post)
		else:
			SNo = 0
			post = shipment.query.filter_by(Shipment_No=SNo).first()
			# post.End_Time = datetime.now()
			flash("Shipment number not correct")
			return render_template("end_ship.html", shipment=post)

	if request.method == 'GET':
		print("get")
		print(SNo)
		if SNo:
			print("yayuy")
			post = shipment.query.filter_by(Shipment_No=SNo).first()

			post.End_Time = datetime.now()
			# db.session.commit()

			p1 = activity.query.filter_by(Unique_ID = post.Pilot_unique_ID).first()
			p1.On_Shipment = 'No'
			p1.Last_shipment_date =  post.End_Time
			p2 = activity.query.filter_by(Unique_ID = post.Copilot_unique_ID).first()
			if p2 :
				p2.On_Shipment = 'No'
				p2.Last_shipment_date =  post.End_Time
			d1 = activity.query.filter_by(Unique_ID = post.Dispatcher_unique_ID).first()
			d1.On_Shipment = 'No'
			d1.Last_shipment_date =  post.End_Time
			db.session.commit()
			SNo = 0

			return render_template("end_ship.html", shipment=post)
		
		else:
			print("hola")
			SNo = 0
			post = shipment.query.filter_by(Shipment_No=SNo).first()
			print(post)
			# post.End_Time = datetime.now()
			# flash("Shipment number not correct")
			return render_template("end_ship.html", shipment=post)

	print("hola")
	SNo = 0
	post = shipment.query.filter_by(Shipment_No=SNo).first()
	print(post)
	# post.End_Time = datetime.now()
	# flash("Shipment number not correct")
	return render_template("end_ship.html", shipment=post)


# driver form
@app.route("/driver", methods = ['GET','POST'])
def driver():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	print("uuuuu")
	Tran = transport.query.all()
	if request.method == 'POST':
		print("YOOOOOOOO")

		# Unique_ID = request.form['Unique_ID']
		Date_of_Onboard = request.form['Date_of_Onboard']
		First_Name = request.form['First_Name']
		Middle_Name = request.form['Middle_Name']
		Last_Name = request.form['Last_Name']
		Transporter = request.form['Transporter']
		Role = request.form['Role']
		Address_1 = request.form['Address_1']
		Address_2 = request.form['Address_2']
		City = request.form['City']
		State = request.form['State']
		Zip_Code = request.form['Zip_Code']
		Mobile_No = request.form['Mobile_No']
		DOB = request.form['DOB']
		Emergency_Contact_Person = request.form['Emergency_Contact_Person']
		Emergency_Contact_No = request.form['Emergency_Contact_No']
		Blood_Group = request.form['Blood_Group']
		Marital_Status = request.form['Marital_Status']
		Spouse_Name = request.form['Spouse_Name']
		No_of_Children = request.form['No_of_Children']
		Aadhar_Number = request.form['Aadhar_Number']
		PAN_Number = request.form['PAN_Number']
		Driving_License_Number = request.form['Driving_License_Number']
		Driving_License_Type = request.form['Driving_License_Type']
		DLV = request.form['Drive_License_Validity']
		Vaccination_Name = request.form['Vaccination_Name']
		Dose1_Date = request.form['Dose1_Date']
		Dose2_Date = request.form['Dose2_Date']
		Booster_Dose_Date = request.form['Booster_Dose_Date']
		Education_Qualification = request.form['Education_Qualification']
		Aadhar_Attachment = request.files['Aadhar_Attachment']
		PANCard_Attachment = request.files['PANCard_Attachment']
		Driver_Lic_Attachment = request.files['Driver_Lic_Attachment']
		Vaccination_Certi_Attachment = request.files['Vaccination_Certi_Attachment']
		Photo_Attachment = request.files['Photo_Attachment']

		
		obj = employee.query.all()
		uni_code = 0
		for i in obj:
			a = int(i.Unique_ID[-4:])
			if a > uni_code :
				uni_code = a
		tran = transport.query.filter_by(Transporter = Transporter).first()

		# print(tran.Transporter_ID )
		# print(uni_code)
		uni_code += 1 
		print("uni_code")
		print(uni_code)
		if Role == 'Driver':
			R = 'P'
		else :
			R = 'D'
		S = 'C008'+tran.Transporter_ID[-3:]+R+ str(uni_code).zfill(4)
		print(S)
		print(S)
		user_folder = os.path.join(app.config['UPLOAD_FOLDER'], S)
		print(user_folder)
		os.makedirs(user_folder)
		if Aadhar_Attachment :
			Aadhar_Attachment.save(join(user_folder, secure_filename(Aadhar_Attachment.filename)))
			Aadhar_Attachment = "Yes"
		if PANCard_Attachment :
			PANCard_Attachment.save(join(app.config['UPLOAD_FOLDER']+'\\'+S, secure_filename(PANCard_Attachment.filename)))
			PANCard_Attachment = "Yes"
		else:
			PANCard_Attachment = "No"
		if Driver_Lic_Attachment :
			Driver_Lic_Attachment.save(join(app.config['UPLOAD_FOLDER']+'\\'+S, secure_filename(Driver_Lic_Attachment.filename)))
			Driver_Lic_Attachment = "Yes"
			Drive_License_Validity = (datetime.strptime(DLV,"%Y-%m").date() + relativedelta(day=31))
		else:
			Driver_Lic_Attachment = "No"
		if Vaccination_Certi_Attachment :
			Vaccination_Certi_Attachment.save(join(app.config['UPLOAD_FOLDER']+'\\'+S, secure_filename(Vaccination_Certi_Attachment.filename)))
			Vaccination_Certi_Attachment = "Yes"
		if Photo_Attachment :
			Photo_Attachment.save(join(app.config['UPLOAD_FOLDER'] +'\\'+S, secure_filename(Photo_Attachment.filename)))
			Photo_Attachment = "Yes"
		

		print("S being printed")
		print(S)
		Drive_License_Validity = DLV
		entry = employee(
			Unique_ID = S , 
			Date_of_Onboard= Date_of_Onboard,
		 First_Name= First_Name,Middle_Name= Middle_Name,
		 Last_Name= Last_Name, Transporter= Transporter,Role= Role,
		 Address_1= Address_1,Address_2=Address_2,City=City,State=State,Zip_Code=Zip_Code, Mobile_No= Mobile_No, 
		 DOB= DOB,Emergency_Contact_Person= Emergency_Contact_Person,
		 Emergency_Contact_No= Emergency_Contact_No, Blood_Group= Blood_Group,Marital_Status= Marital_Status,
		 Spouse_Name= Spouse_Name,No_of_Children= No_of_Children,
		 Aadhar_Number= Aadhar_Number,
		 PAN_Number= PAN_Number,
		 Driving_License_Number= Driving_License_Number,Driving_License_Type= Driving_License_Type,
		 Drive_License_Validity= Drive_License_Validity,
		 Vaccination_Name= Vaccination_Name,
		 Dose1_Date= Dose1_Date,Dose2_Date= Dose2_Date,Booster_Dose_Date= Booster_Dose_Date,
		 Education_Qualification= Education_Qualification,Aadhar_Attachment= Aadhar_Attachment,
		 PANCard_Attachment= PANCard_Attachment,
		 Driver_Lic_Attachment= Driver_Lic_Attachment,
		 Vaccination_Certi_Attachment= Vaccination_Certi_Attachment,Photo_Attachment= Photo_Attachment)


		print(entry)
		db.session.add(entry)
		db.session.commit()


		act_entry = activity(Unique_ID = S,Role = Role, BGV = 'No', Active = 'Yes', Avaialbility = 'No', Last_shipment_date = datetime.now(), Last_shipment_day = '', On_Shipment = 'No', Blacklisted = 'No')
		print(entry)
		db.session.add(act_entry)
		db.session.commit()

		flash(Role +" added Successful")
		return redirect(request.path,code=302)
	return render_template("driver.html", Transport=Tran)




 
 # update in shipment
@app.route("/ajax_update",methods=['POST','GET'])
def ajax_update():
	print("cooollll")
	msg = "yoo"
	if request.method == 'POST': 
		msg = 'update done'
		field = request.form['field']
		value = request.form['value']
		editid = request.form['id']

		
		try:
			post = shipment.query.filter_by(Shipment_No=editid).first()
			if field == 'Vehicle_No' :
				post.Vehicle_No = value
			elif field == 'Shipment_Type' :
				post.Shipment_Type = value
			elif field == 'Pilot_unique_ID' :
				post.Pilot_unique_ID = value
			elif field == 'Copilot_unique_ID' :
				post.Copilot_unique_ID = value
			elif field == 'Dispatcher_unique_ID' :
				post.Dispatcher_unique_ID = value
			elif field == 'Transporter' :
				post.Transporter = value

			db.session.commit()
			msg = 'Record successfully Updated'
		except :
			msg = 'shipment number is not changable'
			return jsonify(msg)
	return jsonify(msg)



 # update in driver
@app.route("/ajax_driver_update",methods=['POST'])
def ajax_driver_update():
	print("drive away")
	if request.method == 'POST':
		field = request.form['field']
		value = request.form['value']
		editid = request.form['id']

		print(field)
		print(value)
		print(editid)
		
		try:
			post = employee.query.filter_by(Unique_ID=editid).first()
			if field == 'Date_of_Onboard' :
				post.Date_of_Onboard = value
			elif field == 'First_Name' :
				post.First_Name = value
			elif field == 'Middle_Name' :
				post.Middle_Name = value
			elif field == 'Last_Name' :
				post.Last_Name = value
			elif field == 'Transporter' :
				post.Transporter = value
				# tran = transport.query.filter_by(Transporter=value).first()
				# if tran :
				# 	post.Transporter = value
				# 	new = employee.query.filter_by(Unique_ID=editid).first()
				# 	new.Unique_ID = 
			elif field == 'Role' :
				post.Role = value
			elif field == 'Address_1' :
				post.Address_1 = value
			elif field == 'Address_2' :
				post.Address_2 = value
			elif field == 'City' :
				post.City = value
			elif field == 'State' :
				post.State = value
			elif field == 'Zip_Code' :
				post.Zip_Code = value
			elif field == 'Mobile_No' :
				post.Mobile_No = value
			elif field == 'Emergency_Person' :
				post.Emergency_Person = value
			elif field == 'Emergency_Contact_No' :
				post.Emergency_Contact_No = value
			elif field == 'Spouse_Name' :
				post.Spouse_Name = value
			elif field == 'No_of_Children' :
				post.No_of_Children = value
			elif field == 'Driving_License_Number' :
				post.Driving_License_Number = value
			elif field == 'Driving_License_Type' :
				post.Driving_License_Type = value
			elif field == 'Drive_License_Validity' :
				post.Drive_License_Validity = value
			elif field == 'Vaccination_Name' :
				post.Vaccination_Name = value
			elif field == 'Dose1_Date' :
				post.Dose1_Date = value
			elif field == 'Dose2_Date' :
				post.Dose2_Date = value
			elif field == 'Booster_Dose_Date' :
				post.Booster_Dose_Date = value

			db.session.commit()
			success = 1
			return jsonify(success)
		except Exception as e:
			print(e)
   


@app.route("/ajax_activity_update",methods=["POST","GET"])
def ajax_activity_update():
    try:
        if request.method == 'POST':
            field = request.form['field'] 
            value = request.form['value']
            editid = request.form['id']
            
            print(field)
            print(value)
            print(editid)
            try:
            	post = activity.query.filter_by(Unique_ID=editid).first()
            	if field == 'BGV' :
            		post.BGV = value
            	elif field == 'Active' :
            		post.Active = value
            	elif field == 'Blacklisted' :
            		post.Blacklisted = value

            	if post.BGV == 'Yes' and post.Blacklisted == 'No':
            		post.Avaialbility = 'Yes'
            	else:
            		post.Avaialbility = 'No'
            except Exception as e:
            	print(e)
            	print("fool")

            db.session.commit()

            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)



# shipment list
@app.route("/ship_list", methods= ["GET","POST"])
def ship_list():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	ships = shipment.query.all()
	print(ships)
	if request.method == 'GET':
		return render_template("ship_list.html", shipment=ships)
	return render_template("ship_list.html")	


# driver list
@app.route("/driver_list", methods= ["GET","POST"])
def driver_list():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	emp = employee.query.all()
	if request.method == 'GET':
		return render_template("driver_list.html", employee=emp)
	return render_template("driver_list.html")	


# activity list
@app.route("/activity_list", methods= ["GET","POST"])
def activity_list():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	act = activity.query.all()

	for u in act :
		if u.On_Shipment == 'No' :
			ship_date = datetime.strptime(u.Last_shipment_date,'%m/%d/%Y').date()
			delta = datetime.now() - ship_date
			u.Last_shipment_day = delta.days



	if request.method == 'GET':
		return render_template("activity_list.html", activity=act)
	return render_template("activity_list.html")	





# download_driver_report
@app.route("/download/driver_report/pdf" , methods=["GET","POST"])
def download_Driver_report():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	if request.method == 'GET':
		driver = employee.query.all()
		act = activity.query.all()


		print()
		output = io.BytesIO()
		WORKBOOK = xlwt.Workbook()
		sh = WORKBOOK.add_sheet('report')


		sh.write( 0,0,'Unique_ID')
		sh.write( 0,1,'Date_of_Onboard')
		sh.write( 0,2,'First_Name')
		sh.write( 0,3,'Middle_Name')
		sh.write( 0,4,'Last_Name')
		sh.write( 0,5,'Transporter')
		sh.write( 0,6,'Role')
		sh.write( 0,7,'Address_1')
		sh.write( 0,8,'Address_2')
		sh.write( 0,9,'City')
		sh.write( 0,10,'State')
		sh.write( 0,11,'Zip_Code')
		sh.write( 0,12,'Mobile_No')
		sh.write( 0,13,'DOB')
		sh.write( 0,14,'Emergency_Contact_Person')
		sh.write( 0,15,'Emergency_Contact_No')
		sh.write( 0,16,'Blood_Group')
		sh.write( 0,17,'Marital_Status')
		sh.write( 0,18,'Spouse_Name')
		sh.write( 0,19,'No_of_Children')
		sh.write( 0,20,'Aadhar_Number')
		sh.write( 0,21,'PAN_Number')
		sh.write( 0,22,'Driving_License_Number')
		sh.write( 0,23,'Driving_License_Type')
		sh.write( 0,24,'Drive_License_Validity')
		sh.write( 0,25,'Vaccination_Name')
		sh.write( 0,26,'Dose1_Date')
		sh.write( 0,27,'Dose2_Date')
		sh.write( 0,28,'Booster_Dose_Date')
		sh.write( 0,29,'Education_Qualification')
		sh.write( 0,30,'Aadhar_Attachment')
		sh.write( 0,31,'PANCard_Attachment')
		sh.write( 0,32,'Driver_Lic_Attachment')
		sh.write( 0,33,'Vaccination_Certi_Attachment')
		sh.write( 0,34,'Photo_Attachment')
		sh.write( 0,35,'BGV')
		sh.write( 0,36,'Active')
		sh.write( 0,37,'Avaialbility')
		sh.write( 0,38,'Last_shipment_date')
		sh.write( 0,39,'Last_shipment_day')
		sh.write( 0,40,'On_Shipment')
		sh.write( 0,41,'Blacklisted')


		idx = 0
		print("olaa")
		# print(type(driver[1]))
		print(act)
		for row in driver:
			print(row)
			sh.write(idx+1,0, str(row.Unique_ID))
			sh.write(idx+1,1, str(row.Date_of_Onboard))
			sh.write(idx+1,2, str(row.First_Name))
			sh.write(idx+1,3, str(row.Middle_Name))
			sh.write(idx+1,4, str(row.Last_Name))
			sh.write(idx+1,5, str(row.Transporter))
			sh.write(idx+1,6, str(row.Role))
			sh.write(idx+1,7, str(row.Address_1))
			sh.write(idx+1,8, str(row.Address_2))
			sh.write(idx+1,9, str(row.City))
			sh.write(idx+1,10, str(row.State))
			sh.write(idx+1,11, str(row.Zip_Code))
			sh.write(idx+1,12, str(row.Mobile_No))
			sh.write(idx+1,13, str(row.DOB))
			sh.write(idx+1,14, str(row.Emergency_Contact_Person))
			sh.write(idx+1,15, str(row.Emergency_Contact_No))
			sh.write(idx+1,16, str(row.Blood_Group))
			sh.write(idx+1,17, str(row.Marital_Status))
			sh.write(idx+1,18, str(row.Spouse_Name))
			sh.write(idx+1,19, str(row.No_of_Children))
			sh.write(idx+1,20, str(row.Aadhar_Number))
			sh.write(idx+1,21, str(row.PAN_Number))
			sh.write(idx+1,22, str(row.Driving_License_Number))
			sh.write(idx+1,23, str(row.Driving_License_Type))
			sh.write(idx+1,24, str(row.Drive_License_Validity))
			sh.write(idx+1,25, str(row.Vaccination_Name))
			sh.write(idx+1,26, str(row.Dose1_Date))
			sh.write(idx+1,27, str(row.Dose2_Date))
			sh.write(idx+1,28, str(row.Booster_Dose_Date))
			sh.write(idx+1,29, str(row.Education_Qualification))
			sh.write(idx+1,30, str(row.Aadhar_Attachment))
			sh.write(idx+1,31, str(row.PANCard_Attachment))
			sh.write(idx+1,32, str(row.Driver_Lic_Attachment))
			sh.write(idx+1,33, str(row.Vaccination_Certi_Attachment))
			sh.write(idx+1,34, str(row.Photo_Attachment))
			act = activity.query.filter_by(Unique_ID = row.Unique_ID).first()
			sh.write(idx+1,35, str(act.BGV))
			sh.write(idx+1,36, str(act.Active))
			sh.write(idx+1,37, str(act.Avaialbility))
			sh.write(idx+1,38, str(act.Last_shipment_date))
			sh.write(idx+1,39, str(act.Last_shipment_day))
			sh.write(idx+1,40, str(act.On_Shipment))
			sh.write(idx+1,41, str(act.Blacklisted))
			idx += 1

		WORKBOOK.save(output)
		output.seek(0)

		return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=driver_report.xls"})

	return render_template("shipment.html")




# download_ship_report
@app.route("/download/ship_report/pdf" , methods=["GET","POST"])
def download_Shipment_report():
	try :
		if session['user'] in params['User'] :
			pass
	except :
		return redirect(url_for('login'))
	if request.method == 'GET':
		ships = shipment.query.all()

		print()
		output = io.BytesIO()
		WORKBOOK = xlwt.Workbook()
		sh = WORKBOOK.add_sheet('report')

		sh.write( 0,0,'Shipment_No')
		sh.write( 0,1,'Vehicle_No')
		sh.write( 0,2,'Shipment_Type')
		sh.write( 0,3,'Pilot_unique_ID')
		sh.write( 0,4,'Copilot_unique_ID')
		sh.write( 0,5,'Dispatcher_unique_ID')
		sh.write( 0,6,'Transporter')
		sh.write( 0,7,'Add_Time')
		sh.write( 0,8,'End_Time')

		idx = 0
		for row in ships:
			print(row)
			sh.write(idx+1,0,str(row.Shipment_No))
			sh.write(idx+1,1,str(row.Vehicle_No))
			sh.write(idx+1,2,str(row.Shipment_Type))
			sh.write(idx+1,3,str(row.Pilot_unique_ID))
			sh.write(idx+1,4,str(row.Copilot_unique_ID))
			sh.write(idx+1,5,str(row.Dispatcher_unique_ID))
			sh.write(idx+1,6,str(row.Transporter))
			sh.write(idx+1,7,str(row.Add_Time))
			sh.write(idx+1,8,str(row.End_Time))
			idx += 1

		WORKBOOK.save(output)
		output.seek(0)

		return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=shipment_report.xls"})

	return render_template("shipment.html")


class shipment(db.Model):
	print("hello")
	Shipment_No  = db.Column(db.String(20), primary_key=True, nullable=False)
	Vehicle_No = db.Column(db.String(80), unique=True, nullable=False)
	Shipment_Type = db.Column(db.String(80), unique=False, nullable=False)
	Pilot_unique_ID = db.Column(db.String(80), unique=True, nullable=False)
	Copilot_unique_ID = db.Column(db.String(80), unique=True, nullable=False)
	Dispatcher_unique_ID = db.Column(db.String(80), unique=True, nullable=False)
	Transporter = db.Column(db.String(80), unique=True, nullable=False)
	Add_Time = db.Column(db.String(120), unique=False, nullable=True)
	End_Time = db.Column(db.String(120), unique=False, nullable=True)


class activity(db.Model):
	print("hello")
	Unique_ID   = db.Column(db.String(80), primary_key=True, nullable=False)
	Role = db.Column(db.String(10), unique=False, nullable=True)
	BGV = db.Column(db.String(10), unique=False, nullable=True)
	Active = db.Column(db.String(10), unique=False, nullable=True)
	Avaialbility = db.Column(db.String(10), unique=False, nullable=True)
	Last_shipment_date = db.Column(db.String(120), unique=False, nullable=True)
	Last_shipment_day = db.Column(db.String(120), unique=False, nullable=True)
	On_Shipment = db.Column(db.String(80), unique=False, nullable=True)
	Blacklisted = db.Column(db.String(80), unique=False, nullable=True)


class transport(db.Model):
	print("hello")
	Transporter_ID  = db.Column(db.String(80), primary_key=True, nullable=False)
	Transporter = db.Column(db.String(80), unique=False, nullable=True)
	

class employee(db.Model):
	print("hello")
	Unique_ID =  db.Column(db.String(80), primary_key=True, nullable=False)
	Date_of_Onboard = db.Column(db.String(80), primary_key=False, nullable=False)
	First_Name = db.Column(db.String(80), primary_key=False, nullable=False)
	Middle_Name = db.Column(db.String(80), primary_key=False, nullable=True)
	Last_Name = db.Column(db.String(80), primary_key=False, nullable=False)
	Transporter = db.Column(db.String(80), primary_key=False, nullable=False)
	Role = db.Column(db.String(80), primary_key=False, nullable=False)
	Address_1 = db.Column(db.String(80), primary_key=False, nullable=False)
	Address_2 = db.Column(db.String(80), primary_key=False, nullable=False)
	City = db.Column(db.String(80), primary_key=False, nullable=False)
	State = db.Column(db.String(80), primary_key=False, nullable=False)
	Zip_Code = db.Column(db.String(80), primary_key=False, nullable=False)
	Mobile_No = db.Column(db.String(80), primary_key=False, nullable=False)
	DOB = db.Column(db.String(80), primary_key=False, nullable=False)
	Emergency_Contact_Person = db.Column(db.String(80), primary_key=False, nullable=False)
	Emergency_Contact_No = db.Column(db.String(80), primary_key=False, nullable=False)
	Blood_Group = db.Column(db.String(80), primary_key=False, nullable=False)
	Marital_Status = db.Column(db.String(80), primary_key=False, nullable=False)
	Spouse_Name = db.Column(db.String(80), primary_key=False, nullable=False)
	No_of_Children = db.Column(db.String(80), primary_key=False, nullable=False)
	Aadhar_Number = db.Column(db.String(80), primary_key=False, nullable=False)
	PAN_Number = db.Column(db.String(80), primary_key=False, nullable=False)
	Driving_License_Number = db.Column(db.String(80), primary_key=False, nullable=True)
	Driving_License_Type = db.Column(db.String(80), primary_key=False, nullable=True)
	Drive_License_Validity = db.Column(db.String(80), primary_key=False, nullable=True)
	Vaccination_Name = db.Column(db.String(80), primary_key=False, nullable=False)
	Dose1_Date = db.Column(db.String(80), primary_key=False, nullable=False)
	Dose2_Date = db.Column(db.String(80), primary_key=False, nullable=False)
	Booster_Dose_Date = db.Column(db.String(80), primary_key=False, nullable=False)
	Education_Qualification = db.Column(db.String(80), primary_key=False, nullable=False)
	Aadhar_Attachment = db.Column(db.String(80), primary_key=False, nullable=False)
	PANCard_Attachment = db.Column(db.String(80), primary_key=False, nullable=True)
	Driver_Lic_Attachment = db.Column(db.String(80), primary_key=False, nullable=True)
	Vaccination_Certi_Attachment = db.Column(db.String(80), primary_key=False, nullable=False)
	Photo_Attachment = db.Column(db.String(80), primary_key=False, nullable=False)


app.run(debug=True)