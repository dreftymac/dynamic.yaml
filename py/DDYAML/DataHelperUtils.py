### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### init py
if('python_region'):
      ## init py
      import base64
      import codecs
      import csv
      import datetime
      import glob
      import jinja2
      import json
      import platform
      import markdown
      import os
      import random
      import requests
      import re
      import shutil
      import string
      import StringIO
      import sys
      import textwrap
      import time
      import uuid
      import xlrd
      import yaml
      import zipfile
      
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### DataHelperUtils
if('python_region'):
### <beg-region_testiff_20151229121946>
###!- caption:  DataHelperUtils
###!  date:     created="Tue Dec 29 12:19:46 2015"
###!  goal:     |
###!       __blank__
###!  result:   |
###!       __blank__
###!  tags:     __tags__
###!  seealso: |   
###!  		* __blank__
###!  desc: |   
###!  		__desc__
###!  
###!  
###!  dreftymacid: itch_drain_resorts
###!  wwbody: |
      class DataHelperUtils():
        
        ##
        def py_mergedict(self, dict1, dict2):
          '''
          TODO: move this into DataHelperUtils
          python addon function for merging nested dictionaries
          see also:
          * http://stackoverflow.com/a/7205672/42223
          '''
          for ppk in set(dict1.keys()).union(dict2.keys()):
              if ppk in dict1 and ppk in dict2:
                  if isinstance(dict1[ppk], dict) and isinstance(dict2[ppk], dict):
                      yield (ppk, self.dict(py_mergedict(dict1[ppk], dict2[ppk])))
                  else:
                      # If one of the values is not a dict, you can't continue merging it.
                      # Value from second dict overrides one in first and we move on.
                      yield (ppk, dict2[ppk])
                      # Alternatively, replace this with exception raiser to alert you of value conflicts
              elif ppk in dict1:
                  yield (ppk, dict1[ppk])
              else:
                  yield (ppk, dict2[ppk])
        ##enddef        
        
        ##
        def dict_find_multikey(self,dd_source={},knownkeys=[],sdefault=''):
          """
          find a value associated with potential synonym keys
          http://stackoverflow.com/questions/29259204/how-to-get-a-value-from
          """
          ##
          vfind           =   [dd_source.get(vxx) for vxx in knownkeys if(not dd_source.get(vxx) is None)]
          vout            =   vfind[0] if vfind else sdefault
          ##
          return vout
        ##enddef
        
        ##
        def dict_to_nvptable(self,vdict,fldorder=[]):
          """
          changes BEFORE into AFTER
          
          BEFORE (native python dictionary):  
            {"fname":"homer","lname":"simpson","age":33}
  
          AFTER (native python aod represented as yaml):
              - name:   age
                value:  33
              - name:   fname
                value:  homer
              - name    lname
                value:  simpson
          """
          
          ##
          vout = []
  
          ##
          if (len(fldorder) == 0): fldorder = sorted(vdict.keys())
          
          ##
          for fld in fldorder:
            orec = {}
            if fld in vdict:
              orec['value']   =   vdict[fld]
              orec['name']    =   fld
              vout.append(orec)
            
          ##
          return vout
        ##enddef
        
        ##
        def excel_sheet_to_python_aod(self,oparams={}):
          """
          desc: convert excel spreadsheet to python aod
          arr_fldtypes:
            - int
            - text
            - float
            - date
          usage: |
              oparams = {}
              oparams['xlpath']     =   '../excel/people.simple30.xls'  ## excel filepath
              oparams['xlsheet']    =   1                               ## wkbk sheet index (one-based)
              oparams['xlfirstrow'] =   4                               ## first datarow    (one-based)
              oparams['datadef']    =   yaml.safe_load('''              ## sheet dataschema
                - {fldname: lname     ,    fldtype: TEXT , fldlabel: "Last Name" }
                - {fldname: fname     ,    fldtype: TEXT , fldlabel: "First Name" }
                - {fldname: amount    ,    fldtype: INT  , fldlabel: "Amount" }
                - {fldname: age       ,    fldtype: INT  , fldlabel: "Age" }
                - {fldname: nation    ,    fldtype: TEXT , fldlabel: "Nation" }
                - {fldname: platform  ,    fldtype: TEXT , fldlabel: "Platform" }
                - {fldname: date      ,    fldtype: DATE , fldlabel: "Current Date" }
              ''')
              excel_sheet_to_python_aod(oparams)
          """
          
          ## try-catch
          try:
            ## init defaults smartmerge
            myparam = {}
            myparam['xlpath']       =   ''
            myparam['xlsheet']      =   1
            myparam['xlfirstrow']   =   2
            myparam['datadef']      =   []
            myparam.update(oparams)
            ##;;
            
            ## testing
            # print"""### ------------------------------------------------------------------------ """
            # oDumper.pprint( myparam )
            # exit()
            ##;;            
            
            ## init
            ssfileorig      =   self.dict_find_multikey(myparam,['xlpath','path','filepath'],'')
            sheet           =   int(self.dict_find_multikey(myparam,['xlsheet','sheet'],'1'))
            firstrow        =   int(self.dict_find_multikey(myparam,['xlfirstrow','firstrow'],'1'))
            ##;;
            
            ## testing
            # print"""### ------------------------------------------------------------------------ """
            # oDumper.pprint( myparam )
            # oDumper.pprint( datadef )
            # exit()
            ##;;                    
            
            ## init
            book              =   xlrd.open_workbook(ssfileorig)
            sheet             =   book.sheet_by_index(int(sheet-1))
            aadataout         =   []
            ddheaderrow       =   []
            iitotcols         =   (sheet.ncols)
            #print iitotcols
            ##;;
  
            ## init ;; validate dataschema if exist
            if(True
              and myparam["datadef"].__len__()    != 0      ## user-defined-dataschema (udd) exists
              and iitotcols > myparam['datadef'].__len__()  ## udd has fewer fields than sheet.ncols
              ):
              ## wipeout any datadef and create_datadef_from_scratch
              myparam["datadef"] = []              
              # print '''
              # ## Caution: 
              # ## Possible mismatch or non-well-formed user defined dataschema
              # '''
              # for tmpcol, ixx in enumerate(range(sheet.ncols)):
              #   ##
              #   if(ixx <= myparam["datadef"].__len__()):
              #     continue
              #   ##
              #   tmprec  = {}              
              #   tmprec["fldname"]   = 'fld%03d'%(ixx)
              #   tmprec["fldtype"]   = 'text'
              #   tmprec["fldlabel"]  = 'fld%03d'%(ixx)              
              #   myparam["datadef"].append(tmprec)
              #   #print ixx
              #   #print self.xlrd_get_value(book,sheet.cell(1,ixx),'fld%s'%(ixx))
            ##;;
          except Exception as msg:
            print 'EXCEPTION adi_dining_servants msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;
          
          ## try-catch
          try:          
            ## init dataschema if empty create_datadef_from_scratch
            if(myparam["datadef"].__len__() == 0):
              print """### excel_sheet_to_python_aod: missing or incomplete dataschema, using generic auto-generated schema instead"""
              for tmpcol, ixx in enumerate(range(sheet.ncols)):
                tmprec  = {}              
                tmprec["fldname"]   = 'fld%03d'%(ixx)
                tmprec["fldtype"]   = 'text'
                tmprec["fldlabel"]  = 'fld%03d'%(ixx)
                myparam["datadef"].append(tmprec)
            ##;;
          except Exception as msg:
            print 'EXCEPTION toplofty_hyper_dreamily msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;            
          
          ## try-catch
          try:          
            ## process dataschema
            for row in myparam["datadef"]:
              ddheaderrow.append(self.dict_find_multikey(row,['fldname','fieldname',]))
            ##;;
          except Exception as msg:
            print 'EXCEPTION minks_merge_unsound msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;
          
          ## try-catch
          try:          
            ## iterate rows
            for row_index in range(sheet.nrows):
              if(row_index  < firstrow): continue  ## skip until we reach first datarow
              rowout        = {}
              ## iterate columns
              for col_index in range(sheet.ncols):
                  sheet_cell = sheet.cell(row_index,col_index)
                  rowout[ ddheaderrow[col_index] ] =  self.xlrd_get_value(book,sheet_cell,myparam["datadef"][col_index])
              ##endfor
              aadataout.append(rowout)
            ##endfor
          except Exception as msg:
            print 'EXCEPTION clueing_henchman_swam msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;              
          
          ## return aadataout
          ## print yaml.dump(aadataout,default_flow_style = False)
          return aadataout
        ##enddef        
        
        ##
        def xlrd_get_value(self,book,sheet_cell,rec_datadef={}):
          """
          /**
            * dependencies:
            *   import xlrd
            *   import datetime
            * 
            * rec_datadef:
            *    {fldname: ID , fldtype: INTEGER }    
            *
            * example: 
            * @code
            *   _example_
            * @endcode
            *
            * @param xlrd book       $book (required|) xlrd workbook object
            * @param xlrd sheet_cell $sheet_cell (required|) xlrd sheet_cell object
            * @param rec_datadef    rec_datadef (optional|) python dict datadef 
            * @return var output
            *   
            */ 
          """
          ## init vars
          vout        =   ''
          rxnewline   =   re.compile('\n|\r\n|\r|\n\r')
          
          ### ------------------------------------------------------------------------
          ## handle excel type
          if(False): vout = ''
          ##
          elif(sheet_cell.ctype == 3): # 3 means 'xldate' , 1 means 'text'
            ms_date_number = sheet_cell.value # Correct option 2
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(ms_date_number,book.datemode)
            py_date = datetime.datetime(year, month, day, hour, minute)
            vout    = py_date.__str__()
          ##
          elif(True):    
            vout = sheet_cell.value
          
          #oDumper.pprint(vout)
          
          ### ------------------------------------------------------------------------
          ## handle datadef type
          try:
            if(False):
              pass
            elif(rec_datadef['fldtype'].lower().startswith("int")):
              vout = int(vout)
            elif(rec_datadef['fldtype'].lower().startswith("text")):
              vout = str(vout).strip()
            elif(rec_datadef['fldtype'].lower().startswith("float")):
              vout = float(vout)
            elif(rec_datadef['fldtype'].lower().startswith("date")):
              vout = str(vout)
          except Exception as msg:
            pass
          ##endtry
          
          ### ------------------------------------------------------------------------
          ## handle python type
          if(False):
            pass
          elif(type(vout) is int):
            vout = vout
          elif(type(vout) is long):
            vout = vout
          elif(type(vout) is float):
            vout = vout
          elif(type(vout) is str):
            vout = re.sub(rxnewline, " ", vout)
          elif(type(vout) is unicode):
            vout = re.sub(rxnewline, " ", vout).encode('utf-8')
          ##endif
        
          ### ********************
          ## postprocess
          ##
          return vout
        ##enddef        
        
      ##endclass

### <end-region_testiff_20151229121946>  
