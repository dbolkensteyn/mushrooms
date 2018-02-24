// run with: node calibration.js
nudged = require('nudged')

var domain = [[0, 0], [300, 0], [0, 300], [200, 100]]
var range = [[560, 108], [240, 139], [574, 432], [354, 239]]

var t = nudged.estimate('TSR', domain, range)

console.log(t)
console.log(t.transform([0, 300]))
