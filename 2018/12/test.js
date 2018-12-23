const assert = require('assert');
const parts = require('./12');

describe('given a list of rules and starting pots', () => {
  it('should find how many potted plants there are after 20 generations', () => {
    assert.strictEqual(parts.part1(20), 3410);
  });

  it('should find how many potted plants there are after 50000000000 generations', () => {
    assert.strictEqual(parts.part2(50000000000), 4000000001480);
  });
});
