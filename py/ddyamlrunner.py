# -*- coding: utf-8 -*-
### <beg-file_info>
### main:
###   - date: created="Wed Dec 30 12:53:38 2015"
###     last: lastmod="Wed Dec 30 12:53:38 2015"
###     tags: tags
###     author: created="dreftymac"
###     dreftymacid: "drawing_verlaine_neck"
###     seealso: |
###         * href="smartpath://mytrybits/p/trypython2/lab2014/pyjinja/dynamic_yaml.py"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml.py"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/dynamicyaml/dynamicyaml.py"
###     desc: |
###         desc
### <end-file_info>

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
    
      ## init py
      from bs4 import BeautifulSoup
      import pprint
      oDumper = pprint.PrettyPrinter(indent=4);      

      ## local import
      from DDYAML  import  DynamicYAML                 ## href="./DDYAML/DynamicYAML.py"
      from DDYAML  import  JinjaFilterBase             ## href="./DDYAML/JinjaFilterBase.py"
      from DDYAML  import  JinjaFilterDynamicYAML      ## href="./DDYAML/JinjaFilterDynamicYAML.py"
      from DDYAML  import  YamlDerivedBaseRepresenter  ## href="./DDYAML/YamlDerivedBaseRepresenter.py"
      from DDYAML  import  DataHelperUtils             ## href="./DDYAML/DataHelperUtils.py"
      from DDYAML  import  XmlssBase                   ## href="./DDYAML/XmlssBase.py"
      #print sys.path
###!}}}

### <beg-region_testiff_20151230125723>
###!- caption:  __caption__
###!  date:     created="Wed Dec 30 12:57:23 2015"
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
###!  dreftymacid: uhuru_vagrant_means
###!  body: |
      if (__name__ == "__main__"):
        ##
        vout    =   ''
        ffpath  =   "c:/sm/docs/mymedia/2014/git/github/dynamic.yaml/app/demo/barebones.helloworld.yaml.txt"
        ffpath  =   "c:/sm/docs/mymedia/2014/git/github/dynamic.yaml/app/demo/demo.topic.excel.txt"
        aaJinjaAddonFilters = [
          JinjaFilterDynamicYAML(),
        ]
        oparams = {}
        oparams['path']         = ffpath
        oparams['addonFilters'] = aaJinjaAddonFilters
        ##
        odyna   =   DynamicYAML(oparams)
        vout    =   odyna.ddtransform()
        print vout.encode('utf-8','replace')
### <end-region_testiff_20151230125723>
