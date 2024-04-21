#!/usr/bin/node

const num = process.argv[2];

if (num === undefined) {
  console.log('No argument');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    console.log(process.argv[i]);
  }
}
