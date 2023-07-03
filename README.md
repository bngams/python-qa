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

## Git local hooks

Uncomment pre-commit hook and add this command:

```
pylint ...
```

# MD Basic syntax

[Markdown syntax](https://www.markdownguide.org/basic-syntax/)

Some **bold** text.

Listing:
- list
- list
