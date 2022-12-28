$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
    var actions = $("table td:last-child").html();


    // Append table with add row form on add new button click
    // $(".add-new").click(function(){
    //     $(this).attr("disabled", "disabled");
    //     var index = $("table tbody tr:last-child").index();
    //     var row = '<tr>' +
    //         '<td><input type="text" class="form-control" name="Shipment_No" id="Shipment_No"></td>' +
    //         '<td><input type="text" class="form-control" name="Vehicle_No" id="Vehicle_No"></td>' +
    //         '<td><input type="text" class="form-control" name="Shipment_Type" id="Shipment_Type"></td>' +
    //         '<td><input type="text" class="form-control" name="Pilot_unique_ID" id="Pilot_unique_ID"></td>' +
    //         '<td><input type="text" class="form-control" name="Copilot_unique_ID" id="Copilot_unique_ID"></td>' +
    //         '<td><input type="text" class="form-control" name="Dispatcher_unique_ID" id="Dispatcher_unique_ID"></td>' +
    //      '<td><input type="text" class="form-control" name="Transporter" id="Transporter"></td>' +
    //      '<td>' + actions + '</td>' +
    //     '</tr>';
    //     $("table").append(row);  
    //     $("table tbody tr").eq(index + 1).find(".add, .edit, .delete").toggle();
    //     $('[data-toggle="tooltip"]').tooltip();
 
    // });
   
    // Add row on add button click


    // $(document).on("click", ".add", function(){
    //     var empty = false;
        // var input = $(this).parents("tr").find('input[type="text"]');
        // input.each(function(){
        //     if(!$(this).val()){
        //         $(this).addClass("error");
        //         empty = true;
        //     } else{
        //         $("#displaymessage").show();
        //     }
        // });

    //     var Shipment_No = $("#Shipment_No").val();
    //     var Vehicle_No = $("#Vehicle_No").val();
    //     var Shipment_Type = $("#Shipment_Type").val();
    //     var Pilot_unique_ID = $("#Pilot_unique_ID").val();
    //     var Copilot_unique_ID = $("#Copilot_unique_ID").val();
    //     var Dispatcher_unique_ID = $("#Dispatcher_unique_ID").val();
    //     var Transporter = $("#Transporter").val();
    //     $.post("/ajax_add", { Shipment_No: Shipment_No, Vehicle_No: Vehicle_No, Shipment_Type: Shipment_Type,
    //      Pilot_unique_ID: Pilot_unique_ID
    // , Copilot_unique_ID: Copilot_unique_ID, Dispatcher_unique_ID: Dispatcher_unique_ID,
    //  Transporter: Transporter}, function(data) {
    //         $("#displaymessage").html(data);
    //         $("#displaymessage").show();
    //     });
    //     $(this).parents("tr").find(".error").first().focus();
    //     if(!empty){
    //         input.each(function(){
    //             $(this).parent("td").html($(this).val());
    //         });   
    //         $(this).parents("tr").find(".add, .edit").toggle();
    //         $(".add-new").removeAttr("disabled");
    //     } 
    // });
    // Delete row on delete button click
    // $(document).on("click", ".delete", function(){
    //     $(this).parents("tr").remove();
    //     $(".add-new").removeAttr("disabled");
    //     var id = $(this).attr("id");
    //     var string = id;
    //     $.post("/ajax_delete", { string: string}, function(data) {
    //         $("#displaymessage").html(data);
    //         $("#displaymessage").show();
    //     });
    // });
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
        $("#displaymessage").html(Vehicle_No);
            $("#displaymessage").show();
        $.post('/ajax_update', { string: string, Shipment_No: Shipment_No, Vehicle_No: Vehicle_No, Shipment_Type: Shipment_Type,
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














// $(document).ready(function(){
//     $('[data-toggle="tooltip"]').tooltip();
//     var actions = $("table td:last-child").html();


//     // Append table with add row form on add new button click
//     $(".add-new").click(function(){
//         $(this).attr("disabled", "disabled");
//         var index = $("table tbody tr:last-child").index();
//         var row = '<tr>' +
//             '<td><input type="text" class="form-control" name="Shipment_No" id="Shipment_No"></td>' +
//             '<td><input type="text" class="form-control" name="Vehicle_No" id="Vehicle_No"></td>' +
//             '<td><input type="text" class="form-control" name="Shipment_Type" id="Shipment_Type"></td>' +
//             '<td><input type="text" class="form-control" name="Pilot_unique_ID" id="Pilot_unique_ID"></td>' +
//             '<td><input type="text" class="form-control" name="Copilot_unique_ID" id="Copilot_unique_ID"></td>' +
//             '<td><input type="text" class="form-control" name="Dispatcher_unique_ID" id="Dispatcher_unique_ID"></td>' +
//          '<td><input type="text" class="form-control" name="Transporter" id="Transporter"></td>' +
//          '<td>' + actions + '</td>' +
//         '</tr>';
//         $("table").append(row);  
//         $("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
//         $('[data-toggle="tooltip"]').tooltip();
 
//     });
   
//     // Add row on add button click
//     $(document).on("click", ".add", function(){
//         var empty = false;
//         // var input = $(this).parents("tr").find('input[type="text"]');
//         // input.each(function(){
//         //     if(!$(this).val()){
//         //         $(this).addClass("error");
//         //         empty = true;
//         //     } else{
//         //         $(this).removeClass("error");
//         //     }
//         // });
//         var Shipment_No = $("#Shipment_No").val();
//         var Vehicle_No = $("#Vehicle_No").val();
//         var Shipment_Type = $("#Shipment_Type").val();
//         var Pilot_unique_ID = $("#Pilot_unique_ID").val();
//         var Copilot_unique_ID = $("#Copilot_unique_ID").val();
//         var Dispatcher_unique_ID = $("#Dispatcher_unique_ID").val();
//         var Transporter = $("#Transporter").val();
//         $.post("/ajax_add", { Shipment_No: Shipment_No, Vehicle_No: Vehicle_No, Shipment_Type: Shipment_Type,
//          Pilot_unique_ID: Pilot_unique_ID
//     , Copilot_unique_ID: Copilot_unique_ID, Dispatcher_unique_ID: Dispatcher_unique_ID,
//      Transporter: Transporter}, function(data) {
//             $("#displaymessage").html(data);
//             $("#displaymessage").show();
//         });
//         $(this).parents("tr").find(".error").first().focus();
//         if(!empty){
//             input.each(function(){
//                 $(this).parent("td").html($(this).val());
//             });   
//             $(this).parents("tr").find(".add, .edit").toggle();
//             $(".add-new").removeAttr("disabled");
//         } 
//     });


//     // Delete row on delete button click
//     // $(document).on("click", ".delete", function(){
//     //     $(this).parents("tr").remove();
//     //     $(".add-new").removeAttr("disabled");
//     //     var id = $(this).attr("id");
//     //     var string = id;
//     //     $.post("/ajax_delete", { string: string}, function(data) {
//     //         $("#displaymessage").html(data);
//     //         $("#displaymessage").show();
//     //     });
//     // });

    
         
//          // Shipment_No: Shipment_No,
         
//     });
//     // Edit row on edit button click
//     $(document).on("click", ".edit", function(){  
//         $(this).parents("tr").find("td:not(:last-child)").each(function(i){
//             // if (i=='0'){
//             //     var idname = 'Shipment_No';
//             // }else if (i=='1'){
//             //     var idname = 'Vehicle_No';
//             // }else if (i=='2'){
//             //     var idname = 'Shipment_Type';
//             // }else if (i=='3'){
//             //     var idname = 'Pilot_unique_ID';
//             // }else if (i=='4'){
//             //     var idname = 'Copilot_unique_ID';
//             // }else if (i=='5'){
//             //     var idname = 'Dispatcher_unique_ID';
//             // }else if (i=='6'){
//             //     var idname = 'Transporter';

//             if (i=='0'){
//                 var idname = 'Vehicle_No';
//             }else if (i=='1'){
//                 var idname = 'Shipment_Type';
//             }else if (i=='2'){
//                 var idname = 'Pilot_unique_ID';
//             }else if (i=='3'){
//                 var idname = 'Copilot_unique_ID';
//             }else if (i=='4'){
//                 var idname = 'Dispatcher_unique_ID';
//             }else if (i=='5'){
//                 var idname = 'Transporter';
//             }else{} 
//             $(this).html('<input type="text" name="updaterec" id="' + idname + '" class="form-control" value="' + $(this).text() + '">');
//         });  
//         $(this).parents("tr").find(".add, .edit").toggle();
//         // $(".add-new").attr("disabled", "disabled");
//         $(this).parents("tr").find(".add").removeClass("add").addClass("update"); 
//     });

//     // update rec row on edit button click
//     $(document).on("click", ".update", function(){
//         var id = $(this).attr("id");
//         var string = id;
//         // var Shipment_No = $("#Shipment_No").val();
//         var Vehicle_No = $("#Vehicle_No").val();
//         var Shipment_Type = $("#Shipment_Type").val();
//         var Pilot_unique_ID = $("#Pilot_unique_ID").val();
//         var Copilot_unique_ID = $("#Copilot_unique_ID").val();
//         var Dispatcher_unique_ID = $("#Dispatcher_unique_ID").val();
//         var Transporter = $("#Transporter").val();
//         $.post("/ajax_update", { string: string,  Vehicle_No: Vehicle_No, Shipment_Type: Shipment_Type,
//          Pilot_unique_ID: Pilot_unique_ID
//     , Copilot_unique_ID: Copilot_unique_ID, Dispatcher_unique_ID: Dispatcher_unique_ID,
//      Transporter: Transporter}, function(data) {
//             $("#displaymessage").html(data);
//             $("#displaymessage").show();
//         });
// });

