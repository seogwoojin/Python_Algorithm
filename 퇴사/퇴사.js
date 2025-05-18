let fs = require('fs');
let filePath = process.platform === 'linux' ? '/dev/stdin' : '/input.txt';
let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split('\n');

let N = +input.shift()

let answer = new Array(N + 2).fill(0);
for(let i = 0 ; i < N; i++){
  let [t, p] = input.shift().split(" ").map(Number)
  let end_date = i+1+t
  
  for(let j = end_date; j<=N+1; j++){
    if (answer[j] < answer[i+1] + p){
      answer[j] = answer[i+1]+p
    }
    else break;
  }
}
console.log(answer[N+1])