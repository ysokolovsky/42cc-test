$(document).ready(function () {
    var url = window.location;
    $('ul.nav a[href="'+ url +'"]').parent().addClass('active');
    $('ul.nav a').filter(function() {
        return this.href == url;
    }).parent().addClass('active');


    var options = {
        target: '#form',
        beforeSubmit: processRequest,
        success: showResponse,
        dataType: 'json'
    };

    $('#form').ajaxForm(options);

    jQuery(document).ajaxStart(function(){
        $('#success_message').html("<p>Loading..</p>");
    });

    function processRequest() {
        $('#submit').unbind('click');
        $('form input').each( function() {
            $( this ).attr( "disabled", "disabled" );
        });
        $('form textarea').each( function() {
            $( this ).attr( "disabled", "disabled" );
        });
        return true;
    }

    jQuery(document).ajaxStop(function(){
        $('form input').each( function() {
            $( this ).removeAttr("disabled");
        });
        $('form textarea').each( function() {
            $( this ).removeAttr("disabled");
        });
    });


    function showResponse(responseText){
        var data = responseText;
        $('#form').find('.error').remove();
        if ($('#id_photo').val()) {
            $('img.col-md-offset-1').attr('src', "/media/photo/" + $('#id_photo').val());
            $('div.col-lg-6 a').attr('href', "/media/photo/" + $('#id_photo').val()).text("photo/" + $('#id_photo').val());
        } else {
            $('img.col-md-offset-1').attr('src', "");
            $('div.col-lg-6 a').attr('href', "").text("");
        }

        if(data['result'] == "error"){
            $('#success_message').html("<p>Changes not saved</p>");
            for (var k in data['response']) {
                $('#form').find('input[name=' + k + ']').after('<div class="error">' + data['response'][k] + '</div>');
                $('#form').find('textarea[name=' + k + ']').after('<div class="error">' + data['response'][k] + '</div>');
            }
        } else {
            $('#success_message').html("<p>Changes saved</p>");
        }
    }

});