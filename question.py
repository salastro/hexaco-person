"""Take the 100 HEXACO-PI-R personality test."""
import argparse
import pandas as pd
from model import start_message, end_message, questions100, reversal, domains_questions

def ask(questions: dict):
    """TODO: Docstring for ask.

    :message: TODO
    :questions: TODO
    :returns: TODO

    """

    answers = {}
    i = 1
    while i <= len(questions):
        ans = input(f"{i}) {questions[i]} ")
        if ans == 'b' :
            if i != 1:
                i -= 2
            else:
                print('You are on the first item, cannot go back')
                continue
        else:
            try:
                ans = int(ans)
            except ValueError:
                print('Not an integer, cannot proceed')
                continue
            if not 1 <= ans <= 5:
                print('Number not in range (1-5), cannot proceed')
                continue
        answers[i] = ans
        i += 1

    return answers

def reverse(reversal: list, answers: dict):
    for i in reversal:
        answers[i] = 6-answers[i]
    return answers

def domains_scores(domains_questions: dict, answers: dict):
    scores = {}
    for domain in domains_questions:
        single_domain_scores = [answers[i] for i in domains_questions[domain]]
        scores[domain] = sum(single_domain_scores)/len(single_domain_scores)
    return scores

def save_as_csv(unindexd_dictionary: dict, filename: str):
    df = pd.DataFrame(unindexd_dictionary, index= [0])
    df.to_csv(filename)

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    parser = argparse.ArgumentParser(
        prog = 'python3 question.py',
        description = 'Take the 100 HEXACO-PI-R personality test.',
    )

    parser.add_argument('answers_file', help='file to which output answers')
    parser.add_argument('results_file', help='file to which output results')

    args = parser.parse_args()

    answers_file = args.answers_file
    results_file = args.results_file

    print(start_message)

    answers = ask(questions100)
    reversed_answers = reverse(reversal, answers)
    scores = domains_scores(domains_questions, reversed_answers)

    print(end_message)

    save_as_csv(answers, answers_file)
    save_as_csv(scores,  results_file)


if __name__ == "__main__":
    main()
