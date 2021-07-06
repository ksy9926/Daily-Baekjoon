const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let input_count = {};

rl.on("line", function (line) {
  //   input = line.split(" ").map((el) => parseInt(el));
  input.push(parseInt(line.split("/n")));
}).on("close", function () {
  answer = input.slice(1);
  avg = 0;
  for (let i = 0; i < answer.length; i++) {
    avg += answer[i];
    input_count[answer[i]] > 0
      ? (input_count[answer[i]] += 1)
      : (input_count[answer[i]] = 1);
  }
  avg /= answer.length;
  console.log(Math.round(avg));

  answer = answer.sort((a, b) => a - b);
  console.log(answer[(answer.length - 1) / 2]);
  console.log(answer[answer.length - 1] - answer[0]);
  console.log(input_count);
  process.exit();
});
