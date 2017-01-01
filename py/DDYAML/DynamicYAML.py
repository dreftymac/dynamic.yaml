# -*- coding: utf-8 -*-
### <beg-file_info>
### main:
###   - date: created="Mon Jan 25 08:07:51 2016"
###     last: lastmod="Mon Jan 25 08:07:51 2016"
###     tags: python, ddyaml, runner
###     dreftymacid: "sue_wireworm_venusian"
###     filetype: "py"
###     seealso: |
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/jinjafilterdynamicyaml.py"
###     desc: |
###         desc
### <end-file_info>

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

  ## pprint
  import pprint
  oDumper = pprint.PrettyPrinter(indent=4);
  ## oDumper.pprint( directives )

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

        ##
        def __init__(self,options={},**kwargs):

          ## init defaults (TODO ;; code refactor use self.options instead of options)
          self.options = {}
          self.options['ddyaml_string_enddata']   = '__yaml__'
          self.options['ddyaml_process_twopass']  = True
          ## bkmk001 ;; support for jinja2.FileSystemLoader ;;
          self.options['filesystemloader_paths']        = []
          self.options['jinja2_globals']                = {}

          ## bring in any globals
          try:
            for item in options['globals']:
              self.options['jinja2_globals'][item[0]] = item[1]
          except:
            pass
          ##;;

          ## jinja2_globals
          if(not 'debugging_alerts_01'):
            print "### nicer_simply_haze ------------------------------------------------------------------------"
            print self.options['jinja2_globals']
          ##;;

          ## allow for overriding defaults
          for tmpname, tmpvarr in kwargs.items():
              self.options[tmpname] = tmpvarr
          ##;;

          ##
          self.options['block_start_string'   ] = options.get('block_start_string'    , '{%')
          self.options['block_end_string'     ] = options.get('block_end_string'      , '%}')
          self.options['variable_start_string'] = options.get('variable_start_string' , '{{')
          self.options['variable_end_string'  ] = options.get('variable_end_string'   , '}}')
          self.options['comment_start_string' ] = options.get('comment_start_string'  , '{#')
          self.options['comment_end_string'   ] = options.get('comment_end_string'    , '#}')
          ##;;

          ##
          self.primaryYamlPath    =   options.get('path', '')          ## primaryYamlPath
          self.addonFilters       =   options.get('addonFilters', [])  ## addonFilterClasses
          ##
          if(self.primaryYamlPath.__str__() != ''):
            self.ffpath_main  =   self.primaryYamlPath.__str__()
            self.ffpath_norm  =   "/".join( self.ffpath_main.split("\\") )
            self.ffpath_pdir  =   "/".join( self.ffpath_norm.split("/")[0:-1] )
            self.ddffpath = {
              'main': self.ffpath_main,
              'norm': self.ffpath_norm,
              'pdir': self.ffpath_pdir,
            }
          elif(True):
            sgtemp = ("""
            \n## primaryYamlPath file not specified or unreachable
            """)
            ## print sgtemp

          ## self settings
          if(not not 'debugging_alerts_01'):
            print "### intently_grins_lament ------------------------------------------------------------------------"
            oDumper.pprint( self.options )
            print '''
            ## self.ddffpath
            main:   {main}
            norm:   {norm}
            pdir:   {pdir}
            '''.format(** self.ddffpath )
          ##;;

        ##enddef

        def provision_jinja2_environment(self):
          '''
          provision a jinja2 environment
          this is a prerequisite for rendering jinja2 output
          '''
          ## init jinja_environment
          self.Environment = jinja2.Environment(
            extensions=[
              'jinja2.ext.do',
              'jinja2.ext.loopcontrols',
              ]
            ## bkmk001
            ,loader=jinja2.FileSystemLoader( self.options['filesystemloader_paths'] )
            #,finalize=self.oenv_finalize
            )
          self.oenv = self.Environment
          ##;;

          # print "### ------------------------------------------------------------------------"
          # print "bkmk001 :: symbiote_security_dna"
          # print self.oenv.loader.list_templates()

          ## init jinja_globals
          ## supports variables that are accessible to every jinja template
          #self.oenv.globals = {"noop" : ""}
          try:
             for ddkey in self.options['jinja2_globals']:
                 self.oenv.globals[ddkey] = self.options['jinja2_globals'][ddkey]
          except:
             pass
          ##;;

          ## jinja2_globals
          if(not 'debugging_alerts_01'):
            print "### wizardly_vaselike_virility ------------------------------------------------------------------------"
            print self.oenv.globals
          ##;;

          ## init ;; jinja_config
          ## standard initializtion parameters for jinja2
          '''
          syntaxconfig          ;; syncondesc    ;; syncondefault
          block_start_string    ;; blockstart    ;; '{%'
          block_end_string      ;; blockend      ;; '%}'
          variable_start_string ;; variablestart ;; '{{'
          variable_end_string   ;; variableend   ;; '}}'
          comment_start_string  ;; commentstart  ;; '{#'
          comment_end_string    ;; commentend    ;; '#}'
          '''
          self.oenv.block_start_string    = self.options['block_start_string'   ]
          self.oenv.block_end_string      = self.options['block_end_string'     ]
          self.oenv.variable_start_string = self.options['variable_start_string']
          self.oenv.variable_end_string   = self.options['variable_end_string'  ]
          self.oenv.comment_start_string  = self.options['comment_start_string' ]
          self.oenv.comment_end_string    = self.options['comment_end_string'   ]
          self.oenv.cache_size            = '0'
          ##;;

          ## init custom filters for self.oenv
          for addonclass in self.addonFilters:
            self.oenv = addonclass.attach_filters( self.oenv )
              ## see href="./JinjaFilterBase.py"
              ## see href="./JinjaFilterDynamicYAML.py"
            pass
          ##;;

          ##
          #return self.oenv
        ##enddef

        #@ figure out optimal use of jinja finalize
        #@ def oenv_finalize(self,vinput):
        #@   vout = ''
        #@   if not (vinput is not None):
        #@     vout = '__blank__'
        #@   ##
        #@   return vout
        #@ ##enddef

        def py_mergedict(self, dict1, dict2):
          '''
          python addon function for merging nested dictionaries
          see also:
          * http://stackoverflow.com/a/7205672/42223
          '''
          for ppk in set( dict1.keys()).union(dict2.keys() ):
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
          ##
          vout  =  dict( self.py_mergedict(ob001,ob002) )
          return vout
        ##enddef

        ##
        def ff_resolvepath_read(self,spath=''):
          '''
          ### main:
          ###   - date: created="Thu Jul 16 15:30:22 2015"
          ###     desc:    read a string filepath with path that is potentially relative to path of strYamlCustomEndSection
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
          if(os.access(spath,os.R_OK)):
            getpath = spath
          ## check if spath is readable as relative to path of strYamlCustomEndSection
          if(os.access(spath_mod01,os.R_OK)):
            getpath = spath_mod01
          ## try to read the file
          if(sscurr ==  '' and (not getpath == '')):
            try:
              sscurr = open(getpath,'rb').read() + "\n"
            except Exception:
              pass
          return sscurr
        ##enddef

        ##
        def ff_resolvepath_path(self,spath=''):
          '''
          ### main:
          ###   - date: created="Thu Jul 16 15:30:22 2015"
          ###     desc:    resolve and return a file path where path is potentially relative to strYamlCustomEndSection
          ###     params:
          ###       - name: spath
          ###         opt:  required
          ###         desc: the potentially_relative path
          ###     return_value: |
          ###         fully_qualified_path
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
          ## check if spath is readable as relative to path of strYamlCustomEndSection
          if(os.access(spath_mod01,os.R_OK)): getpath = spath_mod01
          ##
          return getpath
        ##enddef

        ##
        def ff_filepath_to_dirpath(self,spath=''):
          '''
          ### main:
          ###   - date: created="2016-03-25T16:36:26"
          ###     desc: >
          ###       take a path that points to a file and convert it to path
          ###       that points to the parent directory of that file
          ###     params:
          ###       - name: spath
          ###         opt:  required
          ###         desc: the potentially_relative path
          ###     return_value: |
          ###         string path
          ###     details: |
          ###         _details_
          ###     example: |
          ###         _example_
          ###     seealso: |
          ###         *
          '''
          ##
          sscurr      =   ''
          getpath     =   ''
          spath_mod01 =   '/'.join( [self.ffpath_pdir,'/',spath]  )
          ## check if spath is readable without modification
          if(True
              and os.access(spath,os.R_OK)
              and os.path.isdir(spath)
              ):
            getpath = spath
          ##;;

          ## check if spath points to a file
          if(True
              and os.access(spath,os.R_OK)
              and os.path.isfile(spath)
              ):
            getpath = os.path.dirname(spath)
          ##;;

          ##
          return getpath
        ##enddef

        #@@ ## TODO ;; refactor this ;; parasitic inheritance method that just returns the result of
        #@@ ##    firstpass multipass processing
        #@@ ##    YamlEmbedJinja.template_render_1stpass
        def ddexport(self,rawstr):
          from YamlEmbedJinja import YamlEmbedJinja ### "./YamlEmbedJinja.py"
          parser01  =   YamlEmbedJinja()
          ddexport_vout      =   parser01.template_render_1stpass(yaml=rawstr)
          return ddexport_vout
        ##enddef

        ##
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
          ## placeholder syntax
          sgg_dynamicyaml_key     =   self.options['ddyaml_string_enddata']
          sgg_dynamicyaml_key     =   sgg_dynamicyaml_key.lower()
          sgg_directiveprefix_str =   ''
          ##;;

          ## init vars
          ddtransform_aaout  =   []
          ssgpath         =   ''
          originalconfig  =   {}
          ##;;

          ### TODO ;; adopt the conventions from yamlembedjinja ;; yamlregions
          ###     href="./YamlEmbedJinja.py" find="blast_tinworks_reply"
          ###     href="./YamlEmbedJinja.py" find="yamlregions_primary"
          ### TODO ;; get strYamlCustomEndSection and svirtualtemplate sorted out
          ###     the use between these variables is sub-optimal
          ### ------------------------------------------------------------------------
          if('load_attempt_stora'):
            ##
            bload_stora_success       =   False
            strYamlCustomEndSection   =   ''

            ## get strYamlCustomEndSection from primaryYamlPath
            try:
              ssgpath = self.ffpath_norm
            except Exception:
              #return ''
              pass
            ##;;

            ##
            if(not bload_stora_success):
              ###
              try:
                strYamlCustomEndSection     =     codecs.open(ssgpath, 'r', 'utf-8').read()
                if( self.options['ddyaml_process_twopass'] ):
                  strYamlCustomEndSection   =     self.ddexport(strYamlCustomEndSection)
                originalconfig        =     yaml.safe_load(strYamlCustomEndSection) or originalconfig
                bload_stora_success   =     True
              except:
                pass
              ###;;;
            ##;;
          ## endif

          ##
          if( not 'debugging_alerts_01'):
            print originalconfig              ## endsection_as_data
            print strYamlCustomEndSection     ## endsection_as_string
            #print svirtualtemplate

          ### ------------------------------------------------------------------------
          ## init directives_dictionary
          directives = {}
          directives['default_data']            = ''
          directives['default_tpl_with_procs']  = ''
          directives['current_data']        = ''
          directives['current_template']    = ''
          directives['default_data']        = originalconfig.copy()
          ##;;

          ##
          try:
            ## remove the sgg_dynamicyaml_key from default data
            del(directives['default_data'][sgg_dynamicyaml_key])
          except:
            pass
          ##;;

          ##
          if( not 'debugging_alerts_01'):
            oDumper.pprint( directives ) ## directives_as_clean_init

          ## <beg-process01>
          try:
            ## set default_tpl_with_procs
            ##    use this as the default template if one not specified
            if( directives['default_tpl_with_procs'].__str__() == ''):
              directives['default_tpl_with_procs'] = strYamlCustomEndSection
            ##;;

            ## prepare to iterate_directives ;; tmp_processing_directives
            tmp_processing_directives = originalconfig.pop(sgg_dynamicyaml_key,[])
            if (tmp_processing_directives.__len__() == 0):
              tmp_render  =   self.ddexport(strYamlCustomEndSection)
              ddtransform_aaout.append( tmp_render )

            ## iterate_directives ;; tmp_processing_directives
            for row in tmp_processing_directives:
              directives['current_template']    = directives['default_tpl_with_procs']
              directives['current_data']        = directives['default_data']

              ### ********************
              ## process row

              ## @@@ usedataroot directive ;; wrap all the template data in a common 'dataroot' element
              ## (eg) usedataroot: "myworkbook"
              ## (eg) usedataroot: "datarootf"
              tmpname = ['use','dataroot']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                if(str(tmpval).strip() != ''):
                  directives["".join(tmpname)] = str(tmpval)
              ##;;

              ## DEPRECATED ;; use processthis directive instead
              ## @@@ rowkeep directive ;; skip this entire processing row if rowkeep evals to false
              tmpname = ['row','keep']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                if(bool(tmpval) == False): continue;
              ##;;

              ## DEPRECATED ;; use processthis directive instead
              ## @@@ rowskip directive ;; skip this entire processing row if rowskip evals to true
              tmpname = ['row','skip']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                if(True and tmpval): continue;
              ##;;

              ## @@@ processthis directive ;; skip this entire processing row if processthis evals to false
              tmpname = ['process','this']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                if(bool(tmpval) == False): continue;
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
                #print tmpval
                tmpval = self.ff_resolvepath_path( row[tmpkey] )
                # exit()
                directives['current_'+tmpname[0]]   =   textwrap.dedent(open(tmpval,'rb').read())
                ## print tmpval
              ##;;

              ## @@@ template directive ;; we get template from strYamlCustomEndSection
              tmpname = ['template','']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                directives['current_'+tmpname[0]]   =   textwrap.dedent(tmpval)
                ## print tmpval
              ##;;

              ## @@@ templateincluede directive ;; we get one_or_more template from one_or_more external file
              ## and merge with strYamlCustomEndSection
              tmpname =   ['templateinclude']
              tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval    = row[tmpkey]
                tmptable  = []
                tmp_row_curr = {}

                ## prepare items ;; force_scalar_to_list
                sstemp = ''
                if(tmpval is None):
                  tmpval = ['']
                if( type(tmpval) == str ):
                  tmpval = [tmpval] ## force_scalar_to_list
                ##;;

                ## iterate items ;; force_items_to_rows
                tmp_row_default = {
                  'section':  '',
                  'path':     '',
                }
                for item in tmpval:
                  if (None is True):
                    pass
                  elif (type(item) is str):
                    ## assume bare str is file path
                    tmp_row_curr = ({
                      "section":  "head",
                      "path":     self.ff_resolvepath_read( item ),
                      }).update(tmp_row_default)
                    tmptable.append( tmp_row_curr )
                  elif (type(item) is dict):
                    tmptable.append( item )
                ##;;

                ## iterate rows in tmptable
                for row in tmptable:
                  pass

                ## iterate items
                for spath in tmpval:
                  #sscurr        =   ''
                  ## return readable path or else empty string
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

              ## bkmk001
              ## @@@ pathinclude directive ;; we get one_or_more path for use with jinja.FileSystemLoader
              tmpname =   ['pathinclude']
              tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]

                ## iterate includes ;; force_scalar_to_list
                sstemp = ''
                if(tmpval is None):
                  tmpval = ['']
                if(  type(tmpval) == str ):
                  tmpval = [tmpval] ## force_scalar_to_list

                ## iterate items ;; miner_starts_guava
                for spath in tmpval:
                  ## return readable path or else empty string
                  sscurr = self.ff_resolvepath_path(spath)
                  sscurr = self.ff_filepath_to_dirpath(sscurr)
                  # print " bkmk001 ### ------------------------------------------------------------------------ "
                  # print sscurr
                  #print os.path.dirname(sscurr)

                  ## err_quiet
                  if(sscurr == ''):
                    continue
                  ## err_verbose
                  if(sscurr ==  ''):
                    raise ValueError('wenga_hsiw_repel: failed to access file content at %s '%(spath))
                  elif(True):
                    self.options['filesystemloader_paths'].append( sscurr )
                    # print " bkmk001 :: directs_dozer_forums ### ------------------------------------------------------------------------ "
                    # print sscurr

                ##
                # if(sstemp != ''):
                #   directives['current_'+tmpname[0]]   =   sstemp
                ## print tmpval
              ##;;

              ## @@@ datainclude directive ;; concatenate multiple yaml files to input additional data
              ## and merge it with strYamlCustomEndSection
              tmpname =   ['datainclude','']
              tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]

                ## iterate includes ;; force_scalar_to_list
                sstemp = ''
                if(tmpval is None):
                  tmpval = ['']
                if(  type(tmpval) == str ):
                  tmpval = [tmpval]     ## force_scalar_to_list

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
                    sscurr    = self.ddexport(sscurr) ##;; apply firstpass transform to embedded datainclude
                    sstemp    += sscurr
                ##
                if(sstemp != ''):
                  ## print sstemp
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

              ## @@@ data directive ;; we get data from strYamlCustomEndSection
              tmpname = ['data','']
              tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
              #print row
              if( (tmpkey) in row ):
                tmpval = row[tmpkey]
                directives['current_'+tmpname[0]]   =   yaml.safe_load(tmpval)
              ##;;

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
              if(not 'debugging_alerts_01'):
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
              directives['default_data'].update(directives['current_data'])
              ## bkmk001
              self.provision_jinja2_environment()
              #oEnv  =  self.oenv
              otemplate_data  =   directives['default_data']
              mystring        =   textwrap.dedent(directives['current_template'])
              template        =   self.oenv.from_string(mystring)
              tmpout          =   template.render(otemplate_data)

              if(not 'debugging_alerts_01'):
                  print "### ------------------------------------------------------------------------"
                  print "\n\n\n"
                  print "%s" %( mystring )
                  print "\n\n\n"
                  print "### ------------------------------------------------------------------------"
                  exit()

              ## force unix line endings
              if(True):
                tmpout = string.replace(tmpout, '\r\n', '')
                tmpout = string.replace(tmpout, '\r', '')
              ddtransform_aaout.append( tmpout )
          ##;;
          ## exception ;; process01
          except Exception as msg:
            print 'EXCEPTION voyeur_foulest_weirdly msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ## print tmpout
          #oDumper.pprint( otemplate_data )
          #print( directives['current_template'] )

          ## postproc directives
          try:
            if('current_outputfile' in directives):
              spath = directives['current_outputfile']
              open(spath,'w').write(tmpout)
          except Exception as msg:
            print 'EXCEPTION ariser_twister_teams msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            #print(exc_type, fname, exc_tb.tb_lineno)
            ##;;
          ## <end-process01>
          #oDumper.pprint( directives )
          ##endfor::iterate_yaml

          #print yaml.safe_dump( ddtransform_aaout , default_flow_style=False  )
          ##vjj = "\n"
          vjj   = ""
          ddtransform_aaout  = [vjj +  vxx for vxx in ddtransform_aaout]
          ddtransform_aaout  = "".join(ddtransform_aaout)
          ##;;

          #print self.oenv.filters
          #print self.oenv.finalize

          ##
          return ddtransform_aaout
        ##enddef
      ##endclass
###!}}}
