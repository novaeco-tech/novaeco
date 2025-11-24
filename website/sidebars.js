// website/sidebars.js
module.exports = {
    tutorialSidebar: [
        'intro',
        {
            type: 'category',
            label: 'Architecture',
            items: [
                'architecture/overview',
                'architecture/adr-001-core-services',
                'architecture/adr-002-auth',
                'architecture/adr-003-api-gateway',
                'architecture/adr-004-docs-site',
                'architecture/adr-template',
            ],
        },
        {
            type: 'category',
            label: 'Requirements',
            items: [
                'requirements/functional',
                'requirements/non-functional',
                'requirements/sustainability',
            ],
        },
        {
            type: 'category',
            label: 'Use Cases',
            items: [
                'usecases/level-1-onboarding',
                'usecases/level-2-easy',
                'usecases/level-3-medium',
                'usecases/level-4-complex',
                'usecases/usecase-template',
            ],
        },
        {
            type: 'category',
            label: 'API',
            items: [
                'api/overview',
                'api/auth',
                'api/gateway',
                'api/examples',
                'api/testing',
            ],
        },
        {
            type: 'category',
            label: 'Developers',
            items: [
                'developers/quickstart',
                'developers/setup',
                'developers/cli',
                'developers/workflows',
                'developers/contribution',
            ],
        },
        {
            type: 'category',
            label: 'Guides',
            items: [
                'guides/dev-guide',
                'guides/best-practices',
                'guides/testing-guide',
                'guides/sustainability-guide',
                'guides/style-guide',
                'guides/guide-template',
            ],
        },
        'faq',
        'changelog',
        'glossary'
    ],
};
