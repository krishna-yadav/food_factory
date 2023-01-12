$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
    var actions = $("table td:last-child").html();



    // update rec row on edit button click
    $(document).on("click", ".update", function(){
        var id = $(this).attr("id");
        var string = id;

        var Unique_ID = $("#Unique_ID").val();
        var Date_of_Onboard  = $("#Date_of_Onboard").val();
        var First_Name  = $("#First_Name").val();
        var Middle_Name = $("#Middle_Name").val();
        var Last_Name  = $("#Last_Name").val();
        var Transporter  = $("#Transporter").val();
        var Role  = $("#Role").val();
        var Address_1  = $("#Address_1").val();
        var Address_2  = $("#Address_2").val();
        var City  = $("#City").val();
        var State  = $("#State").val();
        var Zip_Code  = $("#Zip_Code").val();
        var Mobile_No  = $("#Mobile_No").val();
        var DOB  = $("#DOB").val();
        var Emergency_Contact_Person  = $("#Emergency_Contact_Person").val();
        var Emergency_Contact_No  = $("#Emergency_Contact_No").val();
        var Blood_Group  = $("#Blood_Group").val();
        var Marital_Status  = $("#Marital_Status").val();
        var Spouse_Name  = $("#Spouse_Name").val();
        var No_of_Children  = $("#No_of_Children").val();
        var Aadhar_Number  = $("#Aadhar_Number").val();
        var PAN_Number  = $("#PAN_Number").val();
        var Driving_License_Number = $("#Driving_License_Number").val();
        var Driving_License_Type = $("#Driving_License_Type").val();
        var Drive_License_Validity = $("#Drive_License_Validity").val();
        var Vaccination_Name  = $("#Vaccination_Name").val();
        var Dose1_Date  = $("#Dose1_Date").val();
        var Dose2_Date  = $("#Dose2_Date").val();
        var Booster_Dose_Date  = $("#Booster_Dose_Date").val();
        var Education_Qualification  = $("#Education_Qualification").val();
        var Aadhar_Attachment  = $("#Aadhar_Attachment").val();
        var PANCard_Attachment = $("#PANCard_Attachment").val();
        var Driver_Lic_Attachment = $("#Driver_Lic_Attachment").val();
        var Vaccination_Certi_Attachment  = $("#Vaccination_Certi_Attachment").val();
        var Photo_Attachment = $("#Photo_Attachment").val();
        // $("#displaymessage").html(Unique_ID);
        //     $("#displaymessage").show();
        
        $.post('/ajax_driver_update', { string: string, Unique_ID : Unique_ID , 
            Date_of_Onboard: Date_of_Onboard,
         First_Name: First_Name,Middle_Name: Middle_Name,
         Last_Name: Last_Name, Transporter: Transporter,Role: Role,
         Address_1: Address_1,Address_2:Address_2,City:City,State:State,Zip_Code:Zip_Code, Mobile_No: Mobile_No, 
         DOB: DOB,Emergency_Contact_Person: Emergency_Contact_Person,
         Emergency_Contact_No: Emergency_Contact_No, Blood_Group: Blood_Group,Marital_Status: Marital_Status,
         Spouse_Name: Spouse_Name,No_of_Children: No_of_Children,
         Aadhar_Number: Aadhar_Number,
         PAN_Number: PAN_Number,
         Driving_License_Number: Driving_License_Number,Driving_License_Type: Driving_License_Type,
         Drive_License_Validity: Drive_License_Validity,
         Vaccination_Name: Vaccination_Name,
         Dose1_Date: Dose1_Date,Dose2_Date: Dose2_Date,Booster_Dose_Date: Booster_Dose_Date,
         Education_Qualification: Education_Qualification,Aadhar_Attachment: Aadhar_Attachment,
         PANCard_Attachment: PANCard_Attachment,
         Driver_Lic_Attachment: Driver_Lic_Attachment,
         Vaccination_Certi_Attachment: Vaccination_Certi_Attachment,Photo_Attachment: Photo_Attachment }, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
         
         
    });
    // Edit row on edit button click
    $(document).on("click", ".edit", function(){  
        $(this).parents("tr").find("td:not(:last-child)").each(function(i){
            if (i=='0'){
                var idname = 'Unique_ID';
                // $("#displaymessage").html(idname); 
                // $("#displaymessage").show();
            }else if (i=='1'){
                var idname = 'Date_of_Onboard';
            }else if (i=='2'){
                var idname = 'First_Name';
            }else if (i=='3'){
                var idname = 'Middle_Name';
            }else if (i=='4'){
                var idname = 'Last_Name';
            }else if (i=='5'){
                var idname = 'Transporter';
            }else if (i=='6'){
                var idname = 'Role';
            }else if (i=='7'){
                var idname = 'Address_1';
            }else if (i=='8'){
                var idname = 'Address_2';
            }else if (i=='9'){
                var idname = 'City';
            }else if (i=='10'){
                var idname = 'State';
            }else if (i=='11'){
                var idname = 'Zip_Code';
            }else if (i=='12'){
                var idname = 'Mobile_No';
            }else if (i=='13'){
                var idname = 'DOB';
            }else if (i=='14'){
                var idname = 'Emergency_Contact_Person';
            }else if (i=='15'){
                var idname = 'Emergency_Contact_No';
            }else if (i=='16'){
                var idname = 'Blood_Group';
            }else if (i=='17'){
                var idname = 'Marital_Status';
            }else if (i=='18'){
                var idname = 'Spouse_Name';
            }else if (i=='19'){
                var idname = 'No_of_Children';
            }else if (i=='20'){
                var idname = 'Aadhar_Number';
            }else if (i=='21'){
                var idname = 'PAN_Number';
            }else if (i=='22'){
                var idname = 'Driving_License_Number';
            }else if (i=='23'){
                var idname = 'Driving_License_Type';
            }else if (i=='24'){
                var idname = 'Drive_License_Validity';
            }else if (i=='25'){
                var idname = 'Vaccination_Name';
            }else if (i=='26'){
                var idname = 'Dose1_Date';
            }else if (i=='27'){
                var idname = 'Dose2_Date';
            }else if (i=='28'){
                var idname = 'Booster_Dose_Date';
            }else if (i=='29'){
                var idname = 'Education_Qualification';
            }else if (i=='30'){
                var idname = 'Aadhar_Attachment';
            }else if (i=='31'){
                var idname = 'PANCard_Attachment';
            }else if (i=='32'){
                var idname = 'Driver_Lic_Attachment';
            }else if (i=='33'){
                var idname = 'Vaccination_Certi_Attachment';
            }else if (i=='34'){
                var idname = 'Photo_Attachment';
            }else{} 
            $(this).html('<input type="text" name="updaterec" id="' + idname + '" class="form-control" value="' + $(this).text() + '">');

        });  
        $(this).parents("tr").find(".add, .edit").toggle();
        // $(".add-new").attr("disabled", "disabled");
        $(this).parents("tr").find(".add").removeClass("add").addClass("update"); 
    });
});

