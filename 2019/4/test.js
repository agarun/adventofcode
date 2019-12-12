const assert = require('assert');
const parts = require('./4');

describe('given numeric passwords', () => {
  it('isPasswordValid should validate that password meets the criteria', () => {
    assert.strictEqual(parts.isPasswordValid(111111), true);
    assert.strictEqual(parts.isPasswordValid(223450), false);
    assert.strictEqual(parts.isPasswordValid(123789), false);
  });

  it('should find how many passwords in the range meet the criteria', () => {
    assert.strictEqual(parts.part1(), 945);
  });

  it('isPasswordValid should show if passwords meet new criteria', () => {
    assert.strictEqual(parts.isPasswordValid(112233, { strict: true }), true);
    assert.strictEqual(parts.isPasswordValid(123444, { strict: true }), false);
    assert.strictEqual(parts.isPasswordValid(111122, { strict: true }), true);
    assert.strictEqual(parts.isPasswordValid(112222, { strict: true }), true);
  });

  it('should find how many passwords in the range meet the criteria', () => {
    assert.strictEqual(parts.part2(), 617);
  });
});
