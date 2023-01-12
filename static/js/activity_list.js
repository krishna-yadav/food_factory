$(document).ready(function(){
    $('[data-toggle="tooltip pro"]').tooltip();
    var actions = $("table td:last-child").html();



    // update rec row on edit button click
    $(document).on("click", ".update", function(){
        var id = $(this).attr("id");
        var string = id;

        var Unique_ID  = $("#Unique_ID").val();
        var Role = $("#Role").val();
        var BGV = $("#BGV").val();
        var Avaialbility = $("#Avaialbility").val();
        var Last_shipment_day = $("#Last_shipment_day").val();
        var On_Shipment = $("#On_Shipment").val();
        var Blacklisted = $("#Blacklisted").val();
        $("#displaymessage").html(BGV);
            $("#displaymessage").show();
        $.post('/ajax_activity_update', { string: string, Unique_ID:Unique_ID, Role: Role, BGV: BGV,
         Avaialbility: Avaialbility, Last_shipment_day: Last_shipment_day, On_Shipment: On_Shipment,
     Blacklisted: Blacklisted }, function(data) {
            $("#displaymessage").html(data);
            $("#displaymessage").show();
        });
         
         
    });
    // Edit row on edit button click
    $(document).on("click", ".edit", function(){  
        $(this).parents("tr").find("td:not(:last-child)").each(function(i){
            if (i=='0'){
                var idname = 'Unique_ID';
            }else if (i=='1'){
                var idname = 'Role';
            }else if (i=='2'){
                var idname = 'BGV';
                // $("#displaymessage").html(idname);
                // $("#displaymessage").show();
            }else if (i=='3'){
                var idname = 'Avaialbility';
            }else if (i=='4'){
                var idname = 'Last_shipment_day';
            }else if (i=='5'){
                var idname = 'On_Shipment';
            }else if (i=='6'){
                var idname = 'Blacklisted';
            }else{} 
            $(this).html('<input type="text" name="updaterec" id="' + idname + '" class="form-control" value="' + $(this).text() + '">');

        });  
        $(this).parents("tr").find(".add, .edit").toggle();
        // $(".add-new").attr("disabled", "disabled");
        $(this).parents("tr").find(".add").removeClass("add").addClass("update"); 
    });
});

