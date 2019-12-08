const path = require('path');
const fs = require('fs');
const file = path.join(__dirname, './input');
const fileInput = fs.readFileSync(file, { encoding: 'utf-8' }).split('\n');

function calculateFuelRequired(mass) {
  return Math.floor(mass / 3) - 2;
}

function getTotalFuelRequirement(masses) {
  return masses
    .map(calculateFuelRequired)
    .reduce((totalMass, currentMass) => totalMass + currentMass, 0);
}

function part1() {
  return getTotalFuelRequirement(fileInput);
}

function calculateLeftoverFuelRequired(massOrFuel) {
  const fuelRequired = calculateFuelRequired(massOrFuel);
  if (fuelRequired <= 0) {
    return 0;
  } else {
    return fuelRequired + calculateLeftoverFuelRequired(fuelRequired);
  }
}

function getTotalLeftoverFuelRequirement(masses) {
  return masses
    .map(calculateLeftoverFuelRequired)
    .reduce((totalMass, currentMass) => totalMass + currentMass, 0);
}

function part2() {
  return getTotalLeftoverFuelRequirement(fileInput);
}

module.exports = {
  calculateFuelRequired,
  calculateLeftoverFuelRequired,
  part1,
  part2
};
