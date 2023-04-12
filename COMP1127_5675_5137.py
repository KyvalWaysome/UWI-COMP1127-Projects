###################################################
###################################################
##  Group Information:                           ##
##                                               ##
##  Members:                                     ##
##                                               ##
##  Jordan Campbell - 620155675                  ##
##                                               ##
##  Kyval Waysome -  620155137                   ##
##                                               ##
###################################################
###################################################

import math
import os
import random
import re
import sys

#number 1

def makePacket(srcIP, dstIP, length, prt, sp, dp, sqn, pld): #Constructor - creates the packet that has a tag and the packet details
    return ("PK", srcIP, dstIP, [length, prt, [sp, dp], sqn, pld])
    
def getPacketSrc(pkt): #Selector -  collects the source IP address
    if isPacket(pkt):
        return pkt[1]
    else:
        raise TypeError('Object is not a Packet')

def getPacketDst(pkt): #Selector - collects the destination IP address
    if isPacket(pkt):
        return pkt[2]
    else:
        raise TypeError('Object is not a Packet')

def getPacketDetails(pkt): #Selector - collects te packet details
    if isPacket(pkt):
        return pkt[3]
    else:
        raise TypeError('Object is not a Packet')

def isPacket(pkt): #Predicate - checks if the object is a packet 
    return type(pkt) == tuple and len(pkt) == 4 and pkt[0] == 'PK' and type(pkt[3]) == list and len(pkt[3]) == 5 

def isEmptyPkt(pkt): #Predicate - checks if the object is an empty packet
    if isPacket(pkt):
        return pkt[3] == []
    else:
        raise TypeError('Object is not a Packet')

#number 2

def getLength(pkt):#Selector - collects the length of the packet in bytes
    
    if isPacket(pkt):
        return getPacketDetails(pkt)[0]

def getProtocol(pkt): #Selector - collects the protocol used
    
    if isPacket(pkt):
        return getPacketDetails(pkt)[1]

def getSrcPort(pkt): #Selector - collects the source port
    
    if isPacket(pkt):
        return getPacketDetails(pkt)[2][0]

def getDstPort(pkt): #Selector - collects the destination port
    
    if isPacket(pkt):
        return getPacketDetails(pkt)[2][1]

def getSqn(pkt): #Selector - collects the sequence number
    
    if isPacket(pkt):
        return getPacketDetails(pkt)[3]

def getPayloadSize(pkt): #Selector - collects the size of the payload in bytes
    
    if isPacket(pkt):
        return getPacketDetails(pkt)[4]


#Number 3
    

def flowAverage(pkt_list): #produces a list of packets that have above average payload sizes
    
    sum1 = 0
    len1 = 0    
    
    for packet in pkt_list:
        sum1 += getPayloadSize(packet) #adding sum of payload size of each packet
        
    len1 = len(pkt_list) #length of packet list

    
    avgcheck = sum1/len1 #average payload size of all the packets in the list

    lst = []
    
    for packet in pkt_list:
        if getPayloadSize(packet) > avgcheck:
            lst.append(packet)
    return lst
        

def suspPort(pkt): # Predicate - returns a boolean depending on if the source or destination port is more than 500
    
    return getSrcPort(pkt) > 500 or getDstPort(pkt) > 500


def suspProto(pkt): #Predicate - returns a boolean depending on if the packet is in protocolList
    
    return getProtocol(pkt) not in ProtocolList    

def ipBlacklist(pkt): #Predicate - returns a boolean depending on if the packet is in IpBlackList
    
    return getPacketSrc(pkt) in IpBlackList

#number 4
def calScore(pkt): #calculates the score for a particular pakcet depending on certain suspicion parameters
    
    
    p_lst = []
    
    for packet in packet_List: #from the given pack list, checks if it follows the defined packet structure and modifies it accordingly
        if isPacket(packet):
            p_lst.append(packet)
        else:
            p_lst.append(makePacket(packet[0],packet[1],packet[2],packet[3],packet[4],packet[5],packet[6],packet[7]))
            
    lstpayload = list(map(getPayloadSize, p_lst))  

        
    sum = 0
    
    for a in lstpayload:
        sum += a
    
    avg = sum/len(p_lst)
    
    
    print('this is pkt', pkt)
    
    
    count = 0
    
    if getPayloadSize(pkt) > avg:
        count += 3.56
    if suspProto(pkt):
        count += 2.74
    if suspPort(pkt):
        count += 1.45
    if ipBlacklist(pkt):
        count += 10.00
    
    return round(count,2)    
    
        
def makeScore(pkt_list): #Constructor - creates a score structure with a list of packets in its contents
    
    lst = []
    
    for packet in pkt_list:
        lst.append((packet, calScore(packet)))
    
    return ['SCORE', lst]


def addPacket(ScoreList, pkt): #Mutator - adds a packet to the score structure 
    if isScore(ScoreList):
        ScoreList[1].append((pkt, calScore(pkt)))
    else:
        raise TypeError('Object is not a Score')

def getSuspPkts(ScoreList): #Selector - collects the suspicious packets from the score structure
    
    lst = []

    for score in ScoreList[1]:
        if score[1] > 5.00:
            lst.append(score[0])
            
    return lst

