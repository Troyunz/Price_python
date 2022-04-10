$(document).ready(function () {
    $('#priceStorage').DataTable({
        "pageLength": 50,
        // searching: false 
        "autoWidth": false, // might need this
        "columns": [
            { "width": "2%"}, // automatically calculates
            { "width": "80%" },
             null,  // remaining width
             null
  ]
    });
  });