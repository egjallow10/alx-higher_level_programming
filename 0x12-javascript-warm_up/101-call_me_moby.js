#!/usr/bin/node

module.exports.callMeMoby = function (x, func) {
  if (x > 0) {
    for (let i = 0; i < x; i++) {
      func();
    }
  }
};
