# Rate limit challenge

# Architectural Decision Record

1. I'm assuming that the sentence "/api/xyz/abc/ghi/ (Invalid: 4 different random strings were used for path segments in
   this test run)" is wrong because the example doesn't make sentence with the explanation. So I will just assume that I
   can't have random_urls with 4 different segments, 3 is the maximum
2. I'm assuming there will be a CI in place to run the tests and keep the application covered by tests on the most
   important scenarios

# Decisions

- Keep the solution as simples as possible.
- I let the test organized by Arrange, Act and Assert on tests to show how I structure my tests.
- Explicit is better than implicit.
- I'm using Black for code formatting.
- I'm using Ruff for lint.
- I'm using Poetry for dependency and virtual environment management
- Python 3.11.3 is being used for this code, the latest available at the moment.

# Folder structure

```
.
├── Dockerfile
├── Makefile
├── README.md
├── challenge.md
├── docker-compose.yml
├── htmlcov
│   ├── coverage_html.js
│   ├── d_145eef247bfb46b6_main_py.html
│   ├── favicon_32.png
│   ├── index.html
│   ├── keybd_closed.png
│   ├── keybd_open.png
│   ├── status.json
│   └── style.css
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── src
│   ├── __pycache__
│   └── main.py
└── tests
    ├── __pycache__
    └── test_main.py

6 directories, 19 files
```

# Requirements

- Docker
- Python ^3.11.3
- Make
- Poetry

# Commands

## Setup

To set up just run `make setup` or `make s` for a shortcut

output

```bash
❯ make s
./setup.sh
Creating virtualenv close-code-challenge-i9dRl-ji-py3.11 in /Users/felipython/Library/Caches/pypoetry/virtualenvs
Installing dependencies from lock file

Package operations: 22 installs, 0 updates, 0 removals

  • Installing iniconfig (2.0.0)
  • Installing packaging (23.1)
  • Installing pluggy (1.0.0)
  • Installing coverage (7.2.5)
  • Installing pytest (7.3.1)
  • Installing markupsafe (2.1.2)
  • Installing pytest-cov (4.0.0)
  • Installing blinker (1.6.2)
  • Installing click (8.1.3)
  • Installing itsdangerous (2.1.2)
  • Installing jinja2 (3.1.2)
  • Installing mypy-extensions (1.0.0)
  • Installing pathspec (0.11.1)
  • Installing platformdirs (3.5.0)
  • Installing pytest-cover (3.0.0)
  • Installing ruff (0.0.265)
  • Installing werkzeug (2.3.3)
  • Installing black (23.3.0)
  • Installing flask (2.3.2)
  • Installing pytest-coverage (0.0)
  • Installing pytest-ruff (0.0.6)
  • Installing redis (4.5.4)

/Users/felipython/dev/python/code-challenges/close-code-challenge/close_code_challenge does not contain any element
================================================================================================================================== test session starts ===================================================================================================================================
platform darwin -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0 -- /Users/felipython/Library/Caches/pypoetry/virtualenvs/close-code-challenge-i9dRl-ji-py3.11/bin/python
cachedir: .pytest_cache
rootdir: /Users/felipython/dev/python/code-challenges/close-code-challenge
configfile: pytest.ini
testpaths: tests
plugins: ruff-0.0.6, cov-4.0.0
collected 7 items

tests/test_main.py::test_root PASSED                                                                                                                                                                                                                                               [ 14%]
tests/test_main.py::test_api_endpoint PASSED                                                                                                                                                                                                                                       [ 28%]
tests/test_main.py::test_stats_endpoint PASSED                                                                                                                                                                                                                                     [ 42%]
tests/test_main.py::test_test_endpoint PASSED                                                                                                                                                                                                                                      [ 57%]
tests/test_main.py::test_random_segment_generator PASSED                                                                                                                                                                                                                           [ 71%]
tests/test_main.py::test_create_one_random_url PASSED                                                                                                                                                                                                                              [ 85%]
tests/test_main.py::test_generate_random_urls PASSED                                                                                                                                                                                                                               [100%]

================================================================================================================================== slowest 5 durations ===================================================================================================================================
0.00s call     tests/test_main.py::test_root
0.00s call     tests/test_main.py::test_stats_endpoint
0.00s call     tests/test_main.py::test_test_endpoint
0.00s call     tests/test_main.py::test_api_endpoint
0.00s setup    tests/test_main.py::test_root
=================================================================================================================================== 7 passed in 0.59s ====================================================================================================================================
Spawning shell within /Users/felipython/Library/Caches/pypoetry/virtualenvs/close-code-challenge-i9dRl-ji-py3.11
. /Users/felipython/Library/Caches/pypoetry/virtualenvs/close-code-challenge-i9dRl-ji-py3.11/bin/activate

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bash-3.2$ . /Users/felipython/Library/Caches/pypoetry/virtualenvs/close-code-challenge-i9dRl-ji-py3.11/bin/activate
(close-code-challenge-py3.11) bash-3.2$ exit
exit
```

