const fs = require('fs');

const polymer = fs
  .readFileSync('./input', { encoding: 'utf-8' })
  .replace('\n', '');

const isSameMonomer = (a, b) => a.toLowerCase() === b.toLowerCase();

const isOppositePolarity = (a, b) => a !== b && isSameMonomer(a, b);

const react = (polymer, startIndex) => {
  return polymer.slice(0, startIndex) + polymer.slice(startIndex + 2);
};

// part 1
// overflows :(
// const memo = {};
// const scanPolymerPart1 = polymer => {
//   for (let i = 1; i < polymer.length; i += 1) {
//     const current = polymer[i];
//     const previous = polymer[i - 1];
//     if (isOppositePolarity(current, previous)) {
//       let newPolymer;
//       if (memo[polymer]) {
//         newPolymer = memo[polymer];
//       } else {
//         newPolymer = react(polymer, i - 1);
//         memo[polymer] = newPolymer;
//       }
//       return scanPolymer(newPolymer);
//     }
//   }
//   return polymer;
// };

const scanPolymerPart1 = polymer => {
  let unstable = true;
  while (unstable) {
    unstable = false;
    for (let i = 1; i < polymer.length; i += 1) {
      const current = polymer[i];
      const previous = polymer[i - 1];
      if (isOppositePolarity(current, previous)) {
        polymer = react(polymer, i - 1);
        unstable = true;
      }
    }
  }

  return polymer;
};

// console.log(scanPolymerPart1(polymer).length);

const alphabet = 'abcdefghijklmnopqrstuvwxyz';
// i.e. map to monomer => subtractMonomer(polymer, monomer),
//      map to subtractedMonomer => reactedMonomer
//      => Math.min

const subtractMonomer = (polymer, monomer) => {
  const newPolymer = [];
  const targetMonomer = monomer.toLowerCase();
  monomers = polymer.split('');
  for (let i = 0; i < monomers.length; i += 1) {
    if (monomers[i].toLowerCase() !== targetMonomer) {
      newPolymer.push(monomers[i]);
    }
  }
  return newPolymer.join('');
};

const scanPolymerPart2 = polymer => {
  const lengths = [];
  for (let i = 0; i < alphabet.length; i += 1) {
    const newPolymer = subtractMonomer(polymer, alphabet[i]);
    lengths.push(scanPolymerPart1(newPolymer).length);
  }
  return Math.min(...lengths);
};

// console.log(scanPolymerPart2(polymer));

module.exports = { part1: scanPolymerPart1, part2: scanPolymerPart2 };
