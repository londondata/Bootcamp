$(document).ready(function(){

console.log('app.js is loaded');

  $('#work').on('click', function(){
    console.log('please work');
    console.log($(this));
    var button = $(this);
    var energy = button.data('energy');
    var mood = button.data('mood');
    var knowledge = $(this).data('knowledge');
    var stats = $.parseJSON(button.data('stats'));
    console.log(energy, mood, data);
    console.log(stats);
  })
})



$(document).ready( function() {

    $(".event-btn").click( function(event) {
        alert("You made your decision...");
    });
});
