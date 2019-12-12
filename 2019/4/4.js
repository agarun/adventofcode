function isPasswordValid(passwordInput, options = { strict: false }) {
  const password = passwordInput.toString();
  if (password.length > 6) {
    return false;
  }
  if (isNaN(password)) {
    return false;
  }

  const chains = {};

  for (let i = 1; i < password.length; i += 1) {
    prevDigit = password[i - 1];
    currentDigit = password[i];

    if (currentDigit < prevDigit) {
      return false;
    }

    if (currentDigit === prevDigit) {
      if (!chains[currentDigit]) {
        chains[currentDigit] = 1; // the chain started with the `prevDigit`
      }
      chains[currentDigit] += 1;
    }
  }

  for (const digit in chains) {
    if (options.strict && chains[digit] === 2) {
      return true;
    } else if (!options.strict && chains[digit] >= 2) {
      return true;
    }
  }
  return false;
}

function input() {
  const path = require('path');
  const fs = require('fs');
  const file = path.join(__dirname, './input');
  const fileInput = fs.readFileSync(file, { encoding: 'utf-8' }).split('\n');
  const range = fileInput[0].split('-').map(password => parseInt(password));
  return range;
}

const range = (min, max) =>
  Array.from({ length: max - min + 1 }, (curr, idx) => idx + min);

function partHelper(comparatorFn) {
  const [min, max] = input();
  const numbers = range(min, max);
  return numbers.filter(comparatorFn).length;
}

function part1() {
  return partHelper(isPasswordValid);
}

function part2() {
  return partHelper(pwd => isPasswordValid(pwd, { strict: true }));
}

module.exports = {
  isPasswordValid,
  part1,
  part2
};
