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
  const base_url = "http://flip3.engr.oregonstate.edu:55055/api?";

  // URL parameter settings
  const btc = "search_term=bitcoin&";
  const summary = "summary=on";

  const urlRequest = base_url + btc + summary;

  // AJAX request
  const xhr = new XMLHttpRequest();

  // even listener for request
  xhr.addEventListener("load", () => {
    if (xhr.status === 200 && xhr.readyState == 4) {
      console.log("<<---- XHR SERVER RESPONDED");
    }
    else {
      console.log("ERROR in executing AJAX");
    }
  });

  // send GET request
  xhr.open()

}

