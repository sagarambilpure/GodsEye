$(document).ready(function () {

    function get_search() {
        var optionSelected = $(this).find("option:selected");
        var state_name = optionSelected.text();

        console.log(state_name);
        sname = { 'state': state_name };

        $("#from_location option").remove();
        $.ajax('/', { method: 'GET', data: sname }).done(function (result) {
            // console.log(result);
            // $("#from_city option").remove();
            // for (var i = result.length - 1; i >= 0; i--) {
            //     $("#from_city").append('<option>' + result[i].scity + '</option>');
            // };

        }).fail(function () {
            // alert('Server down');
        });
    }

    get_search();

});
