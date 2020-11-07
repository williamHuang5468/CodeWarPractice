function solution(number){
  if (number < 0) return 0;
  var sum=0;
  for (var step = 1; step < number; step++) {
    if (step % 3 === 0){
      sum+=step;
      continue;
    }
    else if(step % 5 ===0 ){
      sum+=step;
      continue;
    }
    else
      continue;
  }
  return sum;
}