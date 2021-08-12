const { stdout } = require('process');
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.on('line', (line) => {
  let n = new Number(line);
  for(let i = 1; i < 10; i++) {
    console.log(`${n} * ${i} = ${n * i}`)
  }
  rl.close();
}).on('close', () => {
  process.exit();
})