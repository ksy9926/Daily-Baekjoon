const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  //   input = line.split(" ").map((el) => parseInt(el));
  input.push(parseInt(line.split("/n")));
}).on("close", function () {
  let answer = input.slice(1).sort((a, b) => a - b);
  answer.forEach((value) => console.log(value));
  process.exit();
});
