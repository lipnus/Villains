function submit(){
    var email = document.getElementsByName('email')[0].value;
    if (email.match('@korea.ac.kr')=='@korea.ac.kr'){
        document.getElementsByClassName('univ_email_error')[0].style.display="none";
        document.getElementsByClassName('form')[0].submit();
        return;
    }
    else{
        var alert = document.getElementsByClassName('registration_alert');
        if (alert!=null){
            for (var i=0; i<alert.length; i++)
                alert[i].style.display="none";
        }
        document.getElementsByClassName('univ_email_error')[0].style.display="block";
        return;
    }
}