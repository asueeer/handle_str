var myF = require('./index.js');
const fs = require('fs');
let rawdata = fs.readFileSync('./input.json');
const event = {
    body: rawdata
  };


myF.handler(event).
  then((result) => {
    console.log(result);
  }).
  catch(err => {
    console.log(err);
  });
