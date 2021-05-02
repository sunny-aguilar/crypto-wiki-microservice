// author:   Sandro Aguilar

// event listener to wait for DOM to load before running script
document.addEventListener("DOMContentLoaded", runScript, false);

// function that adds an event listener for click events
function runScript(event) {
  console.log('Script Activated');
  const parent = document.body;
  parent.addEventListener("click", expandRow, false);
}

function expandRow(event) {
  const ele = event.target;
  console.log(ele);
}