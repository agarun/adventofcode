const assert = require('assert');
const parts = require('./3');

const smallSample = `#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2`.split('\n');

describe('given a list of claims for fabric real estate', () => {
  it('should return how much fabric overlaps', () => {
    assert.strictEqual(parts.part1(smallSample), 4);
  });

  it('should find which claim has no overlaps', () => {
    assert.strictEqual(parts.part2(smallSample), 3);
  });
});
