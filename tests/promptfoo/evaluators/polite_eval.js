module.exports = function(output, context) {
  // A simple heuristic based evaluator to check for polite and empathetic tone
  const lowerOutput = output.toLowerCase();
  const politeWords = ['sorry', 'apologize', 'understand', 'please', 'help', 'policy', 'return', 'exchange'];
  let count = 0;
  for (const word of politeWords) {
    if (lowerOutput.includes(word)) {
      count++;
    }
  }
  
  if (count >= 1) {
    return {
      pass: true,
      score: 1.0,
      reason: `Maintained a polite/helpful tone (found ${count} related words).`
    };
  } else {
    // We expect store assistants to use some of the policy/polite words.
    return {
      pass: false,
      score: 0.0,
      reason: "Response lacked required empathetic or policy-related vocabulary."
    };
  }
};
