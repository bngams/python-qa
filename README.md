# AGL

## Install python

Install python(>3.10) and pip (should be available as commands)

## Install requirements

Run pip install from root folder

```
pip install -r requirements.txt
```


## Linting

* Be sure .editorconfig is loaded
* Autopep as formatter
* Be sure specific custom rules in .pylintrc are loaded. Eg:

```
[STRING]

# This flag controls whether inconsistent-quotes generates a warning when the
# character used as a quote delimiter is used inconsistently within a module.
check-quote-consistency=yes

```
# Workflow

[Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) vs. [Trunk-based](https://trunkbaseddevelopment.com/)

# Testing

## Unit tests

Install pytest globally.

We used pytest instead [unittest](https://docs.python.org/3/library/unittest.html) because it's more simple and it matches our needs.

We use [auto-discovery](https://docs.pytest.org/en/7.3.x/explanation/goodpractices.html#test-discovery) from pytest to scan test files

```
pip install pytest
```
## Http integration Testing

TODO: With Flask Testing API or Postman, etc...

## E2E tests

/!\ nodejs required

We choose cypress, even if it's another tech/language because of its features (and very user friendly)

We use [cypress](https://learn.cypress.io/testing-your-first-application/installing-cypress-and-writing-your-first-test)

To install cypress from root folder (with package.json)
```
npm install
```

To install run tests
```
npx cypress run test
```

# MD Basic syntax

[Markdown syntax](https://www.markdownguide.org/basic-syntax/)

Some **bold** text.

Listing:
- list
- list