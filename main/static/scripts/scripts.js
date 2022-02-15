function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}
jQuery(document).ready(function($) {
    window.realAlert=window.alert
    window.alert=function(s){
        customAlert(s)
    }

    function customAlert(s) {
        if($('#customalert')[0]) {
            if($('#customalert').hasClass('on')) {
                $('#customalert').find('.alerttext').html(s);
            }else{
                $('#customalert').addClass('on').find('.alerttext').html(s);
            }
        }else{
            $('body').append('<div id="customalert" class="on"><span class="alerttext">' + s + '</span><span id="contact-remove-sign"></span></div>');
        }
        $('#customalert').fadeIn(200);
    }
    
    $(document).on('click', '#customalert', function(){
        $(this).removeClass('on').fadeOut();
    });
    
});

function encodeImageFileAsURL(element, input_id) {
    const input_base64 = document.getElementById(input_id);
    var file = element.files[0];
    var reader = new FileReader();
    var base64;
    reader.onloadend = function() {
        input_base64.value = reader.result;
        $('#blah').attr('src', reader.result);
        $('#blah').attr('alt', 'таңдалды');
        $("#blah").css("display", 'block');
        $("#btn_upd").css("display", 'block');
    }
    reader.readAsDataURL(file);      
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result)
        };
        reader.readAsDataURL(input.files[0]);
    }
}