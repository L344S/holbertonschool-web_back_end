export default function hasValuesFromArray(set, array) {
  let flag = true;
  for (const set of array) {
    if (set.has(set) === false) {
      flag = false;
    }
  }
  return flag;
}
