### <beg-file_info>
### main:
###   - date: created="Thu Jul 16 12:05:49 2015"
###     last: lastmod="Thu Jul 16 12:05:49 2015"
###     tags: dynamicyaml, python, yaml, blockspring
###     author:         created="dreftymac"
###     dreftymacid:    "beamer_weave_text"
###     TODO:
###         - testing     ;; run through unit tests in demo for regressions from ddyaml.py
###         - pluggable   ;; add python pip install support
###         - feature     ;; add support for raw input string and not just input file
###         - feature     ;; if no __yaml__ sigil present, assume pure jinja syntax
###         - feature     ;; add support for pluggable filters besides JinjaFilterDynamicYAML
###         - feature     ;; add support for pluggable alternate template engines besides python/jinja2
###         - pluggable   ;; myclip snippet plugin filter
###     seealso: |
###         * href="../../../../../../mytrybits/y/tryyaml/dynamicyaml/devlog.txt"
###         * href="../../../../../../mytrybits/p/trypython2/2009/j/jinja.template/readme.md"
###     desc: |
###         ddyaml.py
###         core dynamic yaml in a single standalone python file
###
### <end-file_info>

### ##beg_func_docs
### - caption:  __caption__
###   date:         lastmod="__lastmod__"
###   grp_maj:      grp_maj
###   grp_med:      grp_med
###   grp_min:      grp_min
###   desc:         __desc__
###   dreftymacid:  __dreftymacid__
###   detail:  |
###     __detail__
###   dependencies:
###     - __blank__
###   params:
###    - param: jjinput ;; optarity ;; placedholder arg for jinja raw input string
### ##end_func_docs

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### init_python
if('python_region'):
###!{{{
###!- caption:  init_python
###!  date:     created="Sun Jan 04 02:56:24 2015"
###!  tags:     tags
###!  desc: |
###!      init python libraries and globals
###!  dreftymacid: sensible_warm_latex
###!  wwbody: |
      import base64
      import codecs
      import datetime
      import glob
      import jinja2
      import json
      import markdown
      import os
      import random
      import requests
      import re
      import string
      import sys
      import textwrap
      import time
      import uuid
      import yaml
      import zipfile
      
      ##
      import pprint
      oDumper = pprint.PrettyPrinter(indent=4);
      
      ##
      ## TODO: improve handling of addon libraries
      ## os.sys.path.insert(0,'c:/sm/docs/mytrybits/p/trypython2/lab2014/libpy')
      
      ##
      def py_mergedict(dict1, dict2):
        '''
        python addon function for merging nested dictionaries
        see also:
        * http://stackoverflow.com/a/7205672/42223
        '''
        for ppk in set(dict1.keys()).union(dict2.keys()):
            if ppk in dict1 and ppk in dict2:
                if isinstance(dict1[ppk], dict) and isinstance(dict2[ppk], dict):
                    yield (ppk, dict(py_mergedict(dict1[ppk], dict2[ppk])))
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
###!}}}

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### yaml helper DerivedBaseRepresenter
if('python_region'):
###!{{{
###!- caption:  __caption__
###!  date:     created="Thu Jul 16 13:21:33 2015"
###!  goal:     |
###!       helper methods for yaml to support yamlpretty output format
###!  result:   |
###!       __blank__
###!  tags:     yaml, addon
###!  seealso: |
###!  		* __blank__
###!  desc: |
###!  		__desc__
###!
###!
###!  dreftymacid: granular_ever_milt
###!  wwbody: |
      class DerivedBaseRepresenter(yaml.representer.BaseRepresenter):
        
        def yaml_addon_should_use_block(self,value):
          '''
          ## function docs
          - caption:  yaml_addon_should_use_block
            date:     lastmod="Mon 2014-10-20 16:45:46"
            desc:     helper method for yaml pretty output
          '''
          vout = False
          for ccx in u"\u000a\u000d\u001c\u001d\u001e\u0085\u2029":
              if ccx in value:
                  vout = True
          return vout
        ##enddef
    
        def yaml_addon_represent_scalar(self, tag, value, style=None):
          '''
          ## function docs
          - caption:  yaml_addon_represent_scalar
            date:     lastmod="Mon 2014-10-20 16:45:46"
            desc:     helper method for yaml pretty output
          '''
          ##
          if style is None:
              if self.yaml_addon_should_use_block(value):
                  style='|'
              else:
                  style = self.default_style
          ##
          node = yaml.representer.ScalarNode(tag, value, style=style)
          if self.alias_key is not None:
              self.represented_objects[self.alias_key] = node
          return node
        ##enddef
      ##endclass
