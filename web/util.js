function extractGIFFrames(gifFile, callback) {
  if (gifFile.type !== 'image/gif') {
    throw new Error('The file provided is not a valid GIF.');
  }

  const reader = new FileReader();

  reader.onload = function (event) {
    const arrayBuffer = event.target.result;

    // Create a new GIF instance
    const gif = new GIF(arrayBuffer);

    // Decompress frames
    const frames = gif.decompressFrames(true); // true = we want the pixel data

    // Extract frame data (e.g., width, height, patch, delay)
    const extractedFrames = frames.map((frame) => ({
      width: frame.dims.width,
      height: frame.dims.height,
      patch: frame.patch,  // Raw pixel data for the frame
      delay: frame.delay   // Frame delay in hundredths of a second
    }));

    callback(extractedFrames);  // Pass the extracted frames to the callback
  };

  reader.onerror = function () {
    throw new Error('Error reading the GIF file.');
  };

  // Read the GIF file as an ArrayBuffer
  reader.readAsArrayBuffer(gifFile);
}

export { extractGIFFrames };
