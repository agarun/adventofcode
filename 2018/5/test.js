const assert = require('assert');
const parts = require('./5');
const fs = require('fs');

const sample = fs
  .readFileSync('./input.sample', { encoding: 'utf-8' })
  .replace('\n', '');

describe('given a polymer', () => {
  it('should carry out reactions between adjacent monomers of opposite polarity', () => {
    assert.strictEqual(parts.part1(sample).length, 'dabCBAcaDA'.length);
  });

  it('should find which claim has no overlaps', () => {
    assert.strictEqual(parts.part2(sample), 4);
  });
});
