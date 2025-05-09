"""
 Complete the solution so that it splits the string into pairs of two characters.
 If the string contains an odd number of characters then it should replace the
 missing second character of the final pair with an underscore ('_').
"""
def solution(s):
    groups = []
    group = ''
    count = 0
    for i in s:
        group += i
        count += 1
        if count == 2:
            groups.append(group)
            group = ''
            count = 0
    if group: groups.append(group + '_')

    return groups

if __name__ == '__main__':
    print(solution("asdfadsf"))
    print(solution("asdfads"))