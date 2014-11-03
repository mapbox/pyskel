Pyskel
======

A skeleton of a Python package with CLI and test suite included.

![](https://farm4.staticflickr.com/3951/15672691531_3037819613_o_d.png)

Quick start
-----------

To use pyskel as the start of a new project, do the following, preferably in
a virtual environment. Clone the repo.

```
git clone git@github.com:mapbox/pyskel.git myproject
cd myproject
```

Then replace all occurrences of 'pyskel' with the name of your own project.

```
find . -not -path './.git*' -type f -exec sed -i '' -e 's/pyskel/myproject/g' {} +
mv pyskel myproject
```

Then install in locally editable (`-e`) mode and run the tests.

```
pip install -e .[test]
py.test
```

To try the command line script.

```
myproject --help
myproject 4
```
