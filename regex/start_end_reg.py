"""
At HackerRank, we always want to find out how popular we are getting every day and have scraped conversations from popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:

Starts with hackerrank
Ends with hackerrank
Start and ends with hackerrank
Input Format

First line of the input contains an integer, N. Then N lines follow.
From the second line onwards, each line contains a set of W words separated by a single space

Constraints

1 <= N <= 10
1 <= W <= 100
All the characters in W are lowercase alphabet characters.
If C is the count of the characters in W, then 1 <= C <= 20
Output Format

For every line,

Print 1 if the conversation starts with hackerrank
Print 2 if the conversation ends with hackerrank
Print 0 if the conversation starts and ends with hackerrank
Print -1 if none of the above.
Sample Input

4
i love hackerrank
hackerrank is an awesome place for programmers
hackerrank
i think hackerrank is a great place to hangout
Sample Output

2
1
0
-1
Explanation

The first conversation ends with hackerrank and hence 2
The second conversation starts with hackerrank and hence 1
The third conversation has only one word, it starts and ends with hackerrank and hence 0.
The fourth conversation satisfies none of the above properties and hence -1.

"""

import re


def search(reg, input):
    size = len(input)
    output = -1
    for search in re.finditer(reg, input):
        if search.start() == 0:
            if search.end() == size:
                output = 0
            else:
                output = 1
        elif search.start() == size - len(reg):
            if output == 1:
                output = 0
            else:
                output = 2
    return output


def main():
    reg = r"hackerrank"
    N = int(raw_input())

    if N < 1 or N > 10:
        exit()

    for i in range(0, N):
        input = raw_input()
        output = search(reg, input)
        print(output)


def test_search():
    reg = "hackerrank"
    assert 1 == search(reg, "hackerrank is best")
    assert 2 == search(reg, "Its best to be in hackerrank")
    assert 0 == search(reg, "hackerrank, you are the best. hackerrank")
    assert -1 == search(reg, "Its not hacckerank")


if __name__ == "main":
    main()
