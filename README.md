# WebApp UI test automation Playwright Python Pytest

## Table of Contents
1. [About](#about)
2. [Getting Started](#getting-started)
    - [Setup](#setup)
    - [Usage](#usage)
3. [Debugging Tests](#debugging-tests)
    - [For Linux](#for-linux)
    - [For Windows](#for-windows)
4. [Reports](#reports)
5. [CI/CD](#cicd)
    - [Setup](#setup-1)
    - [Run](#run)
    - [Reporting](#reporting)

## About
This repository contains the code of tests, written in Playwright framework (https://playwright.dev/python/). Main pattern used for this project is Page Object and Page Component model. We describe elements of pages, actions, which we use to interact with pages (*pages* folder). And describe test specs (*tests* folder) - things/flows we want to test and verify on our pages.

There are several main folders of these project:
- **pages**: contains classes, which describe what elements different pages have and how pages can behave
- **components**: contains components
- **page_factory**: contains elements
- **tests**: contains test specs

## Getting Started

### Setup

1. git clone https://github.com/TatyanaKonop/PythonPlaywrightSportUpdate.git
2. cd PythonPlaywrightSportUpdate
3. Create virtual environment
   `pip install virtualenv`
   `virtualenv venv`
   `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Install playwright. Run `playwright install`

### Usage

#### Running Tests

* General way to run all playwright tests to run `pytest` command. This command will run all existing test spec headless in browsers.

```
pytest
```

### Debugging tests

#### For Linux

* To debug all tests run `PWDEBUG=1 pytest -s` command. This command will open up a Browser window as well as
  the Playwright Inspector. You can use the step over button at the top of the inspector to step through your test.
  Or press the play button to run your test from start to finish. Once the test has finished the browser window will
  close.

```
PWDEBUG=1 pytest -s
```

* To debug one test run `PWDEBUG=1 pytest -s test_shopping_cart.py` followed by the name of the test file that you want
  to debug.

```
PWDEBUG=1 pytest -s test_shopping_cart.py
```

#### For Windows

* To debug tests on windows set env variable PWDEBUG using `$env:PWDEBUG="1"` command. Then run Pytest command to run
  tests.

```
$env:PWDEBUG="1"
```

```
pytest
```

* To set debug mode off, use `$env:PWDEBUG="0"`

```
$env:PWDEBUG="0"
```


### Reports

* To get HTML Report in `pytest.ini` file indicated `--html=${ROOT_DIR}/reports/pwreport3.html --capture=tee-sys` option. After running tests folder reports with *pwreport3.html* file will appear.
* To get Allure Report in `pytest.ini` file indicated `--alluredir=./allure-results ` option. After running tests *allure-results* folder will appear. After that run `allure serve` command.

## CI/CD

### Setup

* Workflow is described in  yml file in folder .github/workflows
* Setting -> Pages -> Source -> Deploy from a branch
* Setting -> Pages -> Branch -> gh-pages (created before)
* Setting -> Actions -> General -> Workflow permissions -> Read and write permissions

### Run

* To start CI/CD workflow in Actions -> Workflow -> <name workflow> -> run workflow

### Reporting

* To get HTML Report Actions -> All workflows -> click workflow -> Artifacts -> github-pages
* To get Allure Report Setting -> Pages -> Visit site
