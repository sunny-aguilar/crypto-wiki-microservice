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
  // parent.addEventListener("load", useWikiService, false);
  useWikiService(event);
}

// function that calls Wiki Scraper service
function useWikiService(event) {
  // url for AJAX request
  // const base_url = "http://flip3.engr.oregonstate.edu:55055/api?";  // use this URL when saving to OSU servers
  // const base_url = "https://crypto-wiki.herokuapp.com/api?";   // for Heroku
  const base_url = "http://localhost:55055/api?";   // update to heroku

  // URL parameter settings
  const btc = "search_term=bitcoin&";
  const summary = "summary=on";

  const url = base_url + btc + summary;
  console.log(url);

  makeRequest(url);

  // AJAX request
  // const xhr = new XMLHttpRequest();



}

function makeRequest(url) {
  // AJAX request
  const xhr = new XMLHttpRequest();

  // even listener for request
  xhr.addEventListener("load", () => {
    if (xhr.status === 200 && xhr.readyState == 4) {
      console.log("<<---- XHR SERVER RESPONDED");

      const summary = JSON.parse(xhr.responseText)
      console.log(summary);
      console.log(summary["summary"]);
      document.getElementById("btc_summary").innerText = summary["summary"];
    }
    else {
      console.log("ERROR in executing AJAX");
    }
  });


  // send GET request
  xhr.open("GET", url, true);
  xhr.send(null);
}