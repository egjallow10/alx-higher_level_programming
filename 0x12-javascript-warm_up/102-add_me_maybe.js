#!/usr/bin/node

module.exports.addMeMaybe = function (x, func) {
  x++;
  func(x);
};
