//  Authors:                                Sandro Aguilar
//  Date:                                   May 8, 2021
//  Class:                                  CS 361
//  Description:                            This JS file is used send GET requests to the Wiki
//                                          API service that I have implemented. The code is not
//                                          called directly but rather an HTTP GET request is made
//                                          over the internet to request the service via this
//                                          script.
// -------------------------------------------------------------------------

// import module functions
import { cryptoSummaries } from "/static/js/cryptoData.js";

// event listener to wait for DOM to load before running script
document.addEventListener("DOMContentLoaded", runScript, false);

// function that adds an event listener for click events
function runScript(event) {
  useWikiService(event);
}

// function that calls Wiki Scraper service
function useWikiService(event) {
  // url for AJAX request

  // + +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  // + this section builds the URL for the GET request for the Wiki API
  // + and then sends the request to get coin summaries from the Wiki
  // + scraper micro-service.
  let url = buildURL("bitcoin")
  makeRequest(url, "btc_summary");
  url = buildURL("ethereum")
  makeRequest(url, "ethereum_summary");
  url = buildURL("litecoin")
  makeRequest(url, "litecoin_summary");
  url = buildURL("Dai_(cryptocurrency)")
  makeRequest(url, "dai_summary");
  url = buildURL("tether_(cryptocurrency)")
  makeRequest(url, "usdt_summary");
  url = buildURL("Chainlink_(cryptocurrency)")
  makeRequest(url, "chainlink_summary");
  url = buildURL("uniswap")
  makeRequest(url, "uniswap_summary");

  // + +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  // + Wikipedia does not have data on the following coins therefore the
  // + data for these coins is being hardcoded.
  updateSummary(cryptoSummaries["Polygon"], "polygon_summary");
  updateSummary(cryptoSummaries["Pancakeswap"], "pancakeswap_summary");
  updateSummary(cryptoSummaries["BNB"], "bnb_summary");
}


// -------------------------------------------------------------------------
//  Name:       buildURL(asset)
//  Purpose:    builds URL for wiki scraper microservice HTTP request.
// -------------------------------------------------------------------------
function buildURL(asset) {
  // const base_url = "http://flip3.engr.oregonstate.edu:55055/api?";  // use this URL when saving to OSU servers
  // const base_url = "http://localhost:55055/api?";   // update to heroku
  const base_url = "https://crypto-wiki.herokuapp.com/api?";   // for Heroku

  // URL parameter settings
  const search_term = `search_term=${asset}&`;
  const summary_param = "summary=on";
  const url = base_url + search_term + summary_param;
  console.log(url);
  return url;
}


// -------------------------------------------------------------------------
//  Name:       makeRequest(url)
//  Purpose:    makes AJAX requests to the Wiki microservice.
// -------------------------------------------------------------------------
function makeRequest(url, coin_id) {
  // AJAX request
  const xhr = new XMLHttpRequest();

  // even listener for request
  xhr.addEventListener("load", () => {
    if (xhr.status === 200 && xhr.readyState == 4) {
      console.log("<<---- XHR SERVER RESPONDED");

      const summary = JSON.parse(xhr.responseText)
      console.log(summary["summary"]);
      updateSummary(summary["summary"], coin_id);
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
  document.getElementById(coin_id).innerText = text;
}