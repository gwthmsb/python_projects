#!/bin/python

"""
Every submission at HackerRank has a field called language which indicates the programming language which a hacker used
to code his solution.

C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:
PASCAL:SBCL:DART: GROOVY:OBJECTIVEC

Sometimes, error-prone API requests can have an invalid language field. Could you find out if a given submission has a
valid language field or not?

Input Format

First line contains N. N API requests follow, each in a newline. Each request has an integer api_id and a string
language which are the request parameters placed by the an API request.

"""
import re

languages_string = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:" \
                        + "ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"

languages = re.split(":", languages_string)


def validate_language(api):
    string_api_id, language = re.split("\s", api, 2)
    api_id = int(string_api_id)
    if (api_id < pow(10, 4) or api_id >= pow(10, 5)):
        return "INVALID"
    else:
        if language in languages:
            return "VALID"
        else:
            return "INVALID"


def main():

    n = int(raw_input())

    if n<=0 or n>100:
        exit()

    for i in range(0, n):
        api = raw_input()
        validity = validate_language(api)
        print(validity)


if __name__ == "__main__":
    main()


def test_validate_language():
    assert "VALID" == validate_language("11011 LUA")
    assert "VALID" == validate_language("11022 BRAINFUCK")
    assert "INVALID" == validate_language("11044 X")
