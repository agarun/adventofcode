const fs = require('fs');

const fileInput = fs
  .readFileSync('./input', { encoding: 'utf-8' })
  .split('\n')
  .slice(0, -1);

function parseInput(input) {
  return input.map(line => {
    const [x, y] = line.split(', ').map(n => parseInt(n));
    return [x, y];
  });
}

/**
 * Finds max integer
 * @param {Array<Array<Number, Number>>} input - Array of [x, y] coordinates
 * @return {number} Largest x or y point
 */
function largestInt(input) {
  const coords = parseInput(input);
  return Math.max(...coords.map(coord => Math.max(...coord)));
}

function manhattanDistance([x1, y1], [x2, y2]) {
  return Math.abs(x1 - x2) + Math.abs(y1 - y2);
}

function squareGrid(size = largestInt(fileInput) + 1) {
  return Array(size)
    .fill()
    .map(() => Array(size));
}

// What is the size of the largest area that isn't infinite?
const part1 = (input = fileInput) => {
  const areas = {};
  const infiniteAreas = {};
  const coordinates = parseInput(input);
  const grid = squareGrid();

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid.length; x++) {
      const distanceToCoords = coordinates.map(coordinate => ({
        coordinate,
        distance: manhattanDistance([x, y], coordinate)
      }));

      distanceToCoords.sort((a, b) => a.distance - b.distance);

      if (distanceToCoords[0].distance !== distanceToCoords[1].distance) {
        // no tie
        const coordinate = distanceToCoords[0].coordinate;

        if (areas[coordinate]) {
          areas[coordinate] += 1;
        } else {
          areas[coordinate] = 1;
        }

        if (
          x === 0 ||
          y === 0 ||
          x === grid.length - 1 ||
          y === grid.length - 1
        ) {
          infiniteAreas[coordinate] = true;
        }
      }
    }
  }

  const largestFiniteArea = Object.entries(areas)
    .sort(([coord1, area1], [coord2, area2]) => area2 - area1)
    .filter(([coordinate, area]) => !infiniteAreas[coordinate])[0][1];
  return largestFiniteArea;
};

// console.log(part1());

// What is the size of the region containing all
// locations which have a total distance to all given
// coordinates of less than 10000?
const part2 = (input = fileInput, maxDistance = 10000) => {
  const coordinates = parseInput(input);
  const grid = squareGrid();

  let targetRegionArea = 0;

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid.length; x++) {
      const distanceToCoords = coordinates.map(coordinate =>
        manhattanDistance([x, y], coordinate)
      );

      const totalDistanceToCoords = distanceToCoords.reduce(
        (prev, current) => prev + current,
        0
      );

      if (totalDistanceToCoords < maxDistance) {
        targetRegionArea += 1;
      }
    }
  }

  return targetRegionArea;
};

// console.log(part2());

module.exports = { part1, part2 };
