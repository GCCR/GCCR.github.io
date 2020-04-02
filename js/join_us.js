$(function() {

  $("#joinForm input,#joinForm select").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, event, errors) {
      // additional error messages or events
    },
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // create timestamp
      var date = new Date.now();
      var timestamp = (date.getDate() + '/' + date.getMonth()+1) + '/' +  date.getFullYear();
      // get values from FORM
      var name = $("input#ms_name").val();
      var institution = $("input#ms_institution").val();
      var country = $("select#ms_country").val();
      var agreement = $("input#ms_agreement").is(":checked");
      var firstName = name; // For Success/Failure Message
      // Check for white space in name for Success/Fail message
      if (firstName.indexOf(' ') >= 0) {
        firstName = name.split(' ').slice(0, -1).join(' ');
      }
      $this = $("#joinFormButton");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "././mail/join_us.php",
        type: "POST",
        data: {
          name: name,
          date: timestamp,
          institution: institution,
          country: country,
          agreement: agreement
        },
        cache: false,
        success: function() {
          // Success message
          $('#ms_success').html("<div class='alert alert-success'>");
          $('#ms_success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#ms_success > .alert-success')
            .append("<strong>Your membership form has been submitted and will be processed shortly. </strong>");
          $('#ms_success > .alert-success')
            .append('</div>');
          //clear all fields
          $('#joinForm').trigger("reset");
        },
        error: function() {
          // Fail message
          $('#ms_success').html("<div class='alert alert-danger'>");
          $('#ms_success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#ms_success > .alert-danger').append($("<strong>").text("Sorry " + firstName + ", it seems that our mail server is not responding. Please try again later!"));
          $('#ms_success > .alert-danger').append('</div>');
          //clear all fields
          $('#joinForm').trigger("reset");
        },
        complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });

  $("a[data-toggle=\"tab\"]").click(function(e) {
    e.preventDefault();
    $(this).tab("show");
  });
});

/*When clicking on Full hide fail/success boxes */
$('#ms_name').focus(function() {
  $('#ms_success').html('');
});
