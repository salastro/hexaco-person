"""Calculate 100 HEXACO-PI-R results."""
import argparse
import pandas as pd
from model import reversal, domains_questions

def reverse(reversal:list, answers: dict, shift: int):
    """TODO: Docstring for reverse.

    :reversal: TODO
    :answers: TODO
    :shift: maximum score + 1
    :returns: TODO

    """
    for i in reversal:
        answers[i] = shift-answers[i]
    return answers

def domains_scores(domains_questions: dict, answers: dict):
    """TODO: Docstring for domains_scores.

    :domains_questions: TODO
    :answers: TODO
    :returns: TODO

    """
    scores = {}
    for domain in domains_questions:
        single_domain_scores = [answers[i] for i in domains_questions[domain]]
        scores[domain] = sum(single_domain_scores)/len(single_domain_scores)
    return scores

def save_as_csv(unindexd_dictionary: dict, filename: str):
    """TODO: Docstring for save_as_csv.
    :unindexd_dictionary: TODO
    :filename: TODO
    :returns: TODO

    """
    df = pd.DataFrame(unindexd_dictionary, index= [0])
    df.to_csv(filename)

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    parser = argparse.ArgumentParser(
        prog = "python3 calculate-results.py",
        description = "Calculate 100 HEXACO-PI-R results.",
    )
    parser.add_argument("answers_file", help="file from which input answers")
    parser.add_argument("results_file", help='file to which output results')
    args = parser.parse_args()
    answers_file = args.answers_file
    results_file = args.results_file

    answers = pd.read_csv(
        answers_file,
        index_col=0,
    ).squeeze("rows").to_dict()
    answers = {int(k): v for k, v in answers.items()}
    answers = reverse(reversal, answers, 6)

    scores = domains_scores(domains_questions, answers)
    save_as_csv(scores,  results_file)

if __name__ == "__main__":
    main()
