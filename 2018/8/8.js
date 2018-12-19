const fs = require('fs');

const fileInput = fs
  .readFileSync('./input', { encoding: 'utf-8' })
  .replace('\n', '')
  .split(/\s+/)
  .map(n => parseInt(n));

class Node {
  constructor() {
    this.children = [];
    this.metadataEntries = [];
  }

  addChild(child) {
    this.children.push(child);
  }

  addMetadataEntry(metadataEntry) {
    this.metadataEntries.push(metadataEntry);
  }
}

class Tree {
  constructor() {
    this.nodes = [];
  }

  get rootNode() {
    return this.nodes[0];
  }

  build(list, idx = 0, parentNode = null) {
    const header = [list[idx++], list[idx++]];
    const [numChildren, numMetadataEntries] = header;

    const node = new Node();
    this.nodes.push(node);
    if (parentNode) {
      parentNode.addChild(node);
    }

    for (let _ = 0; _ < numChildren; _ += 1) {
      idx = this.build(list, idx, node);
    }

    const cap = idx + numMetadataEntries;
    while (idx < cap) {
      const metadataEntry = list[idx];
      node.addMetadataEntry(metadataEntry);
      idx += 1;
    }

    return idx;
  }

  metadataEntriesSum(node) {
    let sum = 0;
    sum = node.metadataEntries.reduce((prev, current) => prev + current, sum);
    for (const childNode of node.children) {
      sum += this.metadataEntriesSum(childNode);
    }
    return sum;
  }

  // If a node does have child nodes,
  // the metadata entries become indexes which refer to those child nodes.
  // A metadata entry of 1 refers to the first child node.
  // A metadata entry of 0 does not refer to any child node.
  valueOf(node) {
    if (node.children.length === 0) {
      return this.metadataEntriesSum(node);
    }

    let value = 0;
    for (let i = 0; i < node.metadataEntries.length; i += 1) {
      const childNodeIdx = node.metadataEntries[i] - 1;
      const childNode = node.children[childNodeIdx];
      if (childNodeIdx >= 0 && childNode) {
        value += this.valueOf(childNode);
      }
    }

    return value;
  }
}

function part1(input = fileInput) {
  const tree = new Tree();
  tree.build(input);
  return tree.metadataEntriesSum(tree.rootNode);
}

function part2(input = fileInput) {
  const tree = new Tree();
  tree.build(input);
  return tree.valueOf(tree.rootNode);
}

console.log({ part1: part1(), part2: part2() });

module.exports = { part1, part2 };
