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

## TODO

- Project cleanup
- find a better way to make internal requests
- wrapp requests on try/except
- Logging

## DONE

- Create dockerfile for the Flask app
- Create docker-compose using Redis
- request counter
- setup redis
- Finish test endpoint
- Generate random urls
- Generate random segments
- Create ADR file
- Setup pytest to run
- Create first endpoint
- Create makefile to run tasks
- Setup ruff as linter
- Create stats endpoint
- Create tests endpoint
- How to teste the Flask
  endpoints? https://flask.palletsprojects.com/en/2.3.x/testing/#sending-requests-with-the-test-client
- 
