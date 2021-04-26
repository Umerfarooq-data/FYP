function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}
console.log(isNumeric("ioiuoi"));
console.log(isNumeric("9"));
console.log(isNumeric("89898"));