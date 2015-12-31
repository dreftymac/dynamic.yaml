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
      ##
      from JinjaFilterBase import JinjaFilterBase
      from JinjaFilterDynamicYAML import JinjaFilterDynamicYAML
      from TymacUtils import DataHelperUtils
      from TymacUtils import XmlssBase
      
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### DynamicYAML
if('python_region'):
###!{{{
###!- caption:  __caption__
###!  date:     created="Thu Jul 16 13:22:13 2015"
###!  dreftymacid: vadodara_glen_bird
###!  goal:     |
###!       __blank__
###!  result:   |
###!       __blank__
###!  tags:     __tags__
###!  seealso: |
###!          * __blank__
###!  desc: |
###!          __desc__
###!  wwbody: |
      class DynamicYAML(object):
        
        def __init__(self,ffpath=''):
          ## init jinja
          self.Environment  =   jinja2.Environment(extensions=['jinja2.ext.do','jinja2.ext.loopcontrols'])
          self.oenv         =   self.Environment
          if(ffpath.__str__() != ''):
            self.ffpath_main  =   ffpath
            self.ffpath_abso  =   "/".join( os.path.abspath(ffpath).split("\\") )
            self.ffpath_pdir  =   "/".join( os.path.dirname(self.ffpath_abso).split("\\") )
          elif(True):
            sgtemp = ("""
            \n## parent_yaml_config file not specified or unreachable
            """)
            print sgtemp
          #oDumper.pprint( self.ffpath_abso )
          #oDumper.pprint( self.ffpath_pdir )
        ##enddef
        
        ##
        def data_struct_merge(self,ob001,ob002,path=None):
          """
          ### main:
          ###   - date: created="Thu Jul 16 13:04:13 2015"
          ###     last: lastmod="Thu Jul 16 13:04:13 2015"
          ###     tags:           tags
          ###     author:         created="__author__"
          ###     dreftymacid:    "lastly_oxen_unearth"
          ###     seealso: |
          ###         *
          ###     desc: |
          ###         merges ob002 into ob001
          ###         * TODO ;; move this to datahelperutils
          """
          return dict(DataHelperUtils().py_mergedict(ob001,ob002))
        ##enddef

        def ff_resolvepath_read(self,spath):
          '''
          ### main:
          ###   - date: created="Thu Jul 16 15:30:22 2015"
          ###     desc:    read a file with path that is potentially relative to path of parent_yaml_config
          ###     params:
          ###       - name: spath
          ###         opt:  required
          ###         desc: the potentially_relative path
          ###     return_value: |
          ###         string content of file at spath
          ###     details: |
          ###         _details_
          ###     example: |
          ###         _example_
          ###     seealso: |
          ###         regain://python_is_readable
          '''
          ##
          sscurr      =   ''
          getpath     =   ''
          spath_mod01 =   '/'.join( [self.ffpath_pdir,'/',spath]  )
          ## check if spath is readable without modification
          if(os.access(spath,os.R_OK)):       getpath = spath
          ## check if spath is readable as relative to path of parent_yaml_config
          if(os.access(spath_mod01,os.R_OK)): getpath = spath_mod01
          ## try to read the file
          if(sscurr ==  '' and (not getpath == '')):
            try:
              sscurr = open(getpath,'rb').read() + "\n"
            except Exception:
              pass
          return sscurr
        ##enddef

        def ddtransform(self):
          """
          ### main:
          ###   - date: created="Thu Jul 16 13:55:43 2015"
          ###     last: lastmod="Thu Jul 16 13:55:43 2015"
          ###     tags:         tags
          ###     dreftymacid:  "darken_doubts_brains"
          ###     seealso: |
          ###         *
          ###     desc: |
          ###         desc
          """
          ## init jinja environment (oEnv) and extensions
          oEnv      =   self.oenv
          ##;;

          ## init custom filters for oEnv
          #import JinjaCustomFilter
          #import JinjaHTMLBasicFilter
          #import JinjaImacrosFilter
          oEnv  =   JinjaFilterDynamicYAML().attach_filters(oEnv)   ## href="#JinjaFilterDynamicYAML"
          #oEnv  =   JinjaImacrosFilter.attach_filters(oEnv)         ## href="../libpy/JinjaImacrosFilter.py"
          ## href="../../../../../../mytrybits/p/trypython2/lab2014/libpy/jinjaimacrosfilter.py"
          #oEnv      =   JinjaHTMLBasicFilter.attach_filters(oEnv)  ## href="../libpy/JinjaHTMLBasicFilter.py"
          ##;;

          ## placeholder syntax
          sgg_dynamicyaml_key     =   '__yaml__'
          sgg_dynamicyaml_key     =   sgg_dynamicyaml_key.lower()
          sgg_directiveprefix_str =   ''
          ##;;

          ## get parent_yaml_config (dynamic_yaml)
          vout          =   []
          ssgpath       =   ''
          try:
            ssgpath       =   self.ffpath_main
          except Exception:
            return ''
            pass

          ##
          parent_yaml_config = codecs.open(ssgpath, 'r', 'utf-8').read()
          #parent_yaml_config   =   open(ssgpath,'rb').read()
          orgconf       =   yaml.safe_load(parent_yaml_config)
          ##;;

          ## init directives_dictionary
          directives = {}
          directives['default_data']        = ''
          directives['default_template']    = ''
          directives['current_data']        = ''
          directives['current_template']    = ''
          ##;;

          ## <beg-process01>
          try:
            ## set defaults on directives_dictionary
            ##    from the parent_yaml_config
            ##    preserve every existing key, except remove the sgg_dynamicyaml_key
            directives['default_data']    = orgconf.copy()
            del(directives['default_data'][sgg_dynamicyaml_key])
            ##;;

            ## set default_template
            ##    use this as the default template if one not specified
            directives['default_template']      = parent_yaml_config
            ##;;

            ## iterate_yaml
            for row in orgconf[sgg_dynamicyaml_key]:
              directives['current_template']    = directives['default_template']
              directives['current_data']        = directives['default_data']

              ### ********************
              ## process row

              ## @@@ usedataroot directive ;; wrap all the template data in a custom 'dataroot' element
              ##
              tmpname = ['use','dataroot']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                if(str(tmpval).strip() != ''):
                  directives["".join(tmpname)] = str(tmpval)
              ##;;

              ## @@@ rowkeep directive ;; skip this entire processing row if rowkeep evals to false
              ## BUGNAG ;; this is not working
              tmpname = ['row','keep']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                if(bool(tmpval) == False): continue;
              ##;;

              ## @@@ rowskip directive ;; skip this entire processing row if rowskip evals to true
              tmpname = ['row','skip']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                if(True and tmpval): continue;
              ##;;

              ## @@@ outputfile directive ;; output content to a file without having to use jjtofile
              tmpname = ['output','file']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                directives['current_'+''.join(tmpname)]   =   tmpval
                #print tmpval
              ##;;

              ## @@@ templatefile directive ;; we get a template from a single external file
              tmpname = ['template','file']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                directives['current_'+tmpname[0]]   =   textwrap.dedent(open(tmpval,'rb').read())
                ## print tmpval
              ##;;

              ## bkmk001
              ## @@@ template directive ;; we get template from parent_yaml_config
              tmpname = ['template','']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                directives['current_'+tmpname[0]]   =   textwrap.dedent(tmpval)
                ## print tmpval
              ##;;

              ## bkmk001
              ## @@@ templateincluede directive ;; we get one_or_more template from one_or_more external file
              ## and merge it with the data in the parent_yaml_config
              tmpname =   ['templateinclude']
              tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]

                ## iterate includes ;; force scalar to list
                sstemp = ''
                if(tmpval is None):
                  tmpval = ['']
                if(  type(tmpval) == str ):
                  tmpval = [tmpval]     ## force scalar to list

                ## iterate items
                for spath in tmpval:
                  sscurr        =   ''
                  sscurr        =   self.ff_resolvepath_read(spath)
                  ## err_quiet
                  if(sscurr == ''):
                    continue
                  ## err_verbose
                  if(sscurr ==  ''):
                    raise ValueError('undid_sail_unleash: failed to access file content at %s '%(spath))
                  elif(True):
                    sstemp += sscurr
                ##
                if(sstemp != ''):
                  directives['current_'+tmpname[0]]   =   sstemp
                ## print tmpval
              ##;;

              ## @@@ datainclude directive ;; concatenate multiple yaml files to input additional data
              ## and merge it with the data in the parent_yaml_config
              tmpname =   ['datainclude','']
              tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]

                ## iterate includes ;; force scalar to list
                sstemp = ''
                if(tmpval is None):
                  tmpval = ['']
                if(  type(tmpval) == str ):
                  tmpval = [tmpval]     ## force scalar to list

                ## iterate items
                for spath in tmpval:
                  sscurr        =   ''
                  sscurr        =   self.ff_resolvepath_read(spath)
                  ## err_quiet
                  if(sscurr == ''):
                    continue
                  ## err_verbose
                  if(sscurr ==  ''):
                    raise ValueError('undid_sail_unleash: failed to access file content at %s '%(spath))
                  elif(True):
                    sstemp += sscurr
                ##
                if(sstemp != ''):
                  ##print sstemp
                  directives['current_'+tmpname[0]]   =   yaml.safe_load(sstemp)
                ## print tmpval
              ##;;

              ### TODO ;; NOT_YET_SUPPORTED
              ### @@@ dataurl directive ;; we get a data from an included url
              #tmpname = ['data','url']
              #tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              #if( (tmpkey) in row ):
              #  tmpval = row[tmpkey]
              #  directives['current_'+tmpname[0]]   =   yaml.safe_load(open(tmpval,'rb').read())
              ##;;

              ## @@@ data directive ;; we get data from parent_yaml_config
              tmpname = ['data','']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              #print row
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                directives['current_'+tmpname[0]]   =   yaml.safe_load(tmpval)
              ##;;

              ## bkmk001
              ## preproc directives
              if('current_templateinclude' in directives):
                directives['current_template'] = directives['current_templateinclude'] + directives['current_template']

              if('current_datainclude' in directives):
                directives['current_data'] = self.data_struct_merge(directives['current_datainclude'],directives['current_data'])

              if('usedataroot' in directives):
                tmpname = directives['usedataroot']
                directives['current_data'] = {tmpname: directives['current_data']}

              ## debug before render
              #oDumper.pprint( directives )
              #print yaml.safe_dump( directives )
              #print json.dumps(directives, sort_keys=True,indent=4, separators=(',', ': '))
              #print yaml.safe_dump(directives, default_flow_style=False)
              if(not 'debugging'):
                mykeys = directives.keys()
                mykeys.sort()
                for tmpkey in mykeys:
                  print "\n\n\n"
                  print "### ------------------------------------------------------------------------"
                  print "### %s" %(tmpkey)
                  print "### ------------------------------------------------------------------------"
                  print directives[tmpkey]
                exit()

              ## render output
              ## TODO ;; allow customizable data merge semantics
              otemplate_data  =   self.data_struct_merge(directives['default_data'],directives['current_data'])
              template        =   oEnv.from_string(textwrap.dedent(directives['current_template']))
              tmpout          =   template.render(otemplate_data)

              ## force unix line endings
              if(True):
                tmpout = string.replace(tmpout, '\r\n', '')
                tmpout = string.replace(tmpout, '\r', '')
              vout.append( tmpout )

          ## exception ;; process01
          except Exception as msg:
            print 'UNEXPECTED TERMINATION voyeur_foulest_weirdly msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ## print tmpout
          #oDumper.pprint( otemplate_data )
          #print( directives['current_template'] )

          ## postproc directives
          try:
            if('current_outputfile' in directives):
              spath = directives['current_outputfile']
              open(spath,'w').write(tmpout)
          except Exception as msg:
              print 'UNEXPECTED TERMINATION ariser_twister_teams msg@%s'%(msg.__repr__())
              exc_type, exc_obj, exc_tb = sys.exc_info()
              fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            #print(exc_type, fname, exc_tb.tb_lineno)
            ##;;
          ## <end-process01>


            #oDumper.pprint( directives )
          ##endfor::iterate_yaml


          #print yaml.safe_dump( vout , default_flow_style=False  )
          ##vjj = "\n"
          vjj = ""
          #vjj = "\n### ------------------------------------------------------------------------\n"
          #vjj = "\n### ------------------------------------------------------------------------\n"
          vout = [vjj +  vxx for vxx in vout]
          vout = "".join(vout)


          return vout
        ##enddef
      ##endclass
###!}}}
