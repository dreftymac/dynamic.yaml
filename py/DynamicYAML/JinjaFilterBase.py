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
      #from DynamicYAML import JinjaFilterDynamicYAML
      from TymacUtils import DataHelperUtils
      from TymacUtils import XmlssBase      

      print DynamicYAML
      exit()

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### JinjaFilterBase
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
###!          * __blank__
###!  desc: |
###!          __desc__
###!
###!
###!  dreftymacid: __dreftymacid__
###!  wwbody: |
      class JinjaFilterBase(object):
        """
        Abstract Class for wrapping Jinja Custom Filters
        """

        def yaml_function_docs(self,filterfor=''):
          '''
          ## function docs
          - caption:  yaml_function_docs
            date:     lastmod="Mon 2014-10-20 16:45:46"
            desc:     produce the function docs for this module as yaml
          '''
          #vout = [str(getattr(self,vxx).__doc__) for vxx in dir(self) if(getattr(self,vxx).__doc__)and(vxx != '__module__')and(vxx != '__doc__') ]
          vout = [str(getattr(self,vxx).__doc__) for vxx in dir(self) if(str(vxx) != '' and str(vxx) != 'None' ) ]
          if(str(filterfor!='') and str(filterfor!='None')):
            vout = [item for item in vout if(filterfor in item)]
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
                current naming convention requires the filter
                function name to start with 'double letter j'
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
             - param: vstr ;; required ;; raw input string
            dreftymacid: __blank__
          '''
          vout = ''
          vout = re.sub('fqq','filter',vstr)
          ##
          return vout
        ##enddef
      ##endclass
###!}}}
