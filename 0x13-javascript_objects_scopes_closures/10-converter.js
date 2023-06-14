#!/usr/bin/node
/**
 * Creates number to string conversion function with given base.
 * @param {Number} base base of the conversion function.
 * @returns {Function} A conversion function.
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
