module.exports = {
    "transform": {
        "^.+\\.tsx?$": "ts-jest"
    },
    "testRegex": "(/__tests__/.*|(\\.|/)(test|spec))\\.(jsx?|tsx?)$",
    "moduleFileExtensions": [
        "ts",
        "tsx",
        "js",
        "jsx",
        "json"
    ],
    "setupFiles": [
        "<rootDir>/test/setupTests.ts"
    ],
    "moduleNameMapper": {
        "\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$": "<rootDir>/test/fileMock.ts",
        "\\.(css|pcss|scss)$": "<rootDir>/test/styleMock.ts"
    },
    "collectCoverage": true,
    "collectCoverageFrom": [
        "**src/**/*.{ts,tsx}"
    ]
}
