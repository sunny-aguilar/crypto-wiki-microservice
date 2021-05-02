// author:   Sandro Aguilar

// event listener to wait for DOM to load before running script
document.addEventListener("DOMContentLoaded", runScript, false);

// function that adds an event listener for click events
function runScript(event) {
  const parent = document.body;
  parent.addEventListener("click", expandRow, false);
}

function expandRow(event) {
  const ele = event.target;
  console.log(event.target);
  if (ele != '<i class="lni lni-arrow-down-circle"></i>') {
    console.log('Wrong target!');
    return;
  }

  console.log("Target found!");
}