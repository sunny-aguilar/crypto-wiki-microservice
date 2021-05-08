 Authors:                                Sandro Aguilar
 Date:                                   April 20, 2021
 Class:                                  CS 361
 Description:                            This module holds the api endpoint for the web app
                                         and is a separate blueprint module. This API
                                         end-point is to access a Wikipedia webscraper.
 Base URL:                               http://localhost:55055/api

-------------------------------------------------------------------------

// event listener to wait for DOM to load before running script
document.addEventListener("DOMContentLoaded", runScript, false);

// function that adds an event listener for click events
function runScript(event) {
  const parent = document.body;
  parent.addEventListener("click", expandRow, false);
}

// toggles additional info for coins
function expandRow(event) {
  const ele = event.target;
  // filter more button clicks
  if (ele.value != "more") { return; }

  console.log("Expand Section Button Clicked >>>>>>>>>");

  // get node
  const info_node = ele.parentNode.parentNode.nextElementSibling;
  // const info_node = document.getElementById('hide-me');
  console.log(info_node);

  // toggle info section



}



$(document).ready(function(){
  $("input").click(function(){
    $(".hide_info").toggle(400);
  });
});

