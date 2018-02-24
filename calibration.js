// run with: node calibration.js

/*
    0,   0: 560, 150
    0, 200: 556, 365
  300,   0: 254, 148
*/

nudged = require('nudged')

var domain = [[0, 0], [300, 0], [0, 300], [200, 100]]
var range = [[560, 108], [240, 139], [574, 432], [354, 239]]

var t = nudged.estimate('TSR', domain, range)

console.log(t)
console.log(t.transform([0, 300]))