## Test

To set up just run `make test` or `make t` for a shortcut

output

```bash
❯ make t
pytest
================================================================================================================================== test session starts ===================================================================================================================================
platform darwin -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0 -- /Users/felipython/Library/Caches/pypoetry/virtualenvs/close-code-challenge-i9dRl-ji-py3.11/bin/python
cachedir: .pytest_cache
rootdir: /Users/felipython/dev/python/code-challenges/close-code-challenge
configfile: pytest.ini
testpaths: tests
plugins: ruff-0.0.6, cov-4.0.0
collected 7 items

tests/test_main.py::test_root PASSED                                                                                                                                                                                                                                               [ 14%]
tests/test_main.py::test_api_endpoint PASSED                                                                                                                                                                                                                                       [ 28%]
tests/test_main.py::test_stats_endpoint PASSED                                                                                                                                                                                                                                     [ 42%]
tests/test_main.py::test_test_endpoint PASSED                                                                                                                                                                                                                                      [ 57%]
tests/test_main.py::test_random_segment_generator PASSED                                                                                                                                                                                                                           [ 71%]
tests/test_main.py::test_create_one_random_url PASSED                                                                                                                                                                                                                              [ 85%]
tests/test_main.py::test_generate_random_urls PASSED                                                                                                                                                                                                                               [100%]

================================================================================================================================== slowest 5 durations ===================================================================================================================================
0.00s call     tests/test_main.py::test_root
0.00s call     tests/test_main.py::test_stats_endpoint
0.00s call     tests/test_main.py::test_test_endpoint
0.00s call     tests/test_main.py::test_api_endpoint
0.00s setup    tests/test_main.py::test_root
=================================================================================================================================== 7 passed in 0.09s ====================================================================================================================================
```

## Lint

To set up just run `make lint` or `make l` for a shortcut

output

```bash
❯ make l
ruff check --fix .
black .
All done! ✨ 🍰 ✨
2 files left unchanged.
```

## Run

To set up just run `make run` or `make r` for a shortcut

output

```bash
❯ make r
flask --app src.main run --debug -h 0.0.0.0
 * Serving Flask app 'src.main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.86.69:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 137-936-594
```

# Tasks

## TODO

1. find a better way to make internal requests
2. wrapp requests on try/except
3. Logging

## DONE

1. Project cleanup
2. Create dockerfile for the Flask app
3. Create docker-compose using Redis
4. request counter
5. setup redis
6. Finish test endpoint
7. Generate random urls
8. Generate random segments
9. Create ADR file
10. Setup pytest to run
11. Create first endpoint
12. Create makefile to run tasks
13. Setup ruff as linter
14. Create stats endpoint
15. Create tests endpoint
16. How to test the Flask
    endpoints? https://flask.palletsprojects.com/en/2.3.x/testing/#sending-requests-with-the-test-client
