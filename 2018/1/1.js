const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, './input');

// 1
fs.readFile(file, { encoding: 'utf-8' }, (error, data) => {
  if (!error) {
    const array = data.split('\n');
    const sum = array
      .map(value => parseInt(value))
      .reduce((previousValue, currentValue) => previousValue + currentValue, 0);
    console.log(sum);
  }
});

// 2
const freqs = fs.readFileSync(file, { encoding: 'utf-8' });
const freqsSeen = {};
let currentFreq = 0;
const duplicateFreqs = [];
while (!duplicateFreqs.length) {
  freqs
    .split('\n')
    .map(freq => parseInt(freq))
    .forEach(freq => {
      currentFreq += freq;
      freqsSeen[currentFreq] = freqsSeen[currentFreq]
        ? freqsSeen[currentFreq] + 1
        : 1;
      if (freqsSeen[currentFreq] === 2) {
        duplicateFreqs.push(currentFreq);
      }
    });
}
console.log(duplicateFreqs);
