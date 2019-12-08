const assert = require('assert');
const parts = require('./1');

describe('given a mass', () => {
  it('should calculate the fuel required', () => {
    assert.strictEqual(parts.calculateFuelRequired(12), 2);
    assert.strictEqual(parts.calculateFuelRequired(14), 2);
    assert.strictEqual(parts.calculateFuelRequired(1969), 654);
    assert.strictEqual(parts.calculateFuelRequired(100756), 33583);
  });

  it('should find the sum of the fuel requirements', () => {
    assert.strictEqual(parts.part1(), 3154112);
  });

  it('should calculate the leftover fuel required correctly', () => {
    assert.strictEqual(parts.calculateLeftoverFuelRequired(14), 2);
    assert.strictEqual(parts.calculateLeftoverFuelRequired(1969), 966);
    assert.strictEqual(parts.calculateLeftoverFuelRequired(100756), 50346);
  });

  it('should find the sum of the fuel requirements', () => {
    assert.strictEqual(parts.part2(), 4728317);
  });
});
