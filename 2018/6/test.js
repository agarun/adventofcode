const assert = require('assert');
const parts = require('./6');
const fs = require('fs');

const sample = fs
  .readFileSync('./input.sample', { encoding: 'utf-8' })
  .split('\n')
  .slice(0, -1);

describe('given a list of coordinates', () => {
  it("finds the size of the largest area that isn't infinite", () => {
    assert.strictEqual(parts.part1(sample), 17);
  });

  it('finds the size of the region with total distance to coords < max distance 32', () => {
    assert.strictEqual(parts.part2(sample, 32), 16);
  });
});
