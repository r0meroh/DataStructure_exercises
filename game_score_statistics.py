"""
  This program takes in a list of scores from the user. Processes the scores in order to do the following:
    Get all the scores from user.
    Calculate the lowest score.
    Calculate the highest score.
    Calculate the average(mean).
    Calculate the standard Deviation.
"""

import statistics as stat


def user_scores():
    """
    take in scores from user and put them into a list
    """
    scores = []
    answer = int(input('enter scores, otherwise answer "-1" to end\n'))
    while (answer != -1):
        scores.append(answer)
        answer = int(input('enter next score\n'))
    return scores

def minimum (scores):
    mini = sorted(scores)
    return mini[0]


def highest(scores):
    mini = sorted(scores)
    return mini[-1]


def average(score):
    return stat.mean(score)

def deviation(scores):
    return stat.stdev(scores)




def main():
    scores = user_scores()
    print('the scores entered are \n')
    print(scores)
    print('lowest score was:\n')
    print(minimum(scores))
    print('highest score was:\n')
    print(highest(scores))
    print('average is:\n')
    print(average(scores))
    print('standard deviation is:\n')
    print(deviation(scores))


if __name__ == '__main__':
    main()