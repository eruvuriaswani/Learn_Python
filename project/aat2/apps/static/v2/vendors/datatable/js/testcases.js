//
// Updates "Select all" control in a data table
//
// window.onbeforeunload = function() {
//   localStorage.removeItem(key);
//   return '';
// };



function updateDataTableSelectAllCtrl(table){
   var $table             = table.table().node();
   var $chkbox_all        = $('tbody input[type="checkbox"]', $table);
   var $chkbox_checked    = $('tbody input[type="checkbox"]:checked', $table);
   var chkbox_select_all  = $('thead input[name="select_all"]', $table).get(0);

   // If none of the checkboxes are checked
   if($chkbox_checked.length === 0){
      chkbox_select_all.checked = false;
      if('indeterminate' in chkbox_select_all){
         chkbox_select_all.indeterminate = false;
      }

   // If all of the checkboxes are checked
   } else if ($chkbox_checked.length === $chkbox_all.length){
      chkbox_select_all.checked = true;
      if('indeterminate' in chkbox_select_all){
         chkbox_select_all.indeterminate = false;
      }

   // If some of the checkboxes are checked
   } else {
      chkbox_select_all.checked = true;
      if('indeterminate' in chkbox_select_all){
         chkbox_select_all.indeterminate = true;
      }
   }
}

function get_selected_apis(){
   var selectedIds = [];

   $('#example tbody input[type="checkbox"]:checked').each(function() {
       selectedIds.push($(this).attr('id'));
   });
   return selectedIds;
}


function get_list(ajax_url){
   var rows_selected = [];
   console.info(ajax_url);
   var table = $('#example').DataTable({
      ajax:           ajax_url,
      scrollY:        '35vh',
      scrollCollapse: true,
      paging:         false,
      search:         false,
      info:           false,
      'columnDefs': [{
      'targets': 0,
      'searchable':false,
      'orderable':false,
      'width':'2%',
      'className': 'id',
         'render': function (data, type, full, meta){
            return '<input type="checkbox" id="' + data + '">';
         }
      },
      {
      'targets': 1
      }],
      'order': [1, 'asc']
   });
}


$(document).ready(function (){
   window.localStorage.clear();
   // Array holding selected row IDs
   
   $("#get_api_list").click(function(){
      var project_id = $('#projects option:selected').attr('id');
      var ajax_url = '/get_tcs?proj='+project_id;
      get_list(ajax_url);
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

   $("#create_tcs").click(function(){
      var selected = get_selected_apis();
      json_data = JSON.stringify({
            'api_list': selected,
            'tc_name': $("#tcs_name").val(),
            'project': $('#projects option:selected').attr('id')
         });
      $.post({
         url: "/create_tcs",
         contentType: 'application/json; charset=utf-8',
         dataType: 'json',
         async: true,
         data: json_data,
         success: function(msg){
            console.info(msg);
            $("#result").empty();
            $("#result").append(msg['msg']);
            // $("#result").val(msg);
         }
      });
   });
});
