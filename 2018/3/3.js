const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, './input');
const fileInput = fs.readFileSync(file, { encoding: 'utf-8' }).split('\n');

const part1 = textInput => {
  let claims = textInput || fileInput;

  const coords = {};
  for (let i = 0; i < claims.length; i += 1) {
    const claim = claims[i];
    const regexp = /^#\d+\s@\s(\d+),(\d+):\s(\d+)x(\d+)$/;
    const matches = claim.match(regexp);
    const [y, x, width, height] = matches.slice(1).map(val => parseInt(val));

    for (let i = x + 1; i <= x + height; i += 1) {
      for (let j = y + 1; j <= y + width; j += 1) {
        if (coords[`${i},${j}`]) {
          coords[`${i},${j}`] += 1;
        } else {
          coords[`${i},${j}`] = 1;
        }
      }
    }
  }

  let overlaps = Object.values(coords).filter(occupants => occupants >= 2)
    .length;
  return overlaps;
};

const part2 = textInput => {
  let claims = textInput || fileInput;

  const coords = {};
  for (let i = 0; i < claims.length; i += 1) {
    const claim = claims[i];
    const regexp = /^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$/;
    const matches = claim.match(regexp);
    const [id, y, x, width, height] = matches
      .slice(1)
      .map(val => parseInt(val));

    for (let i = x + 1; i <= x + height; i += 1) {
      for (let j = y + 1; j <= y + width; j += 1) {
        if (coords[`${i},${j}`]) {
          coords[`${i},${j}`].push(id);
        } else {
          coords[`${i},${j}`] = [id];
        }
      }
    }
  }

  // it'd probably be faster to use sets or partition the coords values array
  const flatOverlaps = flatten(
    Object.values(coords).filter(occupants => occupants.length >= 2)
  );
  const flatSingles = flatten(
    Object.values(coords).filter(occupants => occupants.length == 1)
  );

  return flatSingles.filter(s => !flatOverlaps.includes(s))[0];
};

function flatten(array, result = []) {
  for (let i = 0, length = array.length; i < length; i += 1) {
    const value = array[i];
    if (Array.isArray(value)) {
      flatten(value, result);
    } else {
      result.push(value);
    }
  }
  return result;
}

module.exports = { part1, part2 };
