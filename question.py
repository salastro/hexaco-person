import pandas as pd
from model import start_message, end_message, questions, reversal, domains_questions

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
    df.to_csv (rf"{filename}.csv")

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    print(start_message)
    answers = ask(questions)
    reversed_answers = reverse(reversal, answers)
    scores = domains_scores(domains_questions, reversed_answers)
    print(end_message)
    ans_filename = input("Answers file name: ")
    res_filename = input("Results file name: ")
    save_as_csv(answers, ans_filename)
    save_as_csv(scores, res_filename)

if __name__ == "__main__":
    main()
