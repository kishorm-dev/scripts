const Linter = require("eslint").Linter;
const linter = new Linter();

const commonRules = {
  'no-eval': 'ERROR',
  'no-alert': 'ERROR',
  'no-debugger': 'ERROR',
  'no-unreachable': 'ERROR',
  'no-duplicate-imports': 'ERROR',
  'constructor-super': 'ERROR',
  'for-direction': 'ERROR',
  'no-class-assign': 'ERROR',
  'no-new-native-nonconstructor': 'ERROR',
  'valid-typeof': 'ERROR',
  'no-eq-null': 'ERROR',
  'no-var': 'ERROR',
  'require-await': 'ERROR',
  'no-unreachable-loop': 'ERROR',
  'no-redeclare': 'ERROR',
  'no-self-assign': 'ERROR',
  'no-setter-return': 'ERROR',
  'no-shadow-restricted-names': 'ERROR',
  'no-this-before-super': 'ERROR',
  'no-unsafe-finally': 'ERROR',
  'no-unsafe-optional-chaining': 'ERROR',
  'no-unused-vars': 'ERROR',
  'no-useless-catch': 'ERROR',
  'eqeqeq': 'WARN',
  'prefer-const': 'WARN',
  'require-yield': 'WARN',
  'no-global-assign': 'WARN',
  'no-caller': 'WARN',
  'no-process-env': 'WARN',
  'complexity': ['WARN', 'MAX_COMPLEXITY'],
  'max-nested-callbacks': ['WARN', 'MAX_NESTING'],
  'handle-callback-err': ['WARN', '^.*(e|E)rr'],
  'getter-return': 'WARN',
  'no-async-promise-executor': 'WARN',
  'no-case-declarations': 'WARN',
  'no-compare-neg-zero': 'WARN',
  'no-cond-assign': 'WARN',
  'no-const-assign': 'WARN',
  'no-constant-condition': 'WARN',
  'no-control-regex': 'WARN',
  'no-delete-var': 'WARN',
  'no-dupe-args': 'WARN',
  'no-dupe-class-members': 'WARN',
  'no-dupe-else-if': 'WARN',
  'no-dupe-keys': 'WARN',
  'no-duplicate-case': 'WARN',
  'no-empty': 'WARN',
  'no-empty-character-class': 'WARN',
  'no-empty-pattern': 'WARN',
  'no-ex-assign': 'WARN',
  'no-extra-boolean-cast': 'WARN',
  'no-extra-semi': 'WARN',
  'no-fallthrough': 'WARN',
  'no-func-assign': 'WARN',
  'no-import-assign': 'WARN',
  'no-inner-declarations': 'WARN',
  'no-invalid-regexp': 'WARN',
  'no-irregular-whitespace': 'WARN',
  'no-loss-of-precision': 'WARN',
  'no-misleading-character-class': 'WARN',
  'no-mixed-spaces-and-tabs': 'WARN',
  'no-nonoctal-decimal-escape': 'WARN',
  'no-obj-calls': 'WARN',
  'no-octal': 'WARN',
  'no-prototype-builtins': 'WARN',
  'no-regex-spaces': 'WARN',
  'no-sparse-arrays': 'WARN',
  'no-unexpected-multiline': 'WARN',
  'no-unsafe-negation': 'WARN',
  'no-unused-labels': 'WARN',
  'no-useless-backreference': 'WARN',
  'no-useless-escape': 'WARN',
  'no-with': 'WARN',
  'use-isnan': 'WARN',
};

(async function main() {
  try {
    // Initialize ESLint instance
    const eslint = new ESLint();

    // Retrieve all loaded rules
    const rulesMap = eslint.getRules();

    // Convert rules Map to an array if necessary
    const rulesArray = Array.from(rulesMap);

    // Filter and display rules from commonRules that have the "fixable" flag
    const fixableRules = [];
    for (const [ruleId, rule] of rulesArray) {
      if (ruleId in commonRules && rule.meta && rule.meta.fixable) {
        fixableRules.push({ ruleId, fixable: rule.meta.fixable });
      }
    }

    console.log("Fixable ESLint Rules from commonRules:");
    console.log(fixableRules);
  } catch (error) {
    console.error("Error fetching ESLint rules:", error);
  }
})();
