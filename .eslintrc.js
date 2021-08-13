module.exports = {
  root: true,

  env: {
    node: true
  },

  'extends': [
    "plugin:vue/vue3-essential",
    "plugin:vue/vue3-strongly-recommended",
    "plugin:vue/strongly-recommended",
    "plugin:vue/vue3-recommended",
    'plugin:vue/essential',
    'eslint:recommended'
  ],

  parserOptions: {
    parser: 'babel-eslint'
  },

  rules: {
    "no-mixed-spaces-and-tabs": 0, // disable rule
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off'
  },

  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)'
      ],
      env: {
        jest: true
      }
    }
  ]
}
