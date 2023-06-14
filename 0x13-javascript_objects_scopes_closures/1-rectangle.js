#!/usr/bin/node
/**
 * defines a rectangle class.
 */
class Rectangle {
  /**
   * initialises an instance of the class
   * @param {Number} w -- width
   * @param {Number} h -- the value of the height
  */
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
