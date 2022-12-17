function valid(val) {
    v1 = document.getElementById("First_Name");
    v2 = document.getElementById("Last_Name");
    v3 = document.getElementById("Date_of_Onboard");
    v4 = document.getElementById("Transporter");
    v5 = document.getElementById("Role");
    v6 = document.getElementById("Address_1");
    v7 = document.getElementById("Address_2");
    v8 = document.getElementById("City");
    v9 = document.getElementById("State");
    v10 = document.getElementById("Zip_Code");
    v11 = document.getElementById("Mobile_No");
    v12 = document.getElementById("DOB");
    v13 = document.getElementById("Emergency_Contact_Person");
    v14 = document.getElementById("Emergency_Contact_No");
    v15 = document.getElementById("Blood_Group");
    v16 = document.getElementById("Marital_Status");
    v17 = document.getElementById("Education_Qualification");
    v18 = document.getElementById("Aadhar_Number");
    v19 = document.getElementById("Aadhar_Attachment");
    v20 = document.getElementById("Driving_License_Number");
    v21 = document.getElementById("Driving_License_Type");
    v22 = document.getElementById("Drive_License_Validity");
    v23 = document.getElementById("Driver_Lic_Attachment");
    v24 = document.getElementById("Vaccination_Name");
    v25 = document.getElementById("Vaccination_Certi_Attachment");
    v26 = document.getElementById("Photo_Attachment");
 
 


 // v18 = document.getElementById("Driving_License_Number");
 //    v19 = document.getElementById("Driving_License_Type");
 //    v20 = document.getElementById("Drive_License_Validity");
 //    v21 = document.getElementById("Vaccination_Name");
 //    v22 = document.getElementById("Aadhar_Number");
 //    v23 = document.getElementById("Aadhar_Attachment");
 //    v24 = document.getElementById("Driver_Lic_Attachment");
 //    v25 = document.getElementById("Vaccination_Certi_Attachment");
 //    v26 = document.getElementById("Photo_Attachment");
 

    flag1 = true;
    flag2 = true;
    flag3 = true;
    flag4 = true;
    flag5 = true;
    flag6 = true;
    flag7 = true;
    flag8 = true;
    flag9 = true;
    flag10 = true;
    flag11 = true;
    flag12 = true;
    flag13 = true;
    flag14 = true;
    flag15 = true;
    flag16 = true;
    flag17 = true;
    flag18 = true;
    flag19 = true;
    flag20 = true;
    flag21 = true;
    flag22 = true;
    flag23 = true;
    flag24 = true;
    flag25 = true;
    flag26 = true;

    

    if(val>=1 || val==0) {
        if(v1.value == "") {
            v1.style.borderColor = "red";
            flag1 = false;
        }
        else {
            v1.style.borderColor = "green";
            flag1 = true;
        }
    }

    if(val>=2 || val==0) {
        if(v2.value == "") {
            v2.style.borderColor = "red";
            flag2 = false;
        }
        else {
            v2.style.borderColor = "green";
            flag2 = true;
        }
    }
    if(val>=3 || val==0) {
        if(v3.value == "") {
            v3.style.borderColor = "red";
            flag3 = false;
        }
        else {
            v3.style.borderColor = "green";
            flag3 = true;
        }
    }
    if(val>=4 || val==0) {
        if(v4.value == "") {
            v4.style.borderColor = "red";
            flag4 = false;
        }
        else {
            v4.style.borderColor = "green";
            flag4 = true;
        }
    }
    if(val>=5 || val==0) {
        if(v5.value == "") {
            v5.style.borderColor = "red";
            flag5 = false;
        }
        else {
            v5.style.borderColor = "green";
            flag5 = true;
        }
    }
    if(val>=6 || val==0) {
        if(v6.value == "") {
            v6.style.borderColor = "red";
            flag6 = false;
        }
        else {
            v6.style.borderColor = "green";
            flag6 = true;
        }
    }

    if(val>=7 || val==0) {
        if(v7.value == "") {
            v7.style.borderColor = "red";
            flag7 = false;
        }
        else {
            v7.style.borderColor = "green";
            flag7 = true;
        }
    }

    if(val>=8 || val==0) {
        if(v8.value == "") {
            v8.style.borderColor = "red";
            flag8 = false;
        }
        else {
            v8.style.borderColor = "green";
            flag8 = true;
        }
    }

    if(val>=9 || val==0) {
        if(v9.value == "") {
            v9.style.borderColor = "red";
            flag9 = false;
        }
        else {
            v9.style.borderColor = "green";
            flag9 = true;
        }
    }

    if(val>=10 || val==0) {
        if(v10.value == "") {
            v10.style.borderColor = "red";
            flag10 = false;
        }
        else {
            v10.style.borderColor = "green";
            flag10 = true;
        }
    }


    if(val>=11 || val==0) {
        if(v11.value == "") {
            v11.style.borderColor = "red";
            flag11 = false;
        }
        else {
            v11.style.borderColor = "green";
            flag11 = true;
        }
    }

    if(val>=12 || val==0) {
        if(v12.value == "") {
            v12.style.borderColor = "red";
            flag12 = false;
        }
        else {
            v12.style.borderColor = "green";
            flag12 = true;
        }
    }

    if(val>=13 || val==0) {
        if(v13.value == "") {
            v13.style.borderColor = "red";
            flag13 = false;
        }
        else {
            v13.style.borderColor = "green";
            flag13 = true;
        }
    }

    if(val>=14 || val==0) {
        if(v14.value == "") {
            v14.style.borderColor = "red";
            flag14 = false;
        }
        else {
            v14.style.borderColor = "green";
            flag14 = true;
        }
    }

    if(val>=15 || val==0) {
        if(v15.value == "") {
            v15.style.borderColor = "red";
            flag15 = false;
        }
        else {
            v15.style.borderColor = "green";
            flag15 = true;
        }
    }

    if(val>=16 || val==0) {
        if(v16.value == "") {
            v16.style.borderColor = "red";
            flag16 = false;
        }
        else {
            v16.style.borderColor = "green";
            flag16 = true;
        }
    }

    if(val>=17 || val==0) {
        if(v17.value == "") {
            v17.style.borderColor = "red";
            flag17 = false;
        }
        else {
            v17.style.borderColor = "green";
            flag17 = true;
        }
    }

    if(val>=18 || val==0) {
        if(v18.value == "") {
            v18.style.borderColor = "red";
            flag18 = false;
        }
        else {
            v18.style.borderColor = "green";
            flag18 = true;
        }
    }

    if(val>=19 || val==0) {
        if(v19.value == "") {
            v19.style.borderColor = "red";
            flag19 = false;
        }
        else {
            v19.style.borderColor = "green";
            flag19 = true;
        }
    }

    if(val>=20 || val==0) {
        if(v20.value == "") {
            v20.style.borderColor = "red";
            flag20 = false;
        }
        else {
            v20.style.borderColor = "green";
            flag20 = true;
        }
    }

    if(val>=21 || val==0) {
        if(v21.value == "") {
            v21.style.borderColor = "red";
            flag21 = false;
        }
        else {
            v21.style.borderColor = "green";
            flag21 = true;
        }
    }

    if(val>=22 || val==0) {
        if(v22.value == "") {
            v22.style.borderColor = "red";
            flag22 = false;
        }
        else {
            v22.style.borderColor = "green";
            flag22 = true;
        }
    }

    if(val>=23 || val==0) {
        if(v23.value == "") {
            v23.style.borderColor = "red";
            flag23 = false;
        }
        else {
            v23.style.borderColor = "green";
            flag23 = true;
        }
    }

    if(val>=24 || val==0) {
        if(v24.value == "") {
            v24.style.borderColor = "red";
            flag24 = false;
        }
        else {
            v24.style.borderColor = "green";
            flag24 = true;
        }
    }

    if(val>=25 || val==0) {
        if(v25.value == "") {
            v25.style.borderColor = "red";
            flag25 = false;
        }
        else {
            v25.style.borderColor = "green";
            flag25 = true;
        }
    }

    if(val>=26 || val==0) {
        if(v26.value == "") {
            v26.style.borderColor = "red";
            flag26 = false;
        }
        else {
            v26.style.borderColor = "green";
            flag26 = true;
        }
    }

    


    flag = flag1  &&    flag2  &&    flag3  &&    flag4  &&    flag5  &&    flag6  &&    flag7  &&    flag8  &&    flag9  &&    flag10  &&    flag11  &&    flag12  &&    flag13  &&    flag14  &&    flag15  &&    flag16  &&    flag17  &&    flag18  &&    flag19  &&    flag20  &&    flag21  &&    flag22 &&    flag23  &&    flag24  &&    flag25 && flag26;

    return flag;
}