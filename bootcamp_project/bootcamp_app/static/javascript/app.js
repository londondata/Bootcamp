$(document).ready(() => {
  console.log('app.js loaded!');
})

$('#event1-form').on('submit', function(event){
    event.preventDefault();
    console.log("you made your decision.")  // sanity check
    create_post();
});
