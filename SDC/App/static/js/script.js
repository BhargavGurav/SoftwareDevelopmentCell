$(document).ready(function(){
    $('#email').keyup(function(){
        this.value = this.value.toLowerCase();
    });
})

$(document).ready(function(){
    $('#phone').inputmask('9999999999', {'onincomplete': function(){
        swal('Oops !', 'Please enter full contact number.', 'info')
        return false;
    }})
})

$(document).ready(function(){
    $('#prn').inputmask('9999999', {'onincomplete': function(){
        swal('Oops !', 'Please enter correct PRN.', 'info')
        return false;
    }})
})
$('#fname').keyup(function(){
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){
        return $1.toUpperCase( );
    }))
})

$(document).ready(function(){
    jQuery('input[name="fname"]').keyup(function(){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');  /* replacing space*/
        jQuery(this).val(allow);
    });

    $('input').on('keypress', function(e) { 
        if (e.which === 32 && !this.value.length)
        e.preventDefault();
    });

});

$('#lname').keyup(function(){
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){
        return $1.toUpperCase( );
    }))
})

$(document).ready(function(){
    jQuery('input[name="lname"]').keyup(function(){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');  /* replacing space*/
        jQuery(this).val(allow);
    });

    $('input').on('keypress', function(e) { 
        if (e.which === 32 && !this.value.length)
        e.preventDefault();
    });

});