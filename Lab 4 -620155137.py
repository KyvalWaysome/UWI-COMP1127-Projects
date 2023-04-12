
def removePun(s):
  newstring = ''

  for a in s:
    if a not in (',','.','?','!',';',':'):
      newstring += a 
  return (newstring)



def encode(text):

    if text == "":

        return ""
    else:

        return chr((ord(text[0]))+5) + str(encode(text[1:]))
    
def decode(text):

    if text == "":

        return ""

    else:

        return chr((ord(text[0]))-5) + str(decode(text[1:]))


def stringList(str1):

     return str1.split()
    

def encodeM(lst):

 if lst == []:

    return []
 else:

    return [encode(lst[0])]+ encodeM(lst[1:]) 


def decodeM(lst):

 if lst == []:

    return []
 else:

    return [decode(lst[0])]+ decodeM(lst[1:]) 




def main(s):
 slst=removePun(s)
 eList = encodeM(stringList(slst))
 dList = decodeM(eList)
 print(f"Given string => {s}")
 print(f"Punctuation removed => {slst}")
 print(f"List Encoded => {eList}")
 print(f"List Decoded => {dList}")
 print ("Encoded Message =>",' '.join(eList))
