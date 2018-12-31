// /**
//  * Creates a list of digits in the number
//  *
//  * @param {number} num - Integer number
//  * @return {string} List of digits in the number
//  */
// const numToDigits = num => {
//   if (num == 0) {
//     return [0];
//   }

//   const digits = [];

//   while (num > 0) {
//     const digit = num % 10;
//     digits.unshift(digit);
//     num = (num - digit) / 10;
//   }

//   return digits;
// };

const EXTRA_RECIPES = 10;

const makeRecipes = (elves, scores) => {
  const elfCurrentRecipes = [];
  elves.forEach(currentRecipeIdx => {
    const elfCurrentRecipe = parseInt(scores[currentRecipeIdx]);
    elfCurrentRecipes.push(elfCurrentRecipe);
  });

  const elfCurrentRecipesSum = elfCurrentRecipes.reduce(
    (accumulator, num) => accumulator + num,
    0
  );

  scores.push(...elfCurrentRecipesSum.toString().split(''));

  for (let i = 0; i < elves.length; i++) {
    const currentRecipeIdx = elves[i];
    const currentRecipeScore = parseInt(scores[currentRecipeIdx]);
    const step = currentRecipeScore + 1;
    const nextCurrentRecipeIdx = (currentRecipeIdx + step) % scores.length;
    elves[i] = nextCurrentRecipeIdx;
  }

  return scores;
};

const part1 = numRecipes => {
  numRecipes = parseInt(numRecipes);

  let scores = [3, 7];
  const elves = [0, 1];

  let recipes = scores.length;
  while (recipes < numRecipes + EXTRA_RECIPES) {
    scores = makeRecipes(elves, scores);
    recipes = scores.length;
  }

  return scores.slice(numRecipes, numRecipes + EXTRA_RECIPES).join('');
};

const part2 = scoreSequence => {
  let scores = [3, 7];
  const elves = [0, 1];

  const recipesHasScore = (lastScoreSearchIdx = null) => {
    // There can be multiple recipes added in a step, so we'll search from every new recipe
    // Returns the index of the score sequence in case we find it (truthy!)
    if (lastScoreSearchIdx) {
      for (let i = scores.length; i > lastScoreSearchIdx; i -= 1) {
        if (
          scores.slice(i - scoreSequence.length, i).join('') === scoreSequence
        ) {
          return i - scoreSequence.length;
        }
      }
    }

    return false;
  };

  let lastScoreSearchIdx;
  while (!recipesHasScore(lastScoreSearchIdx)) {
    lastScoreSearchIdx = scores.length - 1;
    scores = makeRecipes(elves, scores);
    recipes = scores.length;
  }

  return recipesHasScore(lastScoreSearchIdx);
};

module.exports = {
  part1,
  part2
};

const INPUT = '681901';
// console.log(part1(INPUT));
// console.log(part2(INPUT));
