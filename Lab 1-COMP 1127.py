def char_complement(base):
    if base == 'A':
     return 'T'

    elif base == 'T':
     return 'A'

    elif base == 'C':
      return 'G'

    elif base == 'G':
     return 'C'

    else:
        return ''


def string_complement(DNA):
   if DNA =='':

    return ''

   else:

    return char_complement(DNA[0])+string_complement(DNA[1:])

def longest_gap(lst,ln):

  if lst==[] or len(lst)==1:

    return 0

  x=len(lst)-1

  gaps=[lst[i+1]-lst[i] for i in range(0,x)]

  max_gap=max(gaps)

  if max_gap < 1:

    return 0

  return max_gap-ln


def bindings(s,t):
  t=string_complement(t)

  num=len(t)-1

  combinations=[s[i:i+num+1] for i in range(0,len(s)-1)]

  gaps=[i for i in range(len(combinations)) if t==combinations[i]]

  if gaps==[]:
    return -1

  if len(gaps)==1:
    return gaps[0]

  return longest_gap(gaps,len(t))
