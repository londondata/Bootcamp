$(document).ready(function(){

console.log('sanity check');

$('#event1-form').on('submit', function(event){
    event.preventDefault();
    console.log("you made your decision.")  // sanity check
    create_post();
  })

  $('form').on('submit', function(e){
    e.preventDefault();
    console.log('please work');
    let form = $(this);
    let form_data = $(form).serialize();
    let json_data = JSON.stringify(form_data);
    let id = $('input[name=id]').val();
    let csrftoken = $("[name=csrfmiddlewaretoken]").val();
    let energy=$('input[name=energy]').val();
    let mood =$('input[name=mood]').val();
    let knowledge = $('input[name=knowledge]').val();
    console.log(id);
    console.log(form_data)

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            console.log('token sent' )
        }
    }
});

    $.ajax({
      type: 'POST',
      url: `/character/update/${id}/`,
      data: {
        "csrfmiddlewaretoken": csrftoken,
        // "json_data": json_data,
        "form_data": form_data,
        // "id": "4",
        // "energy": "-5",
        // "mood": "-5",
        // "knowledge": "10"
      },
      contentType: 'application/json',
      success: function() {
        console.log('this form was submitted ' + form_data)
      },
      error: function(error) {
        console.log(error);
      }
    })

  })
