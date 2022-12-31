$(document).ready(function(){
    $('[data-toggle="tooltip pro"]').tooltip();
    var actions = $("table td:last-child").html();



    // update rec row on edit button click
    $(document).on("click", ".update", function(){
        var id = $(this).attr("id");
        var string = id;

        var Shipment_No = $("#Shipment_No").val();
        var Vehicle_No = $("#Vehicle_No").val();
        var Shipment_Type = $("#Shipment_Type").val();
        var Pilot_unique_ID = $("#Pilot_unique_ID").val();
        var Copilot_unique_ID = $("#Copilot_unique_ID").val();
        var Dispatcher_unique_ID = $("#Dispatcher_unique_ID").val();
        var Transporter = $("#Transporter").val();
        // $("#displaymessage").html(Shipment_Type);
        //     $("#displaymessage").show();
        $.post('/ajax_update', { string: string, Shipment_No:Shipment_No, Vehicle_No: Vehicle_No, Shipment_Type: Shipment_Type,
         Pilot_unique_ID: Pilot_unique_ID, Copilot_unique_ID: Copilot_unique_ID, Dispatcher_unique_ID: Dispatcher_unique_ID,
     Transporter: Transporter }, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
         
         
    });
    // Edit row on edit button click
    $(document).on("click", ".edit", function(){  
        $(this).parents("tr").find("td:not(:last-child)").each(function(i){
            if (i=='0'){
                var idname = 'Shipment_No';
            }else if (i=='1'){
                var idname = 'Vehicle_No';
            }else if (i=='2'){
                var idname = 'Shipment_Type';
            }else if (i=='3'){
                var idname = 'Pilot_unique_ID';
            }else if (i=='4'){
                var idname = 'Copilot_unique_ID';
            }else if (i=='5'){
                var idname = 'Dispatcher_unique_ID';
            }else if (i=='6'){
                var idname = 'Transporter';
            }else{} 
            $(this).html('<input type="text" name="updaterec" id="' + idname + '" class="form-control" value="' + $(this).text() + '">');

        });  
        $(this).parents("tr").find(".add, .edit").toggle();
        // $(".add-new").attr("disabled", "disabled");
        $(this).parents("tr").find(".add").removeClass("add").addClass("update"); 
    });
});

