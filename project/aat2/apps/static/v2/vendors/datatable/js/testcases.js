

function get_list(ajax_url, t_list){
   var rows_selected = [];
   // console.info(ajax_url);
   $.get(ajax_url, function(data, status){
      // console.info("data>>> " + data['data']);
       $.each(data['data'], function( api_id, name ) {
         console.info(name[1]);
        $("#testcases").append("<a class='tcs list-group-item' id=" + name[0] + ">" +name[1]+ "</a>"); 
         
       });
       }); 
    };



$(document).ready(function (){
   $("#get_tcs").click(function(){
      var project_id = $('#projects option:selected').attr('id');
      var ajax_url = '/get_tcs?proj='+project_id;
      get_list(ajax_url, $("#testcases"));
   });

   $('#remove_api').click(function(){
      var selected = get_selected_apis();
      $.ajax({
         type: "POST",
         url: '/remove_apis',
         dataType: "json",
         traditional: true,
         data: {
            apis: selected
         }
      });
   });

   $("#execute_tcs").click(function(){
      var selected = get_selected();
      json_data = JSON.stringify({
            'tc_list': selected
         });
      $.post({
         url: "/start_tcs",
         contentType: 'application/json; charset=utf-8',
         dataType: 'json',
         async: true,
         data: json_data,
         success: function(msg){
            console.info(msg);
            $("#result").empty();
            $("#result").append(msg['msg']);
         }
      });
   });
});
