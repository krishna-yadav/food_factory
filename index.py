from flask import Flask, render_template , request , session ,jsonify
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/zubilant'
db = SQLAlchemy(app)
app.secret_key = 'my-super-secret-key'
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\admin\\OneDrive\\Documents\\KRISHNA\\Final\\food_factory\\static\\images'



@app.route("/dashboard")
def dashboard():
	print("hii")
	return render_template("dashboard.html")
	

# login page
@app.route("/login", methods = ['GET','POST'])
def login():
	if ('user' in session and session['user'] == 'admin'):
		return render_template("dashboard.html")

	if request.method == 'POST':
		username = request.form['user']
		password = request.form['pass']
		if (username == 'admin' and password == 'admin'):
			session['user'] = username
			return render_template("dashboard.html")

	return render_template("login.html")



# shipment form
@app.route("/shipment", methods = ['GET','POST'])
def shipment():
	Driver = employee.query.filter_by(Role='Driver')
	Dispatcher = employee.query.filter_by(Role='Dispatcher')
	print("Driver")
	print(Driver)
	# for i in driver:
	# 	print(i)
	# emp = employee.query.all()
	# print("emp")
	# print(emp)
	if request.method == 'POST':
		s= []
		ShipmentNo = request.form['Shipment_No']
		Vehicle_No = request.form['Vehicle_No']
		Shipment_Type = request.form['Shipment_Type']
		s.append(request.form['Pilot_unique_ID'])
		s.append(request.form['Copilot_unique_ID'])
		s.append(request.form['Dispatcher_unique_ID'])
		Transporter = request.form['Transporter']

		entry = shipment(Shipment_No = ShipmentNo, Vehicle_No= Vehicle_No, Shipment_Type= Shipment_Type,Pilot_unique_ID= s[0],Copilot_unique_ID= s[1],
		 Dispatcher_unique_ID= s[2],Transporter= Transporter, Add_Time= datetime.now(), End_Time = datetime.now())
			 # ,Add_Time= Add_Time, End_Time= End_Time)

		print(entry)
		db.session.add(entry)
		db.session.commit()
		for i in s:
			print(i)
			post = activity.query.filter_by(Unique_ID=i).first()
			print("poastaaaa")
			print(post.On_Shipment)
			post.On_Shipment= 'Yes'
			db.session.commit()

	# 	mail.send_message('New message from me',
    # sender = 'krishna.yadav25021999@gmail.com',
    # recipients = ['krishna.yadav25021999@gmail.com'] ,
    # body = "message",
    # )   

		return 'POST'
	return render_template("shipment.html", Driver=Driver , Dispatcher=Dispatcher )




# driver form
@app.route("/driver", methods = ['GET','POST'])
def driver():
	print("uuuuu")
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
		Drive_License_Validity = request.form['Drive_License_Validity']
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

		if Aadhar_Attachment :
			Aadhar_Attachment.save(join(app.config['UPLOAD_FOLDER'], secure_filename(Aadhar_Attachment.filename)))
			Aadhar_Attachment = "yes"
		if PANCard_Attachment :
			PANCard_Attachment.save(join(app.config['UPLOAD_FOLDER'], secure_filename(PANCard_Attachment.filename)))
			PANCard_Attachment = "yes"
		if Driver_Lic_Attachment :
			Driver_Lic_Attachment.save(join(app.config['UPLOAD_FOLDER'], secure_filename(Driver_Lic_Attachment.filename)))
			Driver_Lic_Attachment = "yes"
		if Vaccination_Certi_Attachment :
			Vaccination_Certi_Attachment.save(join(app.config['UPLOAD_FOLDER'], secure_filename(Vaccination_Certi_Attachment.filename)))
			Vaccination_Certi_Attachment = "yes"
		if Photo_Attachment :
			Photo_Attachment.save(join(app.config['UPLOAD_FOLDER'] , secure_filename(Photo_Attachment.filename)))
			Photo_Attachment = "yes"


		S = First_Name[0:4]+"_"+Transporter[0:4]
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

		return 'POST'
	return render_template("driver.html")



 
 # update in shipment
