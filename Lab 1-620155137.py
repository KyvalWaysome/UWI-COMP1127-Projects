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

    return char_complement(DNA[0])+string_complement(DNA[1:])#for loop could also have been used


def longest_gap(lst,ln):#find the maximum gap between two elements

  if lst==[] or len(lst)==1:

    return 0

  x=len(lst)-1 #subtract this to get the length before returning zer0 as the result 
#assings the variable x
  gaps=[lst[i+1]-lst[i] for i in range(0,x)]#iterate throughout the lst and find the largest gap
  #listcomprehensionwas used

  max_gap= max(gaps) #find the maximum 

  if max_gap < 1:

    return 0

  return max_gap-ln # calculates the difference between eacj number returns the largest value


def bindings(s,t):
  t=string_complement(t)#call the function and assign it to t

  num=len(t)-1 #claculates the length of t and stores it in the num

  combinations=[s[i:i+num+1] for i in range(0,len(s)-1)]

  gaps=[i for i in range(len(combinations)) if t==combinations[i]] #iterates through the combinations 

  if gaps==[]:
    return -1 #if theres no gap at all or no binding sites 

  if len(gaps)==1:
    return gaps[0]#return the index

  return longest_gap(gaps,len(t))
