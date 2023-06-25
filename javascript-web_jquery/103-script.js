// cors issues, keypress event works and code works!
$(document).ready(function(){
    $('INPUT#btn_translate').click(function(){
        translateHello();
    });

    $('INPUT#language_code').keypress(function(event){
        if (event.which === 13){
            translateHello();
        }
    });

    function translateHello(){
        const languageCode = $('INPUT#language_code').val();
        $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data){
            $('#hello').text(data.hello);
        });
    }
});
