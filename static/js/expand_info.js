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

  // console.log("Expand Section Button Clicked >>>>>>>>>");

  // get node
  const info_node_id = ele.parentNode.parentNode.nextElementSibling.id;
  // console.log(info_node_id);



}


$(document).ready(function(){
  const parent = document.body;
  parent.addEventListener("click", getButton, false);
  function getButton(event) {
    console.log("Event: ", event);
  }



  $("#btc_button").click(function(){
    $("#bitcoin_info_section").toggle(400);
  });
  $("#ethereum_button").click(function(){
    $("#ethereum_info_section").toggle(400);
  });
});
