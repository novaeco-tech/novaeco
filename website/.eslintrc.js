module.exports = {
    root: true,
    env: {
        browser: true, // For client-side React code
        node: true,    // For docusaurus.config.js and sidebars.js
        es6: true,
    },
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
        // 'plugin:react-hooks/recommended', // Optional: Uncomment if you add hooks later
    ],
    parserOptions: {
        ecmaFeatures: {
            jsx: true,
        },
        ecmaVersion: 2022, // Supports modern JS syntax used in Docusaurus
        sourceType: 'module',
    },
    settings: {
        react: {
            version: 'detect', // Automatically pick the React version from package.json
        },
    },
    rules: {
        // Docusaurus uses prop-types rarely (mostly content-driven), so we can relax this
        'react/prop-types': 'off',

        // Allow unescaped entities like ' (common in documentation text)
        'react/no-unescaped-entities': 'off',

        // Warn on unused variables (helps clean up code) but don't break build
        'no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
    },
    overrides: [
        {
            // Specific rules for config files which are pure Node.js
            files: ['*.js'],
            rules: {
                'no-var': 'error',
            },
        },
    ],
};