def getRegulPkts(ScoreList): #Selector - collects the regular packets from the score structure
    
    
    lst = []
    
    for score in ScoreList[1]: 
        if score[0] not in getSuspPkts(ScoreList):
            lst.append(score[0])

    return lst
        
def isScore(ScoreList): #Predicate - checks if the object is a score
    return type(ScoreList) == list and ScoreList[0] == 'SCORE' and type(ScoreList[1]) == list
    
def isEmptyScore(ScoreList): #Predicate - checks if the object is an empty score
    if isScore(ScoreList):
        return ScoreList[1] == []
    else:
        raise TypeError('Object is not a Score')

#number 5
def makePacketQueue(): #Constructor - creates the packet queue structure
    return ("PQ", [])
  

def contentsQ(q): #Selector - collects the contents of the queue
    if isPacketQ(q):
        return q[1]
    else:
        raise TypeError('Object is not a queue')  

def frontPacketQ(q):#Selector - collects the front elements in the packet queue
    if isPacketQ(q):
        return q[0]
    else:
        raise TypeError('Object is not a queue')

def addToPacketQ(pkt,q): #Mutator - adds a packet to the packet queue
    if isPacketQ(q):
        contentsQ(q).insert(get_pos(pkt, contentsQ(q)) , pkt)
    else:
        raise TypeError('Object is not a queue')

def get_pos(pkt,lst): #returns a numerical position that produces a list of packets ordered from lowest to highest sequence number
    if lst == []:
        return 0
    elif getSqn(pkt) < getSqn(lst[0]):
        return 0 
    else:
        return 1 + get_pos(pkt,lst[1:])
            
def removeFromPacketQ(q):   #Mutator - removes a packet from the packet queue
    if isPacketQ(q):
        contentsQ(q).pop(0)               
    else:    
        raise TypeError('Object is not a queue')                  
    
def isPacketQ(q): #Predicate - checks if the object is a packet queue
       return type(q) == tuple and len(q) == 2 and q[0] == 'PQ' and type(q[1]) == list                 
  

def isEmptPacketQ(q): #Predicate - checks if the object is a empty packet queue
    return contentsQ(q) == []  

#number 6
  
def makePacketStack(): #Constructor - creates a packet stack
  return ('PS', [])

def contentsStack(stk): #Selector - collects the contents of the packet stack
    if isPKstack(stk):
        return stk[1]
    else:
        raise TypeError('Object is not a stack')
  
def topProjectStack(stk): #Selector - collects the element at the top of the packet stack
    if isPKstack(stk):    
        return contentsStack(stk)[-1]
    else:
        raise TypeError('Object is not a stack')
  

def pushProjectStack(pkt,stk): #Mutator - adds a packet to the packet stack
    if isPKstack(stk):    
        contentsStack(stk).append(pkt)
    else:
        raise TypeError('Object is not a stack')

def popPickupStack(stk): #Mutator - removes a pakcet from the packet stack
  if isPKstack(stk):
    contentsStack(stk).pop()
  else:  
    raise TypeError('Object is not a stack')
  

def isPKstack(stk): #Predicate - checks if the onject is a packet stack
    return type(stk) == tuple and stk[0] == 'PS' and type(stk[1]) == list
  

def isEmptyPKStack(stk): #Predicate - checks if the object is an empty stack
    return contentsStack(stk) == []

#number 7
def sortPackets(scoreList,stack,queue): #places a packet into either a stack or queue structure depending on its respective score
    
    for score in scoreList[1]:
        if score[1] > 5:
            pushProjectStack(score[0],stack)
        else:
            addToPacketQ(score[0], queue)

#number 8
          
def analysePackets(packet_List): #returns a queue than contains regular packets from a given list of packets 
    pkt_lst = []
    
    for packet in packet_List: #converts the packets in the given list into a list of packets that follow the pakcet ADT
        pkt_lst.append(makePacket(packet[0],packet[1],packet[2],packet[3],packet[4],packet[5],packet[6],packet[7]))
    
    
    scorelist = makeScore(pkt_lst) #create score ADT
    
    q = makePacketQueue() #create Queue ADT
    
    stk = makePacketStack() #create Stack ADT
    
    sortPackets(scorelist, stk, q) 
    
    
    return q


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    
    srcIP = str(first_multiple_input[0])
    dstIP = str(first_multiple_input[1])
    length = int(first_multiple_input[2])
    prt = str(first_multiple_input[3])
    sp = int(first_multiple_input[4])
    dp = int(first_multiple_input[5])
    sqn = int(first_multiple_input[6])
    pld = int(first_multiple_input[7])
    
    ProtocolList = ["HTTPS","SMTP","UDP","TCP","DHCP","IRC"]
    
    IpBlackList = []
    
    packet_List = [(srcIP, dstIP, length, prt, sp, dp, sqn, pld),
    ("111.202.230.44","62.82.29.190",31,"HTTP",80,20,1562436,338), 
    ("222.57.155.164","50.168.160.19",22,"UDP",790,5431,1662435,812), 
    ("333.230.18.207","213.217.236.184",56,"IMCP",501,5643,1762434,3138), 
    ("444.221.232.94","50.168.160.19",1003,"TCP",4657,4875,1962433,428), 
    ("555.221.232.94","50.168.160.19",236,"HTTP",7753,5724,2062432,48)]
    
    fptr.write('Forward Packets => ' + str(analysePackets(packet_List)) + '\n')
    
    fptr.close()
