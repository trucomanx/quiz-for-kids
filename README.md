# quiz-for-kids
math quiz for kids


## Requirements

pip install setuptools wheel twine


## Install from source

```bash
git clone https://github.com/trucomanx/quiz-for-kids
cd quiz-for-kids/src
python setup.py sdist
```

## Upload to pypi

```bash
cd quiz-for-kids/src
python setup.py sdist bdist_wheel
twine upload dist/*
```
