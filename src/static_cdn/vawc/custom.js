// Datatables Customization
// remove and replace the default datatable searchbox
var katBrgySearchBox = $('#vawcTable').DataTable({
    "sDom": "tipr",
    "length": 10,
    "responsive": true
});
$('#vawcSearchBox').keyup(function() {
    katBrgySearchBox.search($(this).val()).draw();
})