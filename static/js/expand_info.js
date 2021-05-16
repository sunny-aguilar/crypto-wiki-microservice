//  Authors:                                Sandro Aguilar
//  Date:                                   May 8, 2021
//  Class:                                  CS 361
//  Description:                            This JS file is used to add interactivity to
//                                          the Crypto Asset list GUI.

// -------------------------------------------------------------------------

// event listener to wait for DOM to load before running script
document.addEventListener("DOMContentLoaded", runScript, false);

// function that adds an event listener for click events
function runScript(event) {
  const parent = document.body;
  parent.addEventListener("click", getElement, false);
}

// toggles additional info for coins
function getElement(event) {
  const ele = event.target;
  // filter more button clicks
  if (ele.value != "more") { return; }

  console.log("Expand Section Button Clicked >>>>>>>>>");

  // get node
  const info_node_id = ele.parentNode.parentNode.nextElementSibling.id;
  // const info_node = document.getElementById('hide-me');
  console.log(info_node_id);

  // toggle info section



}



$(document).ready(function(){
  $("input").click(function(){
    $(".hide_info").toggle(400);
  });
});

