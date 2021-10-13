<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Sudoblark](https://circleci.com/gh/Sudoblark/w3c-html-python-validator.svg?style=shield)](https://app.circleci.com/pipelines/github/Sudoblark/w3c-html-python-validator)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Sudoblark/w3c-html-python-validator">
    <img src="images/Idle_02.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">W3C HTML Python Validator</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project aims to build a Python HTML Validator that utilises the [W3C HTML validator API](https://github.com/validator/validator/wiki/Service-%C2%BB-Input-%C2%BB-POST-body).

The main motivation behind this for me is that as part of my Open University [Degree](https://www.open.ac.uk/courses/computing-it/degrees/bsc-computing-it-software-q62-soft) one of my [modules](https://www.open.ac.uk/courses/qualifications/details/tt284?orig=q62-soft&setAcc=true) focused about web technologies. Part of the practical activities for which were to manually valid HTML using [W3C's manual validator](https://validator.w3.org/).

As an experienced DevOps Engineer this seemed horribly inefficient to me, so I decided to make this little piece of code so I could build a CI on my (_private_) module repo to do the HTML validation for me :)

Some caveats:
- Sending your raw HTML over the web isn't great, but downloading the validator locally seemed overkill as a nice addon to my Uni work
- Error formatting could be nicer but as a mainly personal project it's good enough for me

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [pathlib](https://docs.python.org/3/library/pathlib.html)
* [PyTest](https://docs.pytest.org/en/6.2.x/)
* [urllib](https://docs.python.org/3/library/urllib.html)
* [json](https://docs.python.org/3/library/json.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* Python 3.9.7
* python3-virtualenv if running Linux

### Installation
* Clone repo

  ```sh
  git clone https://github.com/Sudoblark/w3c-html-python-validator
  ```

* Setup venv
    * Windows

      ```sh
      python3 -m venv venv
      .\venv\Scripts\activate
      ```
    * MacOS
    
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
      
    * Linux (tested on Ubuntu 20.04 LTS)
        ```sh
        virtualenv venv
        source venv/bin/activate
        ```
      
* Install requirements when in venv

  ```sh
  pip install -r requirements.txt
  ```

<!-- USAGE EXAMPLES -->
## Usage

* Local windows 10 machine

```sh
.\venv\Scripts\activate
python3 .\src\main.py .\tests\test_files\
  
('{"../tests/test_files/indent_0/valid.html": {"result": "HTML validate"}, '
'"../tests/test_files/indent_0/indent_1/invalid.html": {"result": "Invalid '
'HTML, one or more errors reported", "errors": [{"type": "error", "line": 12, '
'"column": 7, "message": "End of file seen when expecting text or an end '
'tag.", "extract": "dy>\\n</html>"}, {"type": "error", "line": 7, "column": '
'9, "message": "Unclosed element \\u201ctitle\\u201d.", "extract": " '
'Name\\">\\n  <title>HTML5 "}]}}')
One of more HTML files failed validation
```
  
* Local MacOS / Local Linux (tested on Ubuntu 20.04 LTS)

```sh
source venv/bin/activate
python3 src/main.py tests/test_files  

('{"../tests/test_files/indent_0/valid.html": {"result": "HTML validate"}, '
'"../tests/test_files/indent_0/indent_1/invalid.html": {"result": "Invalid '
'HTML, one or more errors reported", "errors": [{"type": "error", "line": 12, '
'"column": 7, "message": "End of file seen when expecting text or an end '
'tag.", "extract": "dy>\\n</html>"}, {"type": "error", "line": 7, "column": '
'9, "message": "Unclosed element \\u201ctitle\\u201d.", "extract": " '
'Name\\">\\n  <title>HTML5 "}]}}')
One of more HTML files failed validation
```
    
* CircleCI

See below for CircleCI yaml that will validate all HTML files in a repo:

```yaml
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/python:3.9.4
    steps:
      - checkout
      - run:
          name: Clone w3c-html-python-validator
          command: git clone https://github.com/Sudoblark/w3c-html-python-validator.git ~/w3c-html-python-validator
      - run:
          name: Install Python test dependencies
          command: sudo /home/circleci/.pyenv/shims/pip3.9 install -r ~/w3c-html-python-validator/requirements.txt
      - run:
          # Note clones of parent repo are in ~/project
          name: Run w3c-html-python-validator against local repo
          command: sudo /home/circleci/.pyenv/shims/python3.9 ~/w3c-html-python-validator/src/main.py "/home/circleci/project"
```


<!-- ROADMAP -->
## Roadmap

- [ ] Add CSS validation as well (requires repo rename)
- [ ] Make a pretty `setup.py` and setup CI to publish to PyPI
- [x] Add badges

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Benjamin Clark - [LinkedIn](https://www.linkedin.com/in/benni/) - bclark@sudoblark.com

Project Link: [W3C HTML Python Validator](https://github.com/Sudoblark/w3c-html-python-validator)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>

