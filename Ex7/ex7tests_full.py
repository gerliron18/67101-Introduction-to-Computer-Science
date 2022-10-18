from autotest import TestSet

import sys

import testrunners

def unorderedlists(exp,ans):
    return sorted(exp) == sorted(ans)

def rounded(exp,ans):
    return round(exp,2) == round(ans,2)

def unorderedprints(exp,ans):
    if type(ans) is not str:
        return False
    if len(ans)==0 or ans[-1] != "\n":
        return False
    exp_list = exp[:-1].split('\n')
    ans_list = ans[:-1].split('\n')
    return unorderedlists(exp_list,ans_list)

defaults = {'modulename':'ex7',}

class Hanoi(object):
    def __init__(self, x):
        self.state=[list(range(x)[::-1]),[],[]]

    def move(self, src, dest):
        if not self.state[src]:
            raise Exception("Empty src")
        if self.state[dest] and self.state[src][-1] > self.state[dest][-1]:
            raise Exception("Illegal move")
        print(src,dest)
        self.state[dest].append(self.state[src].pop())

cases = [{'print_to_n_0':{'fname':'print_to_n',
                       'runner':testrunners.print_runner,
                       'args':[0],
                       'ans':[''],
                   },

         'print_to_n_1':{'fname':'print_to_n',
                       'runner':testrunners.print_runner,
                       'args':[1],
                       'ans':['1\n'],
                   },

         'print_to_n_2':{'fname':'print_to_n',
                       'runner':testrunners.print_runner,
                       'args':[2],
                       'ans':['1\n2\n'],
                   },
         'print_to_n_9':{'fname':'print_to_n',
                       'runner':testrunners.print_runner,
                       'args':[9],
                       'ans':['1\n2\n3\n4\n5\n6\n7\n8\n9\n'],
                   },
          },
         {'print_to_n_neg':{'fname':'print_to_n',
                       'runner':testrunners.print_runner,
                       'args':[-1],
                       'ans':[''],
                   },

         'print_reversed_n_0':{'fname':'print_reversed',
                       'runner':testrunners.print_runner,
                       'args':[0],
                       'ans':[''],
                   },

         'print_reversed_n_1':{'fname':'print_reversed',
                       'runner':testrunners.print_runner,
                       'args':[1],
                       'ans':['1\n'],
                   },

         'print_reversed_n_2':{'fname':'print_reversed',
                       'runner':testrunners.print_runner,
                       'args':[2],
                       'ans':['2\n1\n'],
                   },
         'print_reversed_n_9':{'fname':'print_reversed',
                       'runner':testrunners.print_runner,
                       'args':[9],
                       'ans':['9\n8\n7\n6\n5\n4\n3\n2\n1\n'],
                   },
         'print_reversed_n_neg':{'fname':'print_reversed',
                       'runner':testrunners.print_runner,
                       'args':[-1],
                       'ans':[''],
                   },
          },
         {'is_prime_2':{'fname':'is_prime',
                       'args':[2],
                       'ans':[True],
                   },

         'is_prime_4':{'fname':'is_prime',
                       'args':[4],
                       'ans':[False],
                   },

         'is_prime_5':{'fname':'is_prime',
                       'args':[5],
                       'ans':[True],
                   },

         'is_prime_neg':{'fname':'is_prime',
                       'args':[-5],
                       'ans':[False],
                   },

         'is_prime_0':{'fname':'is_prime',
                       'args':[0],
                       'ans':[False],
                   },
          
         'is_prime_1':{'fname':'is_prime',
                       'args':[1],
                       'ans':[False],
                   },
         'is_prime_11':{'fname':'is_prime',
                       'args':[11],
                       'ans':[True],
                   },
         'is_prime_31':{'fname':'is_prime',
                       'args':[31],
                       'ans':[True],
                   },
          },
         {'divisors_6':{'fname':'divisors',
                       'args':[6],
                       'ans':[[1,2,3,6]],
                   },

         'divisors_4':{'fname':'divisors',
                       'args':[4],
                       'ans':[[1,2,4]],
                   },

         'divisors_3':{'fname':'divisors',
                       'args':[3],
                       'ans':[[1,3]],
                   },

         'divisors_1':{'fname':'divisors',
                       'args':[1],
                       'ans':[[1]],
                   },

         'divisors_0':{'fname':'divisors',
                       'args':[0],
                       'ans':[[]],
                   },

         'divisors_neg':{'fname':'divisors',
                       'args':[-6],
                       'ans':[[1,2,3,6]],
                   },
         'divisors_30':{'fname':'divisors',
                       'args':[30],
                       'ans':[[1,2,3,5,6,10,15,30]],
                   },

         'divisors_24':{'fname':'divisors',
                       'args':[24],
                       'ans':[[1,2,3,4,6,8,12,24]],
                   },

          },
         {'exp_n_x_0_1':{'fname':'exp_n_x',
                       'args':[0,1],
                       'ans':[1],
                       'comparemethod':rounded,
                   },

         'exp_n_x_5_1':{'fname':'exp_n_x',
                       'args':[5,1],
                       'ans':[2.72],
                       'comparemethod':rounded,
                   },
         'exp_n_x_5_0':{'fname':'exp_n_x',
                       'args':[5,0],
                       'ans':[1],
                       'comparemethod':rounded,
                   },

         'exp_n_x_8_2':{'fname':'exp_n_x',
                       'args':[8,2],
                       'ans':[7.39],
                       'comparemethod':rounded,
                   },

         'exp_n_x_10_n1':{'fname':'exp_n_x',
                       'args':[10,-1],
                       'ans':[0.37],
                       'comparemethod':rounded,
                   },
          },
         {'hanoi_0':{'fname':'play_hanoi',
                    'runner':testrunners.print_runner,
                    'options':{'check_input':False},
                    'args':[Hanoi(0),0,0,1,2],
                    'ans':[''],
                    },

         'hanoi_1':{'fname':'play_hanoi',
                    'runner':testrunners.print_runner,
                    'options':{'check_input':False},
                    'args':[Hanoi(1),1,0,1,2],
                    'ans':['0 1\n'],
                    },

         'hanoi_2':{'fname':'play_hanoi',
                    'runner':testrunners.print_runner,
                    'options':{'check_input':False},
                    'args':[Hanoi(2),2,0,1,2],
                    'ans':['0 2\n0 1\n2 1\n'],
                    },
          },
         {'print_binary_sequences_0':{'fname':'print_binary_sequences',
                       'runner':testrunners.print_runner,
                       'args':[0],
                       'ans':['\n'],
                   },

         'print_binary_sequences_1':{'fname':'print_binary_sequences',
                       'runner':testrunners.print_runner,
                       'args':[1],
                       'ans':['0\n1\n'],
                       'comparemethod':unorderedprints,
                   },

         'print_binary_sequences_2':{'fname':'print_binary_sequences',
                       'runner':testrunners.print_runner,
                       'args':[2],
                       'ans':['00\n01\n10\n11\n'],
                       'comparemethod':unorderedprints,
                   },
          },
         {'print_sequences_ab_0':{'fname':'print_sequences',
                       'runner':testrunners.print_runner,
                       'args':[['a','b'],0],
                       'ans':['\n'],
                   },

         'print_sequences_ab_1':{'fname':'print_sequences',
                       'runner':testrunners.print_runner,
                       'args':[['a','b'],1],
                       'ans':['a\nb\n'],
                       'comparemethod':unorderedprints,
                   },

         'print_sequences_ab_2':{'fname':'print_sequences',
                       'runner':testrunners.print_runner,
                       'args':[['a','b'],2],
                       'ans':['aa\nab\nba\nbb\n'],
                       'comparemethod':unorderedprints,
                   },
          },
         {'print_no_repetition_sequences_ab_0':{'fname':'print_no_repetition_sequences',
                       'runner':testrunners.print_runner,
                       'args':[['a','b'],0],
                       'ans':['\n'],
                   },
          
         'print_no_repetition_sequences_ab_1':{'fname':'print_no_repetition_sequences',
                       'runner':testrunners.print_runner,
                       'args':[['a','b'],1],
                       'ans':['a\nb\n'],
                       'comparemethod':unorderedprints,
                   },

         'print_no_repetition_sequences_ab_2':{'fname':'print_no_repetition_sequences',
                       'runner':testrunners.print_runner,
                       'args':[['a','b'],2],
                       'ans':['ab\nba\n'],
                       'comparemethod':unorderedprints,
                   },
          },
         {'no_repetition_sequences_list_ab_0':{'fname':'no_repetition_sequences_list',
                       'args':[['a','b'],0],
                       'ans':[['']],
                       'comparemethod':unorderedlists,
                   },

         'no_repetition_sequences_list_ab_1':{'fname':'no_repetition_sequences_list',
                       'args':[['a','b'],1],
                       'ans':[['a','b']],
                       'comparemethod':unorderedlists,
                   },

         'no_repetition_sequences_list_ab_2':{'fname':'no_repetition_sequences_list',
                       'args':[['a','b'],2],
                       'ans':[['ab','ba']],
                       'comparemethod':unorderedlists,
                   },
        
          }
         ]

tsets = {t:TestSet({},c)
         for t,c in zip(['printton',
                         'printrev',
                         'isprime',
                         'divisors',
                         'expnx',
                         'hanoi',
                         'binseq',
                         'printseq',
                         'printnorep',
                         'listnorep',
                         ]
                        ,cases)}
