#!/usr/bin/node
let num = 0;
/**
 * Logs message to console.
 * @param {String} item message to be logged.
 */
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};
