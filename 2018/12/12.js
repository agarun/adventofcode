const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, './input');
const input = fs.readFileSync(file, { encoding: 'utf-8' });

const generationZero = /initial\sstate:\s(.+)/.exec(input)[1];

const notes = input
  .split(/\r\n|\r|\n/)
  .slice(2, -1)
  .reduce((map, spreadNote) => {
    const note = spreadNote.slice(0, 5);
    const next = spreadNote.slice(-1);
    map[note] = next;
    return map;
  }, {});

const evolve = state => {
  state = `....${state}....`;

  let newState = state.split('');

  for (let i = 2; i < state.length - 2; i += 1) {
    const slice = state.slice(i - 2, i + 2 + 1);
    const newPot = notes[slice] || '.'; // '.' is just for the sample input
    newState[i] = newPot;
  }

  return newState.join('');
};

const sumPlantPots = (pots, indexOffset) => {
  let sum = 0;

  for (let i = 0; i < pots.length; i++) {
    const pot = pots[i];
    if (pot === '#') {
      const potNumber = i - indexOffset;
      sum += potNumber;
    }
  }

  return sum;
};

const part1 = generations => {
  let i = 0;
  let pots = generationZero;
  while (i < generations) {
    pots = evolve(pots);
    i += 1;
  }
  // offset is i * 4 since we pad every iteration with `....`
  return sumPlantPots(pots, i * 4);
};

const part2 = generations => {
  let i = 0;
  let pots = generationZero;

  let lastSum = 0;
  let lastSumDiff = 0;
  while (i < generations) {
    pots = evolve(pots);
    i += 1;

    const potsSum = sumPlantPots(pots, i * 4);
    const potsSumDiff = potsSum - lastSum;

    // there are some smaller chains of uniform sums between
    // generations, but the long chain that we are interested
    // in appears around ~200 iterations
    if (potsSumDiff === lastSumDiff && i >= 200) {
      const generationsLeft = generations - i;
      return potsSumDiff * generationsLeft + potsSum;
    } else {
      lastSum = potsSum;
      lastSumDiff = potsSumDiff;
    }
  }
  return sumPlantPots(pots, i * 4);
};

console.log(part1(20));
console.log(part2(50000000000));

module.exports = { part1, part2 };
