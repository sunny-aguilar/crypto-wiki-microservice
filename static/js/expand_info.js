// author:   Sandro Aguilar

// event listener to wait for DOM to load before running script
document.addEventListener("DOMContentLoaded", runScript, false);

// function that adds an event listener for click events
function runScript(event) {
  const parent = document.body;
  // parent.addEventListener("click", expandRow, false);
}

// toggles additional info for coins
function expandRow(event) {
  const ele = event.target;
  // filter more button clicks
  if (ele.value != "more") { return; }

  console.log("Expand Section Button Clicked >>>>>>>>>");

  // get node
  // const info_node = ele.parentNode.parentNode.nextElementSibling;
  const info_node = document.getElementById('hide-me');
  console.log(info_node);

  // toggle info section
  if (info_node.style.display === "none") { info_node.style.display = "block"; }
  else { info_node.style.display = "none"; }




}

$(document).ready(function(){
  $("input").click(function(){
    $("#hide-me").hide();
  });
  $("button").click(function(){
    $("#hide-me").show();
  });
});

// $(document).ready(function(){
//   $("input").click(function(){
//     $("p").hide(1000);
//   });
// });