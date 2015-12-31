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
### YamlYamlDerivedBaseRepresenter
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
###!          * __blank__
###!  desc: |
###!          __desc__
###!
###!
###!  dreftymacid: granular_ever_milt
###!  wwbody: |
      class YamlDerivedBaseRepresenter(yaml.representer.BaseRepresenter):

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
