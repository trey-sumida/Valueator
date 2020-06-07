console.log("dog");

//function hides/shows subscription hours based upon exp-type value
function check_field_value(new_val) {
    console.log(new_val);
    if(new_val != 'Digital Subscription') {
        $('#add-hours').hide();
    } else {
        $('#add-hours').show();
    }
}

// this is executed once when the page loads
$(document).ready(function() {
    console.log("cat");
    // set things up so my function will be called when exp-type changes
    $('#exp-type').change( function() {
        console.log("cat2");
        var val = document.getElementById('topic_text').value
        console.log(val);
        check_field_value(val);
    });

});