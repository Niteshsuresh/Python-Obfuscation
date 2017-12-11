#!/usr/bin/python
# -*- coding: utf-8 -*-
䧞=len
𐠋=open
ﻂ=iter
㣷=True
𐤋=False
ﻴ=map
𥫸=filter
𐠔=sorted
𐲎=None
𧣞=max
𤦒=print
import re
𐏌=re.compile
𐪇=re.sub
import sys
𠷑=sys.argv
class 𝖷:
 def addQMark(self,낉):
  ﵮ=낉[0].replace('?','')
  낉[0]=𐪇('(?<=.)','?',ﵮ)
  return 䧞(낉[0])-䧞(ﵮ)
 def makeRegex(self,뉤):
  낉=[뉤]
  鱗=self.addQMark(낉)
  뉤=낉[0]
  𐣦='^'+뉤+'$'
  if 鱗==1:
   𐣦=뉤.replace('?','')
  return 𐣦
 def fileRead(self,filename):
  ﻧ=[]
  with 𐠋(filename,'rb')as f:
   for 穊 in ﻂ(f.readline(),''):
    ﻧ.append(穊.strip())
  return ﻧ
 def magicMatch(self,𥬔,𨅰,穊,):
  ޡ=self.magic(𨅰,穊)
  if ޡ==㣷:
   return 穊
  return 𐤋
  def 㙏(self):
   或=self.magicMatch(𥬔,𨅰,unFltWrd)
  return returnValue
  def ࢩ(self,wrd):
   ﴪ=wrd
   return ﴪ
 def filterDictWrds(self,𨅰,ﻧ):
  𬂀=ﻴ(ࢩ(fltWrd),𥫸(self.getMagicMatch(unFltWrd),ﻧ))
  return 𬂀
 def 𥬔(self,𨅰,穊):
  if 䧞(𨅰)<䧞(穊):
   return 𐤋
  𨅰=''.join(𐠔(𨅰))
  逰=self.makeRegex(𨅰)
  𐣦=𐏌(逰)
  return self.magicFilter(𐣦,穊)
 def magicFilter(self,𐣦,穊):
  穊=''.join(𐠔(穊))
  𤥾=𐣦.search(穊)
  if 𤥾 is not 𐲎:
   return 㣷
  return 𐤋
 def longest(self,𨅰):
  ﻧ=self.fileRead('dictionary.txt')
  𦳎=self.filterDictWrds(𨅰,ﻧ)
  return 𧣞(𦳎,key=䧞)
def 𥬔():
 ߊ=𝖷()
 𐠑=ߊ.𥬔(𠷑[1],𠷑[2])
 return 𐠑
if __name__=='__main__':
 𤦒(𥬔());
# Created by pyminifier (https://github.com/liftoff/pyminifier)
