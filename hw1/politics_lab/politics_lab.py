voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    dic={}
    for line in voting_data:
        a=line.split()
        b=a[3:]
        name=a[0]
        vote=[int(x) for x in b]
        dic[name]=vote
    return dic



## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    return sum([x*y for (x,y) in zip(voting_dict[sen_a], voting_dict[sen_b])])



## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    a={}
    for x in voting_dict:
        a[x]=voting_dict[x]
    voting_dict.pop(sen, None)


    a={policy_compare(sen,x,a):x for x in voting_dict}
    b = dict(zip(a.values(),a.keys()))
    return max(b.keys(), key=(lambda key: b[key]))





## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    a={}
    for x in voting_dict:
        a[x]=voting_dict[x]
    voting_dict.pop(sen, None)


    a={policy_compare(sen,x,a):x for x in voting_dict}
    b = dict(zip(a.values(),a.keys()))
    return min(b.keys(), key=(lambda key: b[key]))
    
    


## Task 5




most_like_chafee    = most_similar('Chafee', create_voting_dict())
least_like_santorum = least_similar('Santorum', create_voting_dict())




# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    return ...

most_average_Democrat = ... # give the last name (or code that computes the last name)


# Task 7



def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    s=[]

    for i in range(len(sen_set[0])):
        s.append(sen_set[0][i])

    for x in sen_set:

        for i in range(len(sen_set)):
            s[i]+=x[i]
    #print(s)
    for i in range(len(sen_set)):
        s[i]-=sen_set[0][i]

    for i in range(len(sen_set)):
        s[i]/=len(sen_set[0])
    return s

dic={}
dic['D']=[]
dic['R']=[]
for line in voting_data:
    a=line.split()
    b=a[3:]
    name=a[1]

    vote=[int(x) for x in b]
    if name=='D':
        dic['D'].append(vote)
    else:
        dic['R'].append(vote)

        #return [sum(t) for t in zip(*[dic['D']])]

print(find_average_record(dic['D'], 'voting_dict'))

    #return ...
average_Democrat_record = [-0.15217391304347827, -0.21739130434782608, 0.9347826086956522, 0.782608695652174, 0.9130434782608695, -0.13043478260869565, -0.8913043478260869, 0.7608695652173914, 0.9130434782608695, 0.9130434782608695, 0.8478260869565217, 0.717391304347826, 0.6304347826086957, 0.9130434782608695, -0.4782608695652174, 0.8695652173913043, 0.8913043478260869, 0.9130434782608695, -0.3695652173913043, 0.9130434782608695, 0.9347826086956522, 0.9347826086956522, 0.9347826086956522, 0.8913043478260869, -0.45652173913043476, 0.9347826086956522, -0.30434782608695654, -0.06521739130434782, 0.9130434782608695, 0.8043478260869565, 0.9130434782608695, 0.9130434782608695, 0.9347826086956522, 0.9347826086956522, 0.9130434782608695, -0.32608695652173914, 0.9130434782608695, -0.45652173913043476, 0.21739130434782608, 0.8260869565217391, 0.41304347826086957, 0.8478260869565217, -0.8478260869565217, 1, 1, -1]

#average_Democrat_record = find_average_record('sen_set', 'voting_dict')
#print (average_Democrat_record)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    return (..., ...)

