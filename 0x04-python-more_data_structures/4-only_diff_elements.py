#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff1 = set_1.difference(set_2)
    diff2 = set_2.difference(set_1)
    result = diff1.union(diff2)
    return result


set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
