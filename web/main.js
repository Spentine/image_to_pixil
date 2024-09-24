import { convertFile } from "./converter.js";

function main() {
  const inputFile = document.getElementById("inputFile");
  const convertButton = document.getElementById("convertButton");
  const secretText = document.getElementById("hehe");
  const fairText = document.getElementById("fair");
  
  convertButton.addEventListener("click", () => {
    const file = inputFile.files[0]; // get the file (it's in 0)
    console.log(file); // log the file just for fun
    convertFile(file, (results) => {
      console.log(results); // results (object)
      
      const stringified = JSON.stringify(results); // stringified json
      const link = document.createElement("a"); // create link
      link.href = "data:text/plain;base64," + btoa(unescape(encodeURIComponent(stringified))); // set href
      link.download = "output.pixil"; // set download
      
      link.click(); // click the link for the user
    });
  });
  
  var secretClicks = 0;
  secretText.addEventListener("click", () => {
    secretClicks++;
    if (secretClicks > 2) {
      secretText.innerText = atob('bGVnZW5kYXJ5MTIzNDU=');
    }
  });
  
  var fairClicks = 0;
  fairText.addEventListener("click", () => {
    fairClicks++;
    if (fairClicks > 2) {
      fairText.innerText = atob('U2VycGVudGluZQ==');
    }
  });
}

document.addEventListener("DOMContentLoaded", main);