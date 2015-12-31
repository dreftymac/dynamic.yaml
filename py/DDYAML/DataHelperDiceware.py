# -*- coding: utf-8 -*-
'''
### <beg-file_info>
### main:
###   - date: created="Tue Nov 24 09:21:41 2015"
###     last: lastmod="Tue Nov 24 09:21:41 2015"
###     tags: tags 
###     dreftymacid: "foxing_client_totemic"
###     seealso: |
###         *
###     desc: |
###         generate hard-to-remember diceword ngrams
###         for use as unique identifiers instead of passphrases
### <end-file_info>
'''

### --------------------------------------
### begin_: init python
if(True):
    import datetime
    import itertools
    import os
    import random
    import random
    import re
    import string
    import sys
    import sys    

### --------------------------------------
### begin_: 
if('python_region'):
  class DataHelperDiceware(object):
    
    ### --------------------------------------
    ### begin_: __init__ function
    def __init__(self):
        self.basename   = 'DataHelperDiceware'
        self.wordlist   = []
    ## end_def
    
    ### --------------------------------------
    ### begin_: class methods
    def listshuffle(self, ls):
        """
        functional programming version of random.shuffle
        """
        random.shuffle(ls)
        return ls
    ##enddef
    
    def wordnumberize(self, sgword=''):
        """
        randomly inject a number into a string
        """
        vout = sgword      
        ls   = list(sgword)
        ## ls.insert(random.randrange(len(ls)+1), "%03d"%(random.randint(0,999))) ##;; position_random        
        ls.insert((len(ls)+1), "%03d"%(random.randint(0,999))) ##;; position_ending
        vout = "".join( ls )
        return vout
    ##enddef
      
    def wordscramble(self, sgword=''):
        """
        randomly scramble characters in a string
        """
        vout = sgword      
        ls   = list(sgword)
        random.shuffle(ls)
        vout = "".join( ls )
        return vout
    ##enddef
  
    def get_wordlist(self):
        """
        generate diceword wordlist using internal python docs,
        instead of an external diceware wordlist of 7777 words
        
        if self.wordlist already is populated, use that;
        otherwise generate one from scratch.
        """
        
        ## init
        if( self.wordlist == None ):
          pass
        elif( self.wordlist.__len__() >  0):
          vout = self.wordlist
        elif( self.wordlist.__len__() == 0):
          vout      =   []
        ##;;
        
        ## process
        if(vout.__len__() == 0):
          aawords   =   []        
          ## extract
          for objj in [datetime,itertools,os,random,re,string,sys,]:
            aawords.extend(
              re.findall('[a-zA-Z0-9]+',str(getattr(objj,vxx).__doc__))
                for vxx in dir(objj)
                if(re.findall('^[a-z]',vxx))
            )
          aawords = list(itertools.chain(*aawords))
          aawords = [vxx.replace('_','') for vxx in aawords]
          ##;;
          
          ## transform
          aawords = [vxx for vxx in aawords if(vxx)]        ##;; remove_empty
          aawords = [str(vxx) for vxx in aawords if(vxx)]   ##;; stringify   
          aawords = [vxx.lower() for vxx in aawords]        ##;; lowercase
          ## extend
          aawords.extend( [vxx[::-1] for vxx in aawords] )                               ##;; reversal
          aawords.extend( [self.wordnumberize(vxx[0:7]) for vxx in aawords[0:10000]] )   ##;; wordnumberize  
          ##;;
          
          ## remove_dupes
          aawords   =   sorted(set(aawords))
          vout      =   aawords
          self.wordlist = vout
          ##;;
        ##endif
  
        ## return      
        vout        =   self.listshuffle(vout)
        return vout
        ##;;
    ##enddef
  
    def get_ngram(self, isize=3,sdelim='_'):
        """
        get a dicware ngram 
        """
        iggngram  =   isize
        sggdelim  =   sdelim
        aawords   =   self.get_wordlist()
                
        ## output
        ngram     =   sggdelim.join(aawords[0:iggngram])
        return ngram
        #print aafuncs
    ##enddef

### --------------------------------------
### begin_:

if (__name__ == "__main__"):
  
    otest = DataHelperDiceware()
    for item in xrange(15):
      print otest.get_ngram(3,'_')

