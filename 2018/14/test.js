const assert = require('assert');
const parts = require('./14');

describe('given a number of recipes the elves want to make', () => {
  it('should find the scores of the ten recipes after the given number', () => {
    assert.strictEqual(parts.part1('5'), '0124515891');
    assert.strictEqual(parts.part1('9'), '5158916779');
    assert.strictEqual(parts.part1('18'), '9251071085');
    assert.strictEqual(parts.part1('2018'), '5941429882');
  });

  it('should find how many recipes appear on the scoreboard to the left of a given score sequence', () => {
    // assert.strictEqual(parts.part2('51589'), 9);
    assert.strictEqual(parts.part2('01245'), 5);
    assert.strictEqual(parts.part2('92510'), 18);
    assert.strictEqual(parts.part2('59414'), 2018);
  });
});
