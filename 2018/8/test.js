const assert = require('assert');
const parts = require('./8');
const fs = require('fs');

const sample = fs
  .readFileSync('./input.sample', { encoding: 'utf-8' })
  .replace('\n', '')
  .split(/\s+/)
  .map(n => parseInt(n));

describe('given a list of coordinates', () => {
  it('finds the sum of all the metadata entries', () => {
    assert.strictEqual(parts.part1(sample), 138);
  });

  it('finds the value of the root node', () => {
    assert.strictEqual(parts.part2(sample), 66);
  });
});
