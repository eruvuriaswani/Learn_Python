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
   // selected_apis
   // var selected_apis = [];
   // var $chkbox_checked = $('#example tbody input[type="checkbox"]:checked');
   // return $chkbox_checked;

   var selectedIds = [];

   $('#example tbody input[type="checkbox"]:checked').each(function() {
       selectedIds.push($(this).attr('id'));
   });
   return selectedIds;
}

function get_api_list(project_id){
   var rows_selected = [];
   var table = $('#example').DataTable({
      'ajax': '/get_free_apis_by_prj_name?proj='+project_id,
          "scrollY":        "400px",
        "scrollCollapse": true,
        "paging":         false,
      'columnDefs': [{
         'targets': 0,
         'searchable':false,
         'orderable':false,
         'width':'1%',
         'className': 'dt-body-center',
         'render': function (data, type, full, meta){
             return '<input type="checkbox" id="' + data + '">';
         }
      },
         {
         'targets': 1,
         'className': 'api_id',
         }],
      'order': [1, 'asc']
      // ,
      // 'rowCallback': function(row, data, dataIndex){
      //    // Get row ID
      //    var rowId = data[0];

      //    // If row ID is in the list of selected row IDs
      //    if($.inArray(rowId, rows_selected) !== -1){
      //       $(row).find('input[type="checkbox"]').prop('checked', true);
      //       $(row).addClass('selected');
      //    }
      // }
   });
}



$(document).ready(function (){
   window.localStorage.clear();
   // Array holding selected row IDs
   
   $("#get_api_list").click(function(){
         get_api_list($("#projects").val());
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
      $.post({
         url: "/create_tcs",
         dataType: "json",
         data: {
            apis: selected,
            tc_name: $("#create_tcs").val()
         }
      })
   });
});