###!}}}

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### jinja helper JinjaFilterBase
if('python_region'):
###!{{{
###!- caption:  __caption__
###!  date:     created="Thu Jul 16 13:21:33 2015"
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
###!  dreftymacid: __dreftymacid__
###!  wwbody: |
      class JinjaFilterBase(object):
        """
        Abstract Class for wrapping Jinja Custom Filters
        """
        
        def yaml_function_docs(self):
          '''
          ## function docs
          - caption:  yaml_function_docs
            date:     lastmod="Mon 2014-10-20 16:45:46"
            desc:     produce the function docs for this module as yaml
          '''
          vout = [str(getattr(self,vxx).__doc__) for vxx in dir(self) if(getattr(self,vxx).__doc__)and(vxx != '__module__')and(vxx != '__doc__') ]
          return "\n\n".join(vout)
        ##enddef
        
        def attach_filters(self,env):
          '''
          ## function docs
          - caption:  attach_filters
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  system
            grp_med:  jinja
            grp_min:  internal_use_only
            desc:     |
                attach custom filters to the main jinja environment
                current naming convention requires the filter function name to start with 'jj'
            dependencies:
              - import jinja2
            params:
             - param: env ;; required ;; core jinja environment
            dreftymacid: __blank__
          '''
          aallbase  =   [vxx for vxx in dir(self) ]
          aafilt    =   [vxx for vxx in aallbase if vxx.lower().startswith('jj')]
          for item in aafilt:
            env.filters[item] = getattr(self,item)
          return env
        ##enddef
        
        def prefilter(self,vstr):
          '''
          ## function docs
          - caption:  prefilter
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  system
            grp_med:  jinja
            grp_min:  internal_use_only
            desc:     kludgy jinja addon to shorten filter tags
            detail:  |
              prefilter allows for abbreviated tags
              this is not a desirable approach
              you have to pass a whole template in to use this
              and the abbrevated tags must not appear anywhere else
              or you will have delimiter collisions
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          vout = ''
          vout = re.sub('fqq','filter',vstr)
          ##
          return vout
        ##enddef
      ##endclass
###!}}}

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### jinja helper JinjaFilterDynamicYAML
if('python_region'):
###!{{{
###!- caption:  JinjaFilterDynamicYAML
###!  date:     created="Thu Jul 16 13:21:33 2015"
###!  dreftymacid: glint_unjam_cheapen
###!  goal:     |
###!       set of default jinja filters that come with ddyaml out of the box
###!  result:   |
###!       __blank__
###!  tags:     ddyaml, filter, addon, jinja
###!  seealso: |
###!  		* __blank__
###!  desc: |
###!  		Currently assumes jinja2 as the templating engine for ddyaml
###!  wwbody: |
      class JinjaFilterDynamicYAML(JinjaFilterBase):
        ### ------------------------------------------------------------------------
        ### begin_: drupal_specific
        
        ##
        def jjd_alias(self,jjinput):
          '''
          TODO move this out to drupal specific, for now included here for deadlines
          drupal URL aliases settings
          '''
          ##
          vout = jjinput.__str__()
          removals = []
          ##
          vout = vout.lower()
          vout = re.sub(r'[-]+',' ',vout)
          vout = re.sub(r'[^\w\s]+','',vout)
          #vout = re.sub(r'[\s]+','-',vout)
          vout = vout.split(' ')
          removals.append(''      )
          removals.append('a'     )
          removals.append('an'    )
          removals.append('as'    )
          removals.append('at'    )
          removals.append('before')
          removals.append('but'   )
          removals.append('by'    )
          removals.append('for'   )
          removals.append('from'  )
          removals.append('is'    )
          removals.append('in'    )
          removals.append('into'  )
          removals.append('like'  )
          removals.append('of'    )
          removals.append('off'   )
          removals.append('on'    )
          removals.append('onto'  )
          removals.append('per'   )
          removals.append('since' )
          removals.append('than'  )
          removals.append('the'   )
          removals.append('this'  )
          removals.append('that'  )
          removals.append('to'    )
          removals.append('up'    )
          removals.append('via'   )
          removals.append('with'  )
          vout = '-'.join([ixx for ixx in vout if ixx not in removals])
          #vout = re.sub(r'[-]+' ,'-',vout)
          ##
          return vout
        ##enddef

        ### ------------------------------------------------------------------------
        ### begin_: imacros_specific

        ##
        def jji_scripthead(self,jjinput):
          '''
          #TODO move this out to imacros specific, for now included here for deadlines
          #imacros spacify
          
          ##beg_func_docs
          - caption:  __caption__
            date:         lastmod="2015.08.05.1807"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         __desc__
            dreftymacid:  __dreftymacid__
            detail:  |
              __detail__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; ignored ;; placedholder for jinja raw input string
          ##end_func_docs
          '''
          ##
          vout    = jjinput.__str__()
          
          ##
          vout = '''
          TAB T=1
          ''TAB CLOSEALLOTHERS
          VERSION BUILD=8920312 RECORDER=FX
          SET !VAR1 "{{ "
          SET !VAR2 " }}"
          '''
          
          ##
          vout  = textwrap.dedent(vout)
          return vout
        ##enddef
        
        ##
        def jji_sp(self,jjinput):
          '''
          TODO move this out to imacros specific, for now included here for deadlines
          imacros spacify
          '''
          ##
          vout    = jjinput.__str__()
          ##
          vout    = re.sub(r'\n', '<BR>', vout)
          vout    = re.sub(r'^\s','', vout)
          vout    = re.sub(r'\s$','', vout)
          vout    = re.sub(r'[\s]+',' ', vout)
          vout    = re.sub(r'[\s]+','<SP>', vout)
          ##
          return vout
        ##enddef
                
        ##
        def jji_ngsp(self,jjinput):
          '''
          #TODO move this out to imacros specific, for now included here for deadlines
          #imacros spacify
          
          ##beg_func_docs
          - caption:  jji_ngsp
            date:         lastmod="__dates__"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         __desc__
            dreftymacid:  lobster_crime_areal
            seealso:
              - regain://jji_ngsp
              - regain://jji_scripthead
            detail:  |
              __detail__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; ignored ;; placedholder for jinja raw input string
            psrap_info:
              context:    	iim script that outputs code potentially containing angularjs (or any double-curly-brace syntax)
              problem:    	both NG and IIM use `{{ }}` for variable placeholders
              solution:   	in the output template, use jji_scripthead() which sets !VAR1 and !VAR2 to be equal to '{{' and '}}' respectively
              rationale:  	prevents IIM from trying to consume the NG placeholders
              example:
                - href="../../../../../../mytrybits/d/trydrupal/html/helloangular.000.yaml.txt" find="anchor_hunt_nailing_000"
                - href="../../../../../../mytrybits/d/trydrupal/html/helloangular.000.yaml.txt" find="vanadic_urolith_chorus"
          ##end_func_docs
          '''
          ##
          vout    = jjinput.__str__()
          ##
          vout    = re.sub(r'{{([^!])', '{{!VAR1}} \\1', vout)
          vout    = re.sub(r'([\W])}}', '\\1  {{!VAR2}}', vout)
          vout    = re.sub(r'\n', '<BR>', vout)
          vout    = re.sub(r'\n', '<BR>', vout)
          vout    = re.sub(r'^\s','', vout)
          vout    = re.sub(r'\s$','', vout)
          vout    = re.sub(r'[\s]+',' ', vout)
          vout    = re.sub(r'[\s]+','<SP>', vout)
          ##
          return vout
        ##enddef
        
        ### ------------------------------------------------------------------------
        ### begin_: general_purpose
        
        def jjaod_getrecord(self,jjinput,fieldname='fname',fieldvalue='value',iirec=0):
          '''
          ## function docs
          - caption:  jjaod_getrecord
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  data
            grp_med:  array_of_dictionary
            grp_min:  select
            desc:     aod get record where `fieldname` == `fieldvalue`
            detail:  |
                aod select record where `fieldname` == `fieldvalue`
            dependencies:
              - none
            example:
              -
            params:
              - param: jjinput    ;; required ;; raw input string
              - param: fieldname  ;; required ;; aod select field
              - param: fieldvalue ;; required ;; aod select value
              - param: iirec      ;; optional ;; optional record index if more than one record is obtained
            dreftymacid:  byte_urethral_behold
            output: python list (or `__blank__` if no result was found)
          '''
          
          ##
          try:
            table_aod = jjinput
            vout = [row for row in table_aod if(row[fieldname])==fieldvalue]
            vout = vout[iirec]
          except Exception as msg:
            vout = '__blank__'
            #print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            #exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            #print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        
        def jjaod_select(self,jjinput,fieldname='fname'):
          '''
          ## function docs
          - caption:  jjaod_select
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  data
            grp_med:  array_of_dictionary
            grp_min:  select
            desc:     aod select field
            detail:  |
              aod select values and return list of values
            dependencies:
              - none
            params:
              - param: jjinput    ;; required ;; raw input string
              - param: fieldname  ;; required ;; aod select field
            dreftymacid: bra_bluntly_celt
            output: python list
          '''
          
          ##
          table = jjinput
          ##
          vout = [row[fieldname] for row in table]
          ##
          return vout
        ##enddef
    
        def jjdata_formatas(self,jjinput,sfmt='json'):
          '''
          ## function docs
          - caption:  jjdata_formatas
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  data
            grp_med:  transform
            grp_min:  reformat
            desc:     reformat arbitrary data structures
            detail:  |
              * process input data and dump it out to another format
              * seealso
                  * href="../../../../../appdata/home/smosley/.dreftymac/py/datadump_formatas.py" find="lookfor"
                  * href="../../../../../mytrybits/y/tryyaml/dynamicyaml/app/demo/demo.dataformatas.txt"
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          ## init lib
          import json
          import yaml
          
          ## init vars
          vout          = jjinput
          ddtransform   = {}
          
          ## init yaml
          if(sfmt=='yamlpretty'):
            ## see also (regain://listener_faze_whenever)
            yaml.representer.BaseRepresenter.represent_scalar = DerivedBaseRepresenter().yaml_addon_represent_scalar
    
          ## init transform engines
          ddtransform['yaml']        = lambda vxx: yaml.safe_dump(vxx)
          ddtransform['yamlblock']   = lambda vxx: yaml.safe_dump(vxx
                                                                 ,default_flow_style=True
                                                                 )
          ddtransform['yamlfold']   = lambda vxx: yaml.safe_dump(vxx
                                                                 ,default_style='|'
                                                                 )
          ddtransform['yamlpara']   = lambda vxx: yaml.safe_dump(vxx
                                                                 ,default_flow_style=False
                                                                 )
          ddtransform['yamlpretty'] = lambda vxx: yaml.safe_dump(vxx, default_flow_style=False)
          ddtransform['json']       = lambda vxx: json.dumps(vxx)
          ddtransform['jsonpretty'] = lambda vxx: json.dumps(vxx
                                                             ,sort_keys = True
                                                             ,indent = 2
                                                             ,separators  =(',', ': ')
                                                             )
          ##
          try:
            vout = ddtransform[sfmt](vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjchr(self,jjinput):
          '''
          ### ##beg_func_docs
          ### - caption:  __caption__
          ###   date:         lastmod="__lastmod__"
          ###   grp_maj:      grp_maj
          ###   grp_med:      grp_med
          ###   grp_min:      grp_min
          ###   desc:         __desc__
          ###   dreftymacid:  __dreftymacid__
          ###   detail:  |
          ###     * http://code.activestate.com/recipes/65117-converting-between-ascii-numbers-and-characters/
          ###   dependencies:
          ###     - __blank__
          ###   params:
          ###    - param: jjinput ;; optarity ;; placedholder arg for jinja raw input string
          ### ##end_func_docs
          '''

          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = chr(int(vout))
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
          ##
          return vout          
        ##enddef
    
        def jjdate_get(self,jjinput,getwhat='year'):
          '''
          ## function docs
          - caption:  jjdate_get
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  datetime
            grp_med:  output
            grp_min:  current
            desc:     get date components for current localtime
            detail:  |
              output the current date value for a specific date component
              supported date components:
                - 'year'
                - 'month'
                - 'day'
                - 'hour'
                - 'minute'
                - 'second'
                - 'week'
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            now   =   datetime.datetime.now()
            if(getwhat.lower()=='year'):
              vout  =   "%04d" % getattr(now,getwhat)
            if(getwhat.lower()=='month'):
              vout  =   "%02d" % getattr(now,getwhat)
            if(getwhat.lower()=='day'):
              vout  =   "%02d" % getattr(now,getwhat)
            if(getwhat.lower()=='hour'):
              vout  =   "%02d" % getattr(now,getwhat)
            if(getwhat.lower()=='minute'):
              vout  =   "%02d" % getattr(now,getwhat)
            if(getwhat.lower()=='second'):
              vout  =   "%02d" % getattr(now,getwhat)
            if(getwhat.lower()=='week'):
              vout  = "%02d" % (datetime.date(now.year, now.month, now.day).isocalendar()[1]-1)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjdate_now(self,jjinput,sfmt=''):
          '''
          ## function docs
          - caption:  jjdate_now
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  datetime
            grp_med:  output
            grp_min:  current
            desc:     get current localtime
            detail:  |
              output the current date
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        
        def jjdec64(self,jjinput):
          '''
          ## function docs
          - caption:  jjdec64
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  codec
            grp_med:  base64
            grp_min:  decode
            desc:     base64 decode
            detail:  |
              base64 decode
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          ##
          vout  =   base64.b64decode(jjinput.__str__())
          ##
          return vout
        ##enddef
        
        def jjenc64(self,jjinput):
          '''
          ## function docs
          - caption:  jjenc64
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  codec
            grp_med:  base64
            grp_min:  encode
            desc:     base64 encode
            detail:  |
              base64 encode
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          ##
          vout  =   base64.b64encode(jjinput.__str__())
          ##
          return vout
        ##enddef
    
        def jjdedent(self,jjinput):
          '''
          ## function docs
          - caption:  jjdedent
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  string_transform
            grp_med:  whitespace
            grp_min:  dedent
            desc:     textrap dedent
            detail:  |
              textrap dedent
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: rebuilt_lever_chariot
          '''
          ##
          vout = textwrap.dedent(jjinput.__str__())
          ##
          return vout
        ##enddef
        
        def jjdubsplit(self,jjinput,spliton=';;',splitget=0):
          '''
          ## function docs
          - caption:  jjdubsplit
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  string_transform
            grp_med:  string
            grp_min:  split
            desc:     string split and return result from split index
            example: |
              {{ "hello;;fancy;;world" |jjdubsplit(';;',0)    }}{#- returns 'hello' -#}
              {{ "hello;;fancy;;world" |jjdubsplit(';;',1)    }}{#- returns 'fancy' -#}
              {{ "hello;;fancy;;world" |jjdubsplit(';;',2)    }}{#- returns 'world' -#}
              {{ "hello;;fancy;;world" |jjdubsplit(';;',-1)   }}{#- returns 'world' -#}
              {{ "hello;;fancy;;world" |jjdubsplit(';;',3)    }}{#- returns ''      -#}
            detail:  |
              * split a string on a delimiter and return the indexed portion
              * uses zero-based index
              * return empty string if there is no match at indexed portion
            dependencies:
              - none
            params:
              - param: jjinput   ;; required ;; raw input string
              - param: spliton   ;; optional ;; string to split on (defaults to double-semicolon)
              - param: splitget  ;; optional ;; extraction index (defaults to zero)
            dreftymacid: zeros_cods_views
          '''
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = vout.split(spliton)
            vout = vout[splitget]
          except Exception as msg:
            vout = ''
            
          ##
          return vout
        ##enddef
    
        def jjfmt(self,jjinput,fmt='{0}',typeof='str'):
          '''
          ## function docs
          - caption:  jjfmt
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  string_transform
            grp_med:  reformat
            grp_min:  sprintf
            desc:     python-specific string sprintf-style format
            detail:  |
              seealso:
              https://docs.python.org/2/library/string.html#formatspec
              href="../py/string_examples.py" find="BarebonesStringFormatExample"
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: merits_axial_extra
          '''
          ##
          vout  = jjinput.__str__()
                
          ##
          try:
            if typeof=='str':
              vout  = fmt.format(str(vout))
            if typeof=='int':
              vout  = fmt.format(int(vout))
            if typeof=='float':
              vout  = fmt.format(float(vout))
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjfromfile(self,jjinput,surl=''):
          '''
          ## function docs
          - caption:  jjfromfile
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  FileIO
            grp_med:  string
            grp_min:  fromfile
            desc: string.fromfile
            detail:  |
              pull in content from a file
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; placeholder argument for jinja
             - param: surl    ;; required ;; file path
            dreftymacid: __blank__
          '''
          ##
          vout  = ''
          #vout  = open(surl,'r').read()
          
          ##
          try:
            ## BUGNAG ;; added encode ascii ignore
            vout  = open(surl,'r').read()
            vout  = vout.decode('utf-8').encode('ascii', 'ignore')
          except Exception as msg:
            print 'UNEXPECTED TERMINATION sharing_client_smearing msg@%s %s'%(msg.__repr__(),surl)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        
        def jjget_basename(self,jjinput):
          '''
          ## ANNOYANCE: this just gives the basename of this current py file
          ## function docs
          - caption:  jjget_basename
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  getinfo
            grp_med:  python
            grp_min:  os.path.basename
            desc: os.path.basename
            detail:  |
              os.path.basename of current file
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; placeholder argument for jinja
            dreftymacid: fuel_cinema_ajax
          '''
          ##
          try:
            ## BUGNAG ;; added encode ascii ignore
            vout  = os.path.basename(os.path.abspath(__file__))
            vout  = vout.split('.')[0:-1]
            vout  = ".".join(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION sharing_client_smearing msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjgreplines(self,jjinput,lookfor=''):
          """
          ## function docs
          - caption:    jjgreplines
            date:       lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string
            grp_med:    process
            grp_min:      __blank__
            dreftymacid:  invoker_panic_inquire
            desc: greplines for occurance of lookfor
            detail: |
              convert string to array and select lines matching lookfor
            dependencies:
              - none
            params:
             - param: jjinput   ;; required ;; input string
             - param: lookfor   ;; optional ;; substring to find
          """
          ##
          vinp = jjinput.splitlines()
          vout = []
          
          ##
          try:
            for line in vinp:
              if(lookfor in line):
                vout.append(line)
            vout = "\n".join(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjhtml_squeeze(self,jjinput):
          """
          ## function docs
          - caption:  jjhtml_squeeze
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string
            grp_med:    process
            grp_min:    __blank__
            dreftymacid:  __blank__
            desc: smush html
            detail: |
              squeeze html
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; placeholder argument for jinja
             - param: __blank__ ;; required ;; __blank__
          """
          ##
          vout  = jjinput.__str__()
          
          ##
          try:
            vout = vout.split("\n")
            vout = "".join(vout)
            #vout = vout.split(' ')
            #vout = "".join(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjhug(self,jjinput,hug='"'):
          """
          ## function docs
          - caption:  jjhug
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    wrap
            grp_min:    balanced delimiters
            dreftymacid:  visuals_sinus_breakage
            desc: string wrap with delims
            detail: |
              string wrap with balanced delimiters
              seealso
              * href="../../../../../mytrybits/r/tryruby/myruby/private/addon/addon.rb" find="hug"
            dependencies:
              - none
            params:
             - param: jjinput   ;; required ;; raw input string
             - param: hug       ;; optional ;; hug-character (default doublequote)
            output: python string
          """
          ##
          vout  = jjinput.__str__()
          aahug = []
          
          ##
          if(hug=='"'): aahug.append('"');aahug.append('"');
          if(hug=="'"): aahug.append("'");aahug.append("'");
          if(hug=="["): aahug.append("[");aahug.append("]");
          if(hug=="]"): aahug.append("[");aahug.append("]");
          if(hug=="<"): aahug.append("<");aahug.append(">");
          if(hug==">"): aahug.append("<");aahug.append(">");
          if(hug=="("): aahug.append("(");aahug.append(")");
          if(hug==")"): aahug.append("(");aahug.append(")");
          if(hug=="{"): aahug.append("{");aahug.append("}");
          if(hug=="}"): aahug.append("{");aahug.append("}");
          
          ##
          try:
            vout = "".join([ aahug[0], vout , aahug[1] ])
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        
        def jjindent(self,jjinput,strlead=' ',imult=2):
          """
          ## function docs
          - caption:  jjindent
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    whitespace
            grp_min:      indent
            dreftymacid:  mustang_gunfire_being
            desc:         string indent
            detail: |
                string indent
                
                NOTE A trick to using this filter, when dealing with a potentially multiline string,
                put a newline before the indent to have all lines show up with a common and uniform indent.
                
                (see href="../../image/mustang_gunfire_being.001.png")
                
            dependencies:
              - import re
            params:
             - param: jjinput   ;; required ;; raw input string
             - param: strlead   ;; optional ;; leading indenter default (single whitespace char)
             - param: imult     ;; optional ;; multiplier for indenter (default 2)
            output: python string
          """
          
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = re.sub(re.compile('^', re.MULTILINE), str(strlead * imult), vout,)
            pass
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
          ##
          return vout
          pass
        ##enddef
    
        def jjlen(self,jjinput):
          """
          ## function docs
          - caption:  jjlen
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    getinfo
            grp_med:
            grp_min:
            dreftymacid:  __blank__
            desc: python len()
            detail: |
              python len() function
              NOTE:
                this is superfluous, you can easily do this in a jinja template
                {%- set mtt_fldcount  = table001_fieldmeta.__len__()    -%}
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
             - param: jjinput ;; optional ;; optional delimiter string
            output: python string
          """
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = len(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjlistget(self,jjinput,index=0):
          """
          ## function docs
          - caption:  jjlistget
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    getinfo
            grp_med:    list
            grp_min:    item
            dreftymacid:  fakery_brats_diets
            desc: try to return list item at index
            detail: |
                __blank__
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; python list
             - param: jjinput ;; optional ;; optional index
            output: python string
          """
          ##
          vout = jjinput
          
          ##
          try:
            vout = jjinput[index]
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjlistjoin(self,jjinput,joinwith=" "):
          """
          ## function docs
          - caption:  jjlistjoin
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    list
            grp_med:    join
            grp_min:    items
            dreftymacid:  vineyard_manly_grouping
            desc: perform join on a list and return a string
            detail: |
                __blank__
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; python list
             - param: joinwith ;; optional ;; join string
            output: python string
          """
          ##
          vout = jjinput
          
          ##
          try:
            vout = joinwith.join(jjinput)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjmarkdown2html(self,jjinput):
          """
          ## function docs
          - caption:  jjmarkdown2html
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:      string_transform
            grp_med:      markup
            grp_min:      convert
            dreftymacid:  grease_style_agnew
            desc: markdown to html
            detail: |
              markdown to html
            dependencies:
              - import markdown
            params:
             - param: jjinput ;; required ;; raw input string
            output: python string
          """
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout  =   textwrap.dedent(vout)
            vout  =   markdown.markdown(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjnewline_erase(self,jjinput):
          """
          ## function docs
          - caption:  jjnewline_erase
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    whitespace
            grp_min:    remove
            dreftymacid:  __blank__
            alias:
              - jjnne
            desc: remove newlines
            detail: |
                __blank__
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            output: python string
          """
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = re.sub("\n", "" , vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        ## alias_definition
        def jjnne(self,jjinput): return self.jjnewline_erase(jjinput)
        ##enddef
    
        def jjnewline_replace(self,jjinput,replacewith="\n"):
          """
          ## function docs
          - caption:  jjnewline_replace
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    whitespace
            grp_min:    modify
            dreftymacid:  gluily_smirky_logan
            alias:
            desc: replace newlines with alternate string
            detail: |
                __blank__
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
             - param: replacewith ;; optional ;; replacement string
            output: python string
          """
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = re.sub("\n", replacewith , vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        ## alias_definition
        ##enddef
    
        def jjpath(self,jjinput,ssmethod='isdir'):
          """
          ## function docs
          - caption:  jjpath_isfile
            date:     lastmod="Mon 2015-06-08 16:06:01"
            grp_maj:      FileIO
            grp_med:      path
            grp_min:      info
            dreftymacid:  drawer_coping_uniplex
            desc: python os.path method call
            alias:
              - __blank__
            detail: |
              reference to all the single-argument method calls of os.path
              seealso:
              * https://docs.python.org/2/library/os.path.html
            dependencies:
              - none
            params:
              - param: jjinput ;; required ;; value evaluated as path
            output: python string
          """
          ##
          vout = jjinput.__str__()
           
          ##
          try:
            vout = getattr(os.path,ssmethod)(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjarray_fromdir(self,jjinput,ssmode='glob',ssfilespec=''):
          """
          ## function docs
          - caption:  jjarray_fromdir
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:      FileIO
            grp_med:      directory
            grp_min:      traverse
            dreftymacid:  pests_cow_vealing
            desc: python  ArrayFromDirectory
            alias:
              - __blank__
            detail: |
              seealso:
              * href="../../../../../mydaydirs/2015/week22/py/oswalk.demo.py"
              return a python list result from os.walk
            dependencies:
              - none
            params:
              - param: jjinput ;; required ;; placeholder argument for jinja
              - param: ssmode ;; required ;; file traversal mode
              - param: ssfilespec ;; required ;; path specification
            output: python string
          """
          ##
          vout = jjinput.__str__()
           
          ##
          try:
            if(ssmode.lower()==''):
              pass
            elif(ssmode.lower()=='glob'):
              aResults    =   glob.glob(ssfilespec)
              aResults    =   [ vxx.replace('\\','/') for vxx in aResults ]
              vout        =   aResults
            elif(ssmode.lower()=='walk' or True):
              vout    = []
              aatemp  =   []
              for root, dirs, files in os.walk(ssfilespec):
                aatemp.extend(  [ "/".join([root,vxx]) for vxx in dirs ] )
              aatemp = [vxx.replace('\\','/') for vxx in aatemp]
              vout = aatemp
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
       
        def jjq2x(self,jjinput):
          """
          ## function docs
          - caption:  jjq2x
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    substitute
            grp_min:    characters
            dreftymacid:  __blank__
            desc: (single-quote) characters to (double-sinqle-quote)
            detail: |
              convert individual single-quote characters to double-sinqle-quote
              for use with sqlite where the text has embedded single-quote-chars
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            output: python string
          """
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = re.sub("'", "''" , vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjregexreplace(self,jjinput,pattern='',replacement='',ignorecase=False):
          '''
          jjregexreplace
          '''
          ##
          vout      =   jjinput.__str__()
          
          ##
          try:
            regex     =   re.compile(pattern)
            vout      =   regex.sub(replacement, vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
          ##
          return vout
        ##enddef

        #@staticmethod
        #def _regex_replace(value='', pattern='', replacement='', ignorecase=False):
        #    if not isinstance(value, six.string_types):
        #        value = str(value)
        #    flags = CustomFilters._get_regex_flags(ignorecase)
        #    regex = re.compile(pattern, flags)
        #    return regex.sub(replacement, value)
    
        def jjregionreplace(self,jjinput,vreplace='',regbeg='',regend='',):
          """
          ## function docs
          - caption:  jjregionreplace
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    replace
            grp_min:    string
            dreftymacid:  found_goliath_loyalty
            desc: replace a subregion of a string with optional balanced delimiters
            detail: |
              ## overview
              replace a subregion of a string with optional balanced delimiters
              ## demo
              regain://untwist_disobey_dolby
              regain://dynamicyaml
            dependencies:
              - import uuid
            params:
             - param: jjinput   ;; required ;; raw input string
             - param: vreplace  ;; optional ;; replacement string
             - param: regbeg    ;; optional ;; delimiter begin string
             - param: regend    ;; optional ;; delimiter end string
            output: python array
          """
          ##
          vorigg  = jjinput.__str__()
          
          ##
          try:
            ## init
            newdelim  =   str(uuid.uuid4())
            ##;;
            
            ## process
            vtempgg     =   vorigg
            if(not regbeg == regend):
              vtempgg     =   vtempgg.replace(regend,regbeg)
            if(not vtempgg == ''):
              vtempgg     =   vtempgg.replace(regbeg,newdelim)
              vtempgg     =   vtempgg.split(newdelim)
              vtempgg[1]  =   "".join([regbeg,vreplace,regend])
              vtempgg     =   "".join(vtempgg)
            ##;;
            
            ##
            vout = vtempgg
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
    
        def jjrequesturl(self,jjinput,sgurl='http://www.example.com',):
          '''
          ## function docs
          - caption:      jjrequesturl
            date:         lastmod="Tue 2015-08-11 16:12:12"
            grp_maj:      webscrape
            grp_med:      request
            grp_min:      url
            dreftymacid:  viperine_dopey_estimate
            desc:         request the content of a URL using python requests module
            detail: |
              ## overview
              request the content of a URL using python requests module
              
              ## demo
              
            dependencies:
              - import requests              
            params:
             - param: jjinput   ;; ignored  ;; placeholder for raw input string
             - param: url       ;; optional ;; url defaults to example.com
            output: python array
          '''
          ##
          vout      =   ''
          
          ##
          try:
              ## init_content
              ## sgurl       =   "http://ba.uoregon.edu/staff/business-expense-policies"
              vout        =   requests.get(sgurl).text.encode('ascii', 'ignore')
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
          ##
          return vout
        ##enddef    
    
        def jjsplit(self,jjinput,sdelim=';;'):
          """
          ## function docs
          - caption:  jjsplit
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    cast
            grp_min:    array
            dreftymacid:  __blank__
            desc: return string.split(delim)
            detail: |
              split string on sdelim and return python list
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
             - param: sdelim  ;; optional ;; optional delimiter string (default ';;')
            output: python array
          """
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = vout.split(sdelim)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        
        def jjsplit_re(self,jjinput,regex='\w'):
          """
          ## function docs
          - caption:  jjsplit_re
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    cast
            grp_min:    array
            dreftymacid:  coping_inch_wreathe
            desc: return re.split(regex)
            detail: |
              split string on regex and return python list
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
             - param: regex  ;; optional ;; optional delimiter string (default '\w')
            output: python array
          """
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            vout = re.split(regex,vout)
            pass
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        
        def jjslashdouble(self,jjinput):
          """
          ## function docs
          - caption:      jjslashdouble
            date:         lastmod="20150624.1803"
            grp_maj:      string_transform
            grp_med:      slashes
            grp_min:      doublebackslash
            dreftymacid:  fix_pivots_dialog
            alias:
              - jjsldub
            detail: |
              change all slashes to double backslash
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
          """
          ##
          try:
            vout = jjinput.__str__().replace("\x2f",'\\'+'\\')
            vout = jjinput.__str__().replace("\x5c",'\\'+'\\')
            #vout = "\\\\".join(vout)
            #vout = jjinput.__str__().split('\\')
            #vout = "\\\\".join(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        ## alias_definition
        def jjsldub(self,jjinput): return self.jjslashdouble(jjinput)
        ##enddef
        
        def jjslashback(self,jjinput):
          """
          ## function docs
          - caption:  jjslashback
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    slashes
            grp_min:    back
            dreftymacid:  __blank__
            alias:
              - jjslb
            detail: |
              change all slashes to back slash
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
          """
          ##
          try:
            vout = jjinput.__str__().split('/')
            vout = "\\".join(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        ## alias_definition
        def jjslb(self,jjinput): return self.jjslashback(jjinput)
        ##enddef
        
        def jjslashforward(self,jjinput):
          """
          ## function docs
          - caption:  jjslashforward
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    slashes
            grp_min:    forward
            dreftymacid:  __blank__
            alias:
              - jjslf
            detail: |
              change all slashes to forward slash
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
          """
          ##
          try:
            vout = jjinput.__str__().split('\\')
            vout = "/".join(vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        ## alias_definition
        def jjslf(self,jjinput): return self.jjslashforward(jjinput)
        ##enddef
        
        def jjsplitlines(self,jjinput):
          """
          ## function docs
          - caption:  jjsplitlines
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_convert
            grp_med:    splitlines
            grp_min:
            dreftymacid:  analysts_gust_cruncher
            alias:
            detail: |
              return a list of splitlines
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
          """
          ##
          try:
            vout = jjinput.splitlines()
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
        ## alias_definition
        ##enddef
    
        def jjtodir(self,jjinput,outpath=''):
          '''
          ## function docs
          - caption:  jjtodir
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    FileIO
            grp_med:    create
            grp_min:    directory
            dreftymacid:  glucose_visual_unweave
            tags: directory, fileio
            desc: output a directory
            detail: |
              output to a directory
            dependencies:
              - none
            params:
             - param: jjinput ;; optional ;; raw input string
             - param: outpath ;; optional ;; output path for directory
          '''
          ##
          vout = jjinput.__str__()
          
          ##
          try:
            #print(os.path.exists(outpath))
            ##
            if( outpath == ''):
              vout = vout ## just return jjinput and do not try to write to file
            ##
            elif( not outpath == '' ):
              outpath = outpath + '/' ## ensure a trailing slash so python knows we want a directory
              if( not os.path.exists(os.path.dirname(outpath)) ):
                os.makedirs( os.path.dirname(outpath) )
              #oFile = open(outpath,'wb')
              #oFile.write(vout)
              #oFile.close();
              vout = outpath;
              vout = "\n## create directory %s"%(vout)
          except Exception as msg:
            pass
            #print 'UNEXPECTED TERMINATION gadgets_busby_damply msg@%s'%(msg.__repr__())
            #exc_type, exc_obj, exc_tb = sys.exc_info()
            #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            #print(exc_type, fname, exc_tb.tb_lineno)
            
          ##
          return vout
        ##enddef
    
        def jjtofile(self,jjinput,outpath='',writemode='create',usebom=False):
          '''
          ## function docs
          - caption:  jjtofile
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    FileIO
            grp_med:    __blank__
            grp_min:    __blank__
            dreftymacid:  youngest_drail_roaming
            tags: stringtofile, stringtofilebom
            example: |
              {%filter jjtofile('./hello.txt','create',False)%}hello world!!!{%endfilter%}
            desc: output to a file
            detail: |
              writemode
              =========
              * create    ;; only write if file does not already exist
              * replace   ;; overwrite any existing file if it already exists
              * append    ;; create file if not exist, append if already exists
              
            dependencies:
              - none
            params:
              - param: jjinput    ;; required ;; raw input string
              - param: outpath    ;; optional ;; output path for file
              - param: writemode  ;; optional ;; output writemode (create|replace|append)
              - param: usebom     ;; optional ;; true/false write unicode BOM
          '''
          ##
          vbody = jjinput.__str__()
          vout  = ''
          bwrite = True
          
          ##
          try:
            ## outpath is empty
            if( outpath == ''):
              vout = vout ## just return jjinput and do not try to write to file
              
            ## outpath is nonempty
            elif( not outpath == '' ):
              pymode = 'wb'
              
              ## mkdir-p
              if( not os.path.exists(os.path.dirname(outpath)) ):
                os.makedirs( os.path.dirname(outpath) )
              ##---
                        
              ## check writemode
              if( (os.path.isfile(outpath)) and (writemode=='create') ):
                pymode  = ''
                vout    = outpath;
                vout    = "\nfailed to write output file %s (already exists?)"%(vout)
              ##
              elif( (os.path.isfile(outpath)) and (writemode=='replace') ):
                pymode  = 'wb'
                vout    = outpath;
                vout    = "\noutput file %s"%(vout)
              ##
              elif( (os.path.isfile(outpath)) and (writemode=='append') ):
                pymode  = 'ab'
                vout    = outpath;
                vout    = "\nappend file %s"%(vout)
              ##---
              
              #print writemode
              #print outpath
              #print pymode
              
              ## process
              if( not pymode == '' ):
                oFile = open(outpath,pymode)
                if(usebom==True):
                  oFile.write(codecs.BOM_UTF8)
                oFile.write(vbody.encode(encoding='UTF-8',errors='strict'))
                oFile.close();
                vout = outpath;
                vout = "\n## output file %s"%(vout)
              elif(True):
                vout = outpath;
                vout = "\n## failed to write output file %s (already exists?)"%(vout)
              ##---
              
          except Exception as msg:
            pass
            print 'UNEXPECTED TERMINATION gadgets_busby_damply msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
          ##
          return vout
        ##enddef
                
        def jjtozipfile(self,jjinput,zipfilepath='ddyaml_output',archivpath='',stamp=''):
          '''
          ## function docs
          - caption:  jjtozipfile
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  FileIO
            grp_med:  output
            grp_min:  zipfile
            dreftymacid: mckay_planets_richer
            detail:  |
                output to a zip archive
            dependencies:
                - import zipfile
                - import time
            params:
                - param: jjinput      ;;  required  ;;  raw input string
                - param: zipfilepath  ;;  optional  ;;  output path for zipfile
                - param: archivpath   ;;  optional  ;;  output path internally stored zipfile
          '''
          ##
          vout = jjinput.__str__()
          if(zipfilepath == ''): zipfilepath = 'ddyaml_output'
          
          ##
          zipmode     =   None
          wrtmode     =   'a'
          ssfzipout   =   '%s%s.zip'%(zipfilepath,stamp)
          
          ##
          try:
              import zlib
              zipmode= zipfile.ZIP_DEFLATED
          except:
              zipmode= zipfile.ZIP_STORED
              
          ##
          ##
          try:
            #print(os.path.exists(outpath))
            oZip = zipfile.ZipFile(ssfzipout,
                                 mode=wrtmode,
                                 compression=zipmode,
                                 )
            oZip.writestr(archivpath, vout)
            vout = "## jjtozipfile %s"%(archivpath);
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            vout = (exc_type, fname, exc_tb.tb_lineno)
            print vout
          ##
          return vout
        ##enddef
    
        def jjucfirst(self,jjinput):
          '''
          ## function docs
          - caption:  jjucfirst
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  string_transform
            grp_med:  change_case
            grp_min:  uppercase first character
            detail:  |
              uppercase first character
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          ##
          vinn      = jjinput.__str__()
          
          ##
          vtokens   = re.split('(\W)', vinn)
          
          ##
          vtokens   =   [
            (str(item)[0].upper() + str(item)[1:])
              if
                (item.strip()!='')
              else
                (item)
            for item in vtokens
            ]
          
          ##
          vout      =   "".join(vtokens)
          
          ##
          return vout
        ##enddef
            
        def jjuuid(self,jjinput,enum=0):
          '''
          ## function docs
          - caption:  jjuuid
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  string.generate
            grp_med:  __blank__
            grp_min:  __blank__
            dreftymacid: radius_disliker_empty
            detail:  |
              fake pseudo-uuid timestamp-based
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; placeholder argument for jinja
             - param: enum ;; optional ;; add on additional enumeration component
            dreftymacid: __blank__
          '''
    
          ##
          try:
            vout  = []
            vout.append(time.strftime("%Y%m%d"))
            vout.append(time.strftime("%H%M%S"))
            if(enum == 0):
              vout.append("%05d"%random.randint(0,99999))
            else:
              vout.append("%05d"%enum)
            vout    = "-".join(vout)
            return vout
            pass;
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef
      ##endclass
###!}}}

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
###!  		* __blank__
###!  desc: |
###!  		__desc__
###!  wwbody: |
      class DynamicYAML(object):
        def __init__(self,ffpath):
          ##
          self.Environment  =   jinja2.Environment(extensions=['jinja2.ext.do'])
          self.oenv         =   self.Environment
          self.ffpath_main  =   ffpath
          self.ffpath_abso  =   "/".join( os.path.abspath(ffpath).split("\\") )
          self.ffpath_pdir  =   "/".join( os.path.dirname(self.ffpath_abso).split("\\") )
          #oDumper.pprint( self.ffpath_abso )
          #oDumper.pprint( self.ffpath_pdir )
        ##enddef
        
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
          """
          return dict(py_mergedict(ob001,ob002))
        ##enddef
        
        def ff_resolvepath_read(self,spath):
          '''
          ### main:
          ###   - date: created="Thu Jul 16 15:30:22 2015"
          ###     desc:	read a file with path that is potentially relative to path of orgconf_raw
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
          ## check if spath is readable as relative to path of orgconf_raw
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
        
          ## get original_config_file (dynamic_yaml)
          vout          =   []
          ssgpath       =   ''
          try:
            ##ssgpath       =   sys.argv[1]
            ssgpath       =   self.ffpath_main
          except Exception:
            return ''
            pass
          orgconf_raw   =   open(ssgpath,'rb').read()
          orgconf       =   yaml.safe_load(orgconf_raw)
          ##;;
                  
          ## init directives_dictionary
          directives = {}
          directives['default_data']        = ''
          directives['default_template']    = ''
          directives['current_data']        = ''
          directives['current_template']    = ''
          ##;;
          
          ## set defaults on directives_dictionary
          ##    from the original_config_file
          ##    preserve every existing key, except remove the sgg_dynamicyaml_key
          directives['default_data']    = orgconf.copy()
          del(directives['default_data'][sgg_dynamicyaml_key])
          ##;;
          
          ## set default_template
          ##    use this as the default template if one not specified
          directives['default_template']      = orgconf_raw
          ##;;
          
          ## iterate_yaml
          for row in orgconf[sgg_dynamicyaml_key]:
            directives['current_template']    = directives['default_template']
            directives['current_data']        = directives['default_data']
            
            ### ********************
            ## process row
            
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
            
            ## @@@ templatefile directive ;; we get a template from an external included file
            tmpname = ['template','file']
            tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
            if( (tmpkey) in row ):
              tmpval = row[tmpkey]
              directives['current_'+tmpname[0]]   =   textwrap.dedent(open(tmpval,'rb').read())
              ## print tmpval
            ##;;
            
            ## @@@ template directive ;; we get template from original_config_file
            tmpname = ['template','']
            tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
            if( (tmpkey) in row ):
              tmpval = row[tmpkey]
              directives['current_'+tmpname[0]]   =   textwrap.dedent(tmpval)
              ## print tmpval
            ##;;
            
            ## @@@ includefile directive ;; allows template or templatefile to include content from other files
            ## and merge it with the data in the original_config_file
            tmpname = ['include','file']
            tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
            if( (tmpkey) in row ):
              tmpval = row[tmpkey]
              ## iterate includes (can be either scalar or list)
              sstemp  = ''
              if(  type(tmpval) == str ):
                tmpval = [tmpval]
              for spath in tmpval:
                sstemp += open(spath,'rb').read()
              ##
              directives['current_'+tmpname[0]] = sstemp
              ## print tmpval
            ##;;
  
            ## @@@ datafile directive ;; concatenate multiple yaml files to input additional data
            ## and merge it with the data in the original_config_file
            tmpname =   ['data','file']
            tmpkey  =   sgg_directiveprefix_str + "".join(tmpname)
            if( (tmpkey) in row ):
              tmpval = row[tmpkey]
              
              #oDumper.pprint( directives['current_'+tmpname[0]] )
              #oDumper.pprint( tmpval )
              
              ## iterate includes (can be either scalar or list)
              sstemp = ''
              if(tmpval is None):
                tmpval = ''
              if(  type(tmpval) == str ):
                tmpval = [tmpval]     ## force scalar to list
                
              ## iterate list
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
            
            ## @@@ data directive ;; we get data from original_config_file
            tmpname = ['data','']
            tmpkey  = sgg_directiveprefix_str + "".join(tmpname)
            #print row
            if( (tmpkey) in row ):
              tmpval = row[tmpkey]
              directives['current_'+tmpname[0]]   =   yaml.safe_load(tmpval)
            ##;;
            
            ## preproc directives
            if('current_include' in directives):
              directives['current_template'] = directives['current_include'] + directives['current_template']
            
            ## render output
            otemplate_data  =   self.data_struct_merge(directives['default_data'],directives['current_data'])
            template        =   oEnv.from_string(textwrap.dedent(directives['current_template']).encode('ascii', 'ignore'))
            tmpout          =   template.render(otemplate_data)
            ## force unix line endings
            if(True):
              tmpout = string.replace(tmpout, '\r\n', '')
              tmpout = string.replace(tmpout, '\r', '')
            vout.append( tmpout )
            
            ## print tmpout
            #oDumper.pprint( otemplate_data )
            #print( directives['current_template'] )
            
            ## postproc directives
            try:
              if('current_outputfile' in directives):
                spath = directives['current_outputfile']
                open(spath,'w').write(tmpout)
            except Exception as msg:
                print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
              #print(exc_type, fname, exc_tb.tb_lineno)
            ##;;
            
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
