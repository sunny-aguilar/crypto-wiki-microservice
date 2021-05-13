//  Authors:                                Sandro Aguilar
//  Date:                                   May 8, 2021
//  Class:                                  CS 361
//  Description:                            This JS file is used send GET requests to the Wiki
//                                          API service that I have implemented. The code is not
//                                          called directly but rather an HTTP GET request is made
//                                          over the internet to request the service via this
//                                          script.
// -------------------------------------------------------------------------

// event listener to wait for DOM to load before running script
document.addEventListener("DOMContentLoaded", runScript, false);

// function that adds an event listener for click events
function runScript(event) {
  const parent = document.body;
  parent.addEventListener("click", useWikiService, false);
}

// function that calls Wiki Scraper service
function useWikiService(event) {
  // url for AJAX request
  const url = "";
}

