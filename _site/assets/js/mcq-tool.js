// Logic behind the mcq tool
$(document).ready(function(){
$(".mcq-tools").click(function(){
    // var choices = [];

    if ($("#mcq-tools-1").is(':checked') || $("#mcq-tools-2").is(':checked')) {
        // choices.push("#ModalSurvey");
        var choice = "#ModalBoth";
    } 
    if ($("#mcq-tools-3").is(':checked') || $("#mcq-tools-4").is(':checked') || $("#mcq-tools-5").is(':checked')) {
        // choices.push("#ModalSelfCheck");
        var choice = "#ModalSelfCheck";
    }
    // if (choices.includes("#ModalSurvey") && choices.includes("#ModalSelfCheck")) {
    //   var choice = "#ModalBoth";
    // } else {
    //   var choice = choices[0];
    // }
    $(choice).modal();
    });
});