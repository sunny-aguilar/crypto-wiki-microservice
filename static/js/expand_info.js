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
  // Tooltips for Bootstraip
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })
}


// add toggle functionality to main page
$(document).ready(function(){
  $("#btc_button").click(function(){
    $("#bitcoin_info_section").toggle(400);
  });
  $("#ethereum_button").click(function(){
    $("#ethereum_info_section").toggle(400);
  });
  $("#litecoin_button").click(function(){
    $("#litecoin_info_section").toggle(400);
  });
  $("#dai_button").click(function(){
    $("#dai_info_section").toggle(400);
  });
  $("#usdt_button").click(function(){
    $("#usdt_info_section").toggle(400);
  });
  $("#chainlink_button").click(function(){
    $("#chainlink_info_section").toggle(400);
  });
  $("#uniswap_button").click(function(){
    $("#uniswap_info_section").toggle(400);
  });
  $("#polygon_button").click(function(){
    $("#polygon_info_section").toggle(400);
  });
  $("#pancakeswap_button").click(function(){
    $("#pancake_info_section").toggle(400);
  });
  $("#bnb_button").click(function(){
    $("#bnb_info_section").toggle(400);
  });
});