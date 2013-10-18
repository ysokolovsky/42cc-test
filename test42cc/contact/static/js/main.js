$(document).ready(function () {
    var url = window.location;
    $('ul.nav a[href="'+ url +'"]').parent().addClass('active');
    $('ul.nav a').filter(function() {
        return this.href == url;
    }).parent().addClass('active');


    $('#form').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            beforeSend: function() {
                        $("#form :input").attr("disabled", true);
                        $('#success_message').text('Loading...');
                            },
            success: function(response) { // on success..
                     $("#form :input").attr("disabled", false);
                     $('#success_message').text('Data saved');
            }

        });
        return false;
    });
});