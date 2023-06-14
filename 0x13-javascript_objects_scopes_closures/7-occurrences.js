#!/usr/bin/node
/**
 * Computes number of occurrences of element in a list.
 * @param {Array} list list of elements.
 * @param {Any} searchElement element to look for.
 * @returns {Number} number of occurrences of given element.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(item => item === searchElement).length;
};
