function isOdd(arg){
  return (arg % 2 === 1);
}

function findOdd(A) {
  var mappingTable = {};
  for (var i = 0; i < A.length; i++) {
    var item = A[i];
    if(mappingTable[item]===undefined){
      mappingTable[item] = 1;
    } else{
      mappingTable[item] += 1;
    }
  }
  for (var key in mappingTable ){
    var value = mappingTable[key];
    if (isOdd(value)) return parseInt(key);
  }
}