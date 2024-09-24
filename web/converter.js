import { extractGIFFrames } from "./util.js";

const pixilFrame = {
  "name": "",
  "speed": 0, // modify delay
  "layers": [
    {
      "id": 0,
      "src": 0, // modify image
      "edit": false,
      "name": "Background",
      "opacity": 1,
      "active": true,
      "unqid": 0, // modify unique id
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
  "unqid": 0, // modify unique id
  "preview": 0, // modify image
  "width": 0, // modify
  "height": 0 // modify
};

const pixilContainer = {
  "application": "pixil",
  "type": ".pixil",
  "version": "2.7.0",
  "website": "pixilart.com",
  "author": "https://www.pixilart.com",
  "contact": "support@pixilart.com",
  "width": 0, // width
  "height": 0, // height
  "colors": {
    "palette": [
      "000000",
      "ffffff"
    ]
  },
  "colorSelected": "palette",
  "frames": 0, // frames
  "currentFrame": 0,
  "speed": 100,
  "name": "Untitled",
  "preview": "",
  "previewApp": "",
  "art_edit_id": 0,
  "palette_id": false,
  "created_at": 0, // time
  "updated_at": 0, // time
  "id": 0 // time
};

// function to convert file
function convertFile(file, callback) {
  if (file.type === "image/gif") {
    convertGif(file, callback);
    return;
  };
  convertImage(file, callback);
}

// function to return pixilart image object

function convertGif(gif, callback) {
  if (gif.type !== "image/gif") {
    throw "File not a GIF!";
  }
  
  // unique id generator
  var uniqueId = 0;
  function getUniqueId() {
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
    
    // clone json
    const pFrame = structuredClone(pixilFrame);
    
    // set relevant attributes
    pFrame.speed = img.delay;
    pFrame.layers[0].src = encoded;
    pFrame.layers[0].unqid = getUniqueId();
    pFrame.unqid = getUniqueId();
    pFrame.preview = encoded;
    pFrame.width = img.width;
    pFrame.height = img.height;
    
    return pFrame;
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
    
    // clone json
    const output = structuredClone(pixilContainer);
    
    // set relevant attributes
    output.width = frames[0].width;
    output.height = frames[0].height;
    output.frames = encodedFrames;
    output.created_at = time;
    output.updated_at = time;
    output.id = time;
    
    // use callback function
    callback(output);
  });
}

function convertImage(file, callback) {
  // unique id generator
  var uniqueId = 0;
  function getUniqueId() {
    uniqueId++; // increment by 1
    return String(uniqueId).padStart(6, "0") // pad with 0
  }
  
  // read file
  const reader = new FileReader();
  reader.readAsDataURL(file);
  
  // when loading finished
  reader.addEventListener("load", () => {
    // make image
    const image = new Image();
    image.src = reader.result;
    
    // when loading finished
    image.addEventListener("load", () => {
      // make canvas
      const canvas = document.createElement("canvas");
      canvas.width = image.width;
      canvas.height = image.height;
      
      // get context
      const ctx = canvas.getContext('2d');
      
      // draw image
      ctx.drawImage(image, 0, 0);
      
      const encoded = "data:image/pngp98kjasdnasd983/24kasdjasdbase64," + canvas.toDataURL().substring(22);
      
      const pFrame = structuredClone(pixilFrame);
      pFrame.speed = 100;
      pFrame.layers[0].src = encoded;
      pFrame.layers[0].unqid = getUniqueId();
      pFrame.unqid = getUniqueId();
      pFrame.preview = encoded;
      pFrame.width = image.width;
      pFrame.height = image.height;
      
      const time = Math.floor(Date.now() / 1000);
      
      const output = structuredClone(pixilContainer);
      
      output.width = image.width;
      output.height = image.height;
      output.frames = [pFrame]; // one image one frame
      output.created_at = time;
      output.updated_at = time;
      output.id = time;
      
      callback(output);
    });
  });
}

export { convertFile };