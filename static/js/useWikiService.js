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


  let url = buildURL("bitcoin")
  // let url = buildURL("ethereum")
  // let url = buildURL("litecoin")
  // let url = buildURL("Dai_(cryptocurrency)")
  // let url = buildURL("tether_(cryptocurrency)")
  // let url = buildURL("Chainlink_(cryptocurrency)")
  // let url = buildURL("uniswap")


  makeRequest(url);
}


// -------------------------------------------------------------------------
//  Name:       buildURL(asset)
//  Purpose:    builds URL for wiki api
// -------------------------------------------------------------------------
function buildURL(asset) {
  // const base_url = "http://flip3.engr.oregonstate.edu:55055/api?";  // use this URL when saving to OSU servers
  // const base_url = "https://crypto-wiki.herokuapp.com/api?";   // for Heroku
  const base_url = "http://localhost:55055/api?";   // update to heroku

  // URL parameter settings
  const search_term = `search_term=${asset}&`;
  const summary_param = "summary=on";
  const url = base_url + search_term + summary_param;
  console.log(url);
  return url;
}


// -------------------------------------------------------------------------
//  Name:       makeRequest(url)
//  Purpose:    makes AJAX requests
// -------------------------------------------------------------------------
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
      updateSummary("btc_summary");
    }
    else {
      console.log("ERROR in executing AJAX");
    }
  });


  // send GET request
  xhr.open("GET", url, true);
  xhr.send(null);
}


// -------------------------------------------------------------------------
//  Name:       updateSummary(text)
//  Purpose:    uses DOM manipulation to add text to crypto asset list
//              based on data returned from wiki scraper service.
// -------------------------------------------------------------------------
function updateSummary(text, coin_id) {

}