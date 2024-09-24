import { extractGIFFrames } from "./util.js";

// function to convert file
function convertFile(file, callback) {
  if (file.type === "image/gif") convertGif(file, callback);
  
  // make png later
  // if (file.type === "image/png") convertPng(file, callback);
}

// function to return pixilart image object

function convertGif(gif, callback) {
  if (gif.type !== "image/gif") {
    throw "File not a GIF!";
  }
  
  var uniqueId = 0;
  function getUniqueId() { // get unique id for images
    uniqueId++; // increment by 1
    return String(uniqueId).padStart(6, "0") // pad with 0
  }
  
  // create off-screen canvas element
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  
  // convert image to pixilart obj
  function convert(img) {
    // create imageData object
    const idata = ctx.createImageData(canvas.width, canvas.height);

    // set our buffer as source
    idata.data.set(img.patch);

    // update canvas with new data
    ctx.putImageData(idata, 0, 0);
    
    // replace data:image/png;base64, with custom
    const encoded = "data:image/pngp98kjasdnasd983/24kasdjasdbase64," + canvas.toDataURL().substring(22);
    
    return {
      "name": "",
      "speed": img.delay,
      "layers": [
        {
          "id": 0,
          "src": encoded, // image
          "edit": false,
          "name": "Background",
          "opacity": 1,
          "active": true,
          "unqid": getUniqueId(), // unique id
          "options": {
            "blend": "source-over",
            "locked": false,
            "filter": {
              "brightness": "100%",
              "contrast": "100%",
              "grayscale": "0%",
              "blur": 0,
              "hue-rotate": 0,
              "dropshadow_x": 0,
              "dropshadow_y": 0,
              "dropshadow_blur": 0,
              "dropshadow_alpha": 1
            }
          }
        }
      ],
      "active": true,
      "selectedLayer": 0,
      "unqid": getUniqueId(), // unique id
      "preview": encoded, // image
      "width": img.width,
      "height": img.height
    }
  }
  
  extractGIFFrames(gif, (frames) => {
    // console.log(frames); // frames of gif
    
    const encodedFrames = [];
    
    // set dimensions of canvas
    canvas.width = frames[0].width;
    canvas.height = frames[0].height;
    
    frames.forEach((frame) => {
      encodedFrames.push(convert(frame));
    });

    // console.log(encodedFrames);
    
    // get unix time in seconds rather than ms
    const time = Math.floor(Date.now() / 1000);
    
    const output = {
      "application": "pixil",
      "type": ".pixil",
      "version": "2.7.0",
      "website": "pixilart.com",
      "author": "https://www.pixilart.com",
      "contact": "support@pixilart.com",
      "width": frames[0].width,
      "height": frames[0].height,
      "colors": {
        "palette": [
          "000000",
          "ffffff"
        ]
      },
      "colorSelected": "palette",
      "frames": encodedFrames,
      "currentFrame": 0,
      "speed": 100,
      "name": "Untitled",
      "preview": "",
      "previewApp": "",
      "art_edit_id": 0,
      "palette_id": false,
      "created_at": time,
      "updated_at": time,
      "id": time
    }
    
    // use callback function
    callback(output);
  });
}

function convertPng(png, callback) {
  // nah
}

export { convertFile };