@app.route("/ajax_update",methods=['POST'])
def ajax_update():
	print("cooollll")
	msg = "yoo"
	if request.method == 'POST': 
		msg = 'update done'
		ShipmentNo = request.form['Shipment_No']
		Vehicle_No = request.form['Vehicle_No']
		Shipment_Type = request.form['Shipment_Type']
		Pilot_unique_ID = request.form['Pilot_unique_ID']
		Copilot_unique_ID = request.form['Copilot_unique_ID']
		Dispatcher_unique_ID = request.form['Dispatcher_unique_ID']
		Transporter = request.form['Transporter']

		post = shipment.query.filter_by(Shipment_No=ShipmentNo).first()
		if post:
			print("ajax post")
			print(post)
			# post.ShipmentNo = ShipmentNo
			post.Vehicle_No = Vehicle_No
			post.Shipment_Type = Shipment_Type
			post.Pilot_unique_ID = Pilot_unique_ID
			post.Copilot_unique_ID = Copilot_unique_ID
			post.Dispatcher_unique_ID = Dispatcher_unique_ID
			post.Transporter = Transporter
			db.session.commit()
			msg = 'Record successfully Updated'
		else :
			msg = 'shipment number is not changable'
			return jsonify(msg)


	return jsonify(msg)   



 # update in driver
@app.route("/ajax_driver_update",methods=['POST'])
def ajax_driver_update():
	print("drive away")
	if request.method == 'POST': 
		msg = 'update done'
		Unique_ID = request.form['Unique_ID']
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
		Drive_License_Validity = request.form['Drive_License_Validity']
		Vaccination_Name = request.form['Vaccination_Name']
		Dose1_Date = request.form['Dose1_Date']
		Dose2_Date = request.form['Dose2_Date']
		Booster_Dose_Date = request.form['Booster_Dose_Date']
		Education_Qualification = request.form['Education_Qualification']
		Aadhar_Attachment = request.form['Aadhar_Attachment']
		PANCard_Attachment = request.form['PANCard_Attachment']
		Driver_Lic_Attachment = request.form['Driver_Lic_Attachment']
		Vaccination_Certi_Attachment = request.form['Vaccination_Certi_Attachment']
		Photo_Attachment = request.form['Photo_Attachment']
		print("Date_of_Onboard: ",Date_of_Onboard)

		post = employee.query.filter_by(Unique_ID=Unique_ID).first()
		if post:
			print("ajax post")
			print(post)
			post.First_Name = First_Name
			post.Middle_Name = Middle_Name
			post.Last_Name = Last_Name
			post.Transporter = Transporter
			post.Role = Role
			post.Address_1 = Address_1
			post.Address_2 = Address_2
			post.City = City
			post.State = State
			post.Zip_Code = Zip_Code
			post.Mobile_No = Mobile_No
			post.Driving_License_Number = Driving_License_Number
			post.Driving_License_Type = Driving_License_Type
			post.Drive_License_Validity = Drive_License_Validity
			db.session.commit()
			msg = 'Record successfully Updated'
		else :
			msg = 'shipment number is not changable'
			return jsonify(msg)


	return jsonify(msg)   



   


# shipment list
@app.route("/ship_list", methods= ["GET","POST"])
def ship_list():
	ships = shipment.query.all()
	print(ships)
	if request.method == 'GET':
		return render_template("ship_list.html", shipment=ships)
	return render_template("ship_list.html")	


# driver list
@app.route("/driver_list", methods= ["GET","POST"])
def driver_list():
	emp = employee.query.all()
	print(emp)
	if request.method == 'GET':
		return render_template("driver_list.html", employee=emp)
	return render_template("driver_list.html")	


class shipment(db.Model):
	print("hello")
	Shipment_No  = db.Column(db.String(80), primary_key=True, nullable=False)
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
	BGV = db.Column(db.String(10), unique=False, nullable=True)
	Avaialbility = db.Column(db.String(10), unique=False, nullable=True)
	Last_shipment_day = db.Column(db.String(120), unique=False, nullable=True)
	On_Shipment = db.Column(db.String(80), unique=False, nullable=True)
	Blacklisted = db.Column(db.String(80), unique=False, nullable=True)



class employee(db.Model):
	print("hello")
	Unique_ID = db.Column(db.String(80), primary_key=True, nullable=False)
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