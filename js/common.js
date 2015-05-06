// Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
// This file is licensed under the terms of the MIT License.
// See LICENSE.txt for details.

if (!String.prototype.format) {
  String.prototype.format = function() {
    var str = this.toString();
    if (!arguments.length)
      return str;
    switch (typeof arguments[0]) {
      case 'string':
      case 'number':
        var args = arguments;
        break;
      default:
        var args = arguments[0];
        break;
    }
    for (var arg in args)
      str = str.replace(new RegExp('\\{' + arg + '\\}', 'gi'), args[arg]);
    return str;
  }
}
