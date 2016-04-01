# -*- coding: utf-8 -*-
### <beg-file_info>
### main:
###   - date: created="Mon Jan 25 08:09:56 2016"
###     last: lastmod="Mon Jan 25 08:09:56 2016"
###     tags: python, jinja, filter
###     dreftymacid: "dads_policy_divorce"
###     filetype: "py"
###     seealso: |
###         *
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
  import itertools
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
  import urllib2
  import uuid
  import xlrd
  import yaml
  import zipfile

  ##
  from JinjaFilterBase import JinjaFilterBase
  from DataHelperUtils import DataHelperUtils
  from DataHelperDiceware import DataHelperDiceware
  from YamlDerivedBaseRepresenter import YamlDerivedBaseRepresenter

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### new_function_snippet
"""
        def __caption__(self,jjinput):
          '''
          ##beg_func_docs
          - caption:      __caption__
            date:         lastmod="__lastmod__"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         __desc__
            dreftymacid:  __dreftymacid__
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vout = jjinput.__str__()

          ##
          try:
            vout = vout
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef
"""

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
###!          * __blank__
###!  desc: |
###!          Currently assumes jinja2 as the templating engine for ddyaml
###!          TODO ;; extract out the 'subtopic' filters (like imacros) into different JinjaFilter files
###!
###!
###!
###!  wwbody: |
      class JinjaFilterDynamicYAML(JinjaFilterBase):

        ##
        ## __init__ class initialize
        ##

        ##
        def __init__(self,ddparams={}):
          ## init
          self.externalVars    =   {}
          if 'externalVars' in ddparams.keys():
            for key in ddparams.keys():
              self.externalVars[key] = ddparams['externalVars'][key]
          ##;;
        ##enddef

        ##
        ## CustomAddons ;; context_specific
        ##

        ### ------------------------------------------------------------------------
        ### begin_: pillow_specific

        def jjp_imagetopdf(self,jjinput,sgfilein='',sgfileout=''):
          '''
          ##TODO move this out to pillow_specific, for now included here for deadlines

          ##beg_func_docs
          - caption:      jjp_imagetopdf
            date:         lastmod="2015.08.05.1807"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         __desc__
            dreftymacid:  irish_legality_blitz
            detail:  |
              __detail__
            dependencies:
              -     from PIL import Image, ImageDraw, ImageFilter
              -     import pyscreenshot as ImageGrab
            params:
             - param: jjinput   ;; ignored  ;; placedholder for jinja raw input string
             - param: sgfilein  ;; required ;; input image file
             - param: sgfileout ;; required ;; output pdf file
          ##end_func_docs
          '''

          ##
          try:
            ## open the image file in RGB format, this is important if we miss
            ## convert it wont take the color(RGB) parameter and error will be thrown
            im = Image.open(sgfilein).convert('RGB')
            im.save(sgfileout, "PDF", resolution=100.0)
            vout = sgfileout
          except Exception as msg:
            vout = '__blank__'
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        ### ------------------------------------------------------------------------
        ### begin_: drupal_specific

        ##
        def jjd_alias(self,jjinput):
          '''
          #* href="c:/sm/docs/mymedia/2014/git/github/dynamic.yaml/py/ddyaml.py" find="jjd_alias"
          #* regain://murky_frosts_farms
          #* {{ ttsiteroot }}/admin/config/search/path/settings :: Strings to Remove
          #
          #TODO move this out to drupal specific, for now included here for deadlines
          #drupal URL aliases settings
          #
          #MAKE SURE YOUR REMOVALS MATCH: compare this with
          #    {{ ttsiteroot }}/admin/config/search/path/settings
          #    https://businessgrp1-stage.uoregon.edu/admin/config/search/path/settings

          ##beg_func_docs
          - caption:      jjd_alias
            date:         lastmod="20150904.1651"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         mimic the functionality of drupal's pathauto noise-word removal
            dreftymacid:  radius_symbolic_gerald
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''
          ##
          vout = jjinput.__str__()
          rrdict      = {}
          rrcurr      = 'bastage'
          rrdict['bastage'] =  [vxx.strip() for vxx in '''a, an, as, at, but, by, is, in, into, off, onto, per, since, the, this, that, up, via'''.split(',')]
          removals          = rrdict[rrcurr]
          ##
          vout = vout.lower()
          vout = re.sub(r'[-]+',' ',vout)
          vout = re.sub(r'[^\w\s]+','',vout)
          #vout = re.sub(r'[\s]+','-',vout)
          vout = vout.split(' ')
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
          - caption:  jji_scripthead
            date:         lastmod="2015.08.05.1807"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         __desc__
            dreftymacid:  surf_thuds_rhythm
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
              context:        iim script that outputs code potentially containing angularjs (or any double-curly-brace syntax)
              problem:        both NG and IIM use `{{ }}` for variable placeholders
              solution:       in the output template, use jji_scripthead() which sets !VAR1 and !VAR2 to be equal to '{{' and '}}' respectively
              rationale:      prevents IIM from trying to consume the NG placeholders
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

        def jjstr_rstrip(self,jjinput,chars=''):
          '''
          ##beg_func_docs
          - caption:      jjstr_rstrip
            date:         lastmod="2016-03-25T15:12:09"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc: >
              python str.rstrip([chars]) method
            dreftymacid:  mining_petrify_soloing
            seealso:
              - href="https://docs.python.org/2/library/stdtypes.html#str.rstrip"
            example: |
            detail:  >
              Return a copy of the string with trailing characters removed.
              The chars argument is a string specifying the set of characters
              to be removed.
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; required ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vout = jjinput.__str__()

          ##
          try:
            if(not chars == ''):
              vout = vout.rstrip(chars)
            if(chars == ''):
              vout = vout.rstrip()
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        ## TODO ;; formalize this function and docs
        def jjos_hostname(self,jjinput):
          vout = platform.system()
          return vout
        ##enddef
        ## TODO ;; formalize this function and docs
        def jjos_platform(self,jjinput):
          vout = platform.system()
          return vout
        ##enddef
        
        ## import socket
        ## print(socket.gethostname())
        ## alias_definition
        def jjos_hostname(self,jjinput): return self.jjos_platform(jjinput)
        ##enddef        

        def jjscalarize(self,jjinput,myvar=None):
          '''
          ##beg_func_docs
          - caption:      jjscalarize
            date:         lastmod="20160205"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc: |
              * return a normalized version of a var
              * normalize to scalar
            dreftymacid:  uptown_undoer_vagrancy
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vout = jjinput
          if vout is None:            vout = ''
          elif type(vout) is list:    vout = "".join([vxx.__str__() for vxx in vout])

          ##
          try:
            vout = vout
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef
        ## alias_definition
        def jjscala(self,jjinput): return self.jjscalarize(jjinput,myvar=None)
        ##enddef

        def jjget_var(self,jjinput,varname=''):
          '''
          ##beg_func_docs
          - caption:      jjget_var
            date:         lastmod="2016-01-22T16:11:32"
            grp_maj:      variable
            grp_med:      get
            grp_min:      external
            desc:         get an external variable from the externalVars setting
            dreftymacid:  janis_beanie_altruist
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          if (jjinput.__str__() != ''):
            mykey = jjinput.__str__()
          if (varname.__str__() != ''):
            mykey = varname.__str__()
          ##;;

          ##
          try:
            vout = self.externalVars[mykey]
          ##
          except Exception as msg:
            vout = ''
            # print 'EXCEPTION janis_beanie_altruist msg@%s'%(msg.__repr__())
            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # print(exc_type, fname, exc_tb.tb_lineno)
            pass

          ##
          return vout
        ##enddef

        ##
        def jjapplyfunction(self,jjinput,jjfunc='lambda vxx: vxx',jjdatt=''):
          '''
          ##beg_func_docs
          - caption:      jjapplyfunction
            date:         lastmod="Wed Dec 23 06:29:25 2015"
            grp_maj:      jinja
            grp_med:      filter
            grp_min:      addon
            desc:         __desc__
            dreftymacid:  pets_marvel_dave
            example: |
              * demo01.jjapplyfunction01.txt::pets_marvel_dave
            seealso:
              - href="http://stackoverflow.com/questions/12655155/jinja2-for-loop-with-conditions"
              - href="smartpath://mymedia/2014/git/github/dynamic.yaml/app/demo/demo01.jjapplyfunction01.txt"
              - href="smartpath://mytrybits/m/trymyclip/github_symlink/myclip/publiclab/pythonallgeneral.txt" find="uureload_holocopy_001"
            detail:  |
              * NOTE: need to make this a security-sensitive function that can be turned off
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
             - param: jjdatt ;; optarity ;; data to operate on
             - param: jjfunc ;; optarity ;; function to apply
          ##end_func_docs
          '''

          ##
          vout  = ''
          if(jjinput):
            jjdatt  =  jjinput

          ##
          try:
            ## BUGNAG ;; ANNOYANCE ;; SECURITY ;; string-eval
            jjfunc =  eval(jjfunc)
            vout   =  jjfunc(jjdatt)
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION pets_marvel_dave msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        def jjaod_tocsv(self,jjinput,delim="|"):
          '''
          ##beg_func_docs
          - caption:      jjaod_tocsv
            date:         lastmod="20151016.0745"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         python aod to csv string
            dreftymacid:  ranch_oilier_bulb
            detail:  |
              * convert python aod to csv string
            dependencies:
              - import csv
              - import StringIO
            params:
             - param: jjinput ;; required ;; python array_of_dictionary
             - param: delim   ;; optional ;; string delimiter defaults to pipe char "|"
          ##end_func_docs
          '''

          ##
          odata = jjinput
          vout  = ''

          ##
          try:
            ##
            headers =   odata[0].keys()
            rows    =   odata
            for row in rows:
              for key in row:
                if type(row[key])==str:
                  row[key] = row[key].replace("\n",' ')

            ##
            output = StringIO.StringIO()
            f_csv = csv.DictWriter(output, headers, delimiter=delim, lineterminator="\n")
            f_csv.writeheader()
            f_csv.writerows(rows)
            vout = output.getvalue()
            output.close()

            return vout
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

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
                * aod select record where `fieldname` == `fieldvalue`
                * the return result may consist of more than one record
                * iirec is used to specify which matching record is obtained from the return result
                * iirec is zero-based
            dependencies:
              - none
            example:  |
                {%- set iirec         =  0  -%}
                {%- set mydatarec     =  usertable |jjaod_getrecord('sex','female',iirec) -%}
            params:
              - param: jjinput    ;; required ;; python table_aod
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
                aod select single column from aod
            dependencies:
              - none
            example:  |
                {%- set iirec         =  0  -%}
                {%- set mydatarec     =  usertable |jjaod_getrecord('sex','female',iirec) -%}
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

        ##
        def jjdata_diceword(self,jjinput,ilen=3,ssepa='_'):
          '''
          ##beg_func_docs
          - caption:      jjdata_diceword
            date:         lastmod="2015-12-31T08:55:49"
            grp_maj:      data
            grp_med:      generate
            grp_min:      diceword
            desc:         __desc__
            dreftymacid:  flyer_afield_zealand
            detail:  |
              * ANNOYANCE ;; this function does not appear to return a new value per-loop-iteration
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vout = ''
          vout = jjinput.__str__()

          ##
          try:
            odatt = DataHelperDiceware()
            vout  = odatt.get_ngram(ilen,ssepa) + str(vout)
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION flyer_afield_zealand msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

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
                  * href="smartpath://appdata/home/smosley/.dreftymac/py/datadump_formatas.py" find="lookfor"
                  * href="smartpath://mytrybits/y/tryyaml/dynamicyaml/app/demo/demo.dataformatas.txt"
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; raw input string
            dreftymacid: soil_kicks_torch
          '''
          ## init lib
          import json
          import yaml

          ## init vars
          vout          = jjinput
          mytransform   = {}

          ## init yaml
          if(sfmt=='yamlpretty'):
            ## see also (regain://listener_faze_whenever)
            yaml.representer.BaseRepresenter.represent_scalar = YamlDerivedBaseRepresenter().yaml_addon_represent_scalar

          ## init transform engines
          mytransform['yaml']        = lambda vxx: yaml.safe_dump(vxx)
          mytransform['yamlblock']   = lambda vxx: yaml.safe_dump(vxx
                                                                 ,default_flow_style=True
                                                                 )
          mytransform['yamlfold']   = lambda vxx: yaml.safe_dump(vxx
                                                                 ,default_style='|'
                                                                 )
          mytransform['yamlpara']   = lambda vxx: yaml.safe_dump(vxx
                                                                 ,default_flow_style=False
                                                                 )
          mytransform['yamlpretty'] = lambda vxx: yaml.safe_dump(vxx, default_flow_style=False)
          mytransform['json']       = lambda vxx: json.dumps(vxx)
          mytransform['jsonpretty'] = lambda vxx: json.dumps(vxx
                                                             ,sort_keys = True
                                                             ,indent = 2
                                                             ,separators  =(',', ': ')
                                                             )
          ##
          try:
            vout = mytransform[sfmt](vout)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        def jjdata_load(self,jjinput,srcformat='yaml'):
          '''
          ##beg_func_docs
          - caption:      jjdata_load
            date:         lastmod="20150903.1728"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         load string into python native data structure
            dreftymacid:  brat_joints_twenty
            detail:  |
              * TODO ;; add support for source formats other than yaml
            dependencies:
              - __blank__
            params:
             - param: jjinput   ;; required ;; jinja raw input string
             - param: srcformat ;; optional ;; specify input data format
          ##end_func_docs
          '''

          vout = """ {"ERROR":"jjdata_load failed"} """

          ##
          try:
            if(False):
              pass;
            elif(srcformat == 'yaml'):
              vout = yaml.safe_load( jjinput.__str__() )
            elif(srcformat == 'json'):
              vout = json.loads( jjinput.__str__() )
          ##
          except Exception as msg:
            pass
            # print 'UNEXPECTED TERMINATION brat_joints_twenty msg@%s'%(msg.__repr__())
            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        ##
        def jjdata_table_dump_toexcelsheet(self,jjinput,python_aod=[],ddmetadata={}):
          '''
          ##beg_func_docs
          - caption:      jjdata_table_dump_toexcelsheet
            date:         lastmod="2015-12-29T17:15:08"
            grp_maj:      data
            grp_med:      spreadsheet
            grp_min:      dump
            desc:         |
              * output a python aod simpletable to an excel spreadsheet
              * uses 2003 xmlss format
            dreftymacid:  zenith_avenue_write
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput     ;; optarity ;; jinja raw input string
             - param: python_aod  ;; optarity ;; python aod simpletable
          ##end_func_docs
          '''

          ## jjdata_table_dump_toexcelsheet
          try:
            ## init
            from DDYAML import XmlssBase
            oXMLSS  =   XmlssBase()
            vout    =   ''
            params  =   {}
            ##;;

            ## init input
            if(jjinput.__str__() != ''):
              params['data'] = jjinput
            elif(True):
              params['data'] = python_aod
            ##;;

            ## init input
            if(ddmetadata.keys().__len__() > 0):
              params.update(ddmetadata)
            ##;;

            ## process
            vout  =   oXMLSS.tostring(params)
            ##;;
          ##
          except Exception as msg:
            print 'EXCEPTION gyro_xanthous_helmsmen msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ##
          return vout
        ##enddef

        def jjdata_table_load_fromexcelsheet(self,jjinput,sgginfile='',iggsheetindex=0,iggfirsdatarow=2,tableschema=[]):
          '''
          ##beg_func_docs
          - caption:      jjdata_table_load_fromexcelsheet
            date:         lastmod="2015-12-29T12:40:51"
            grp_maj:      data
            grp_med:      spreadsheet
            grp_min:      load
            desc:         __desc__
            dreftymacid:  vial_snaring_jocks
            detail:  |
              * TODO ;; refactor the metadata handling to be more like XmlssBase
                  * href="c:/sm/docs/mytrybits/p/trypython2/lab2014/xml/xmlssbase.py" find="firm_run_rentals"
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optional ;; input source filename
          ##end_func_docs
          '''

          ## init args
          if( jjinput.__str__() == ''):
            pass
          elif(True):
            sgginfile   = jjinput.__str__()
          ##;;

          ## init vars
          oDHH  =   DataHelperUtils()
          vout  =   ''
          ##;;

          ## processing
          try:
            oparams = {}
            oparams['xlpath']     =   sgginfile                       ## excel filepath
            oparams['xlsheet']    =   iggsheetindex                   ## wkbk sheet index (zero-based)
            oparams['xlfirstrow'] =   iggfirsdatarow                  ## first datarow (one-based)
            oparams['datadef']    =   tableschema                     ## sheet dataschema

            # oDumper.pprint( oparams )

            ## Example datadef dataschema
            # oparams['datadef']    =   yaml.safe_load('''
            #   - {fldname: lname     ,    fldtype: TEXT , fldlabel: "Last Name" }
            #   - {fldname: fname     ,    fldtype: TEXT , fldlabel: "First Name" }
            #   - {fldname: amount    ,    fldtype: INT  , fldlabel: "Amount" }
            #   - {fldname: age       ,    fldtype: INT  , fldlabel: "Age" }
            #   - {fldname: nation    ,    fldtype: TEXT , fldlabel: "Nation" }
            #   - {fldname: platform  ,    fldtype: TEXT , fldlabel: "Platform" }
            #   - {fldname: date      ,    fldtype: DATE , fldlabel: "Current Date" }
            # ''')

            vout = oDHH.excel_sheet_to_python_aod(oparams)

          ##
          except Exception as msg:
            print 'EXCEPTION skcoj_gnirans_laiv msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ##
          return vout
        ##enddef

        def jjdata_table_rowfilter(self,jjinput,dictops={}):
          '''
          ##beg_func_docs
          - caption:      jjdata_table_rowfilter
            date:         lastmod="2015-12-29T12:40:51"
            tags:         aod, simpletable, filter, insecure
            grp_maj:      data
            grp_med:      filter
            grp_min:      python array_of_dictionary (simpletable aod)
            desc: |
              * WARNING ;; uses string-eval
              * filter rows based on a row_filter_clause (eg  if( row['fname']!='homer' )   )
              * the row_filter_clause works by using a python lambda function
              * the row_filter_clause is interpolated into the python lambda function
            example: |

            dreftymacid: aware_flourish_influx
            detail:  |
              * TODO ;; complete the function docs for this function
              * TODO ;; add support for specifying input table format
            dependencies: __blank__
            params:
             - param: jjinput   ;; optional ;; input source data (as passed by jinja filter)
             - param: rowfilter ;; optional ;;
          ##end_func_docs
          '''

          ## init args
          vout = jjinput
          optsdefault   = {"rowfilter":"","tableformat":"python_aod"}
          for vkey in optsdefault:
            if(not vkey in dictops): dictops[vkey] = optsdefault[vkey]
          ##
          if(False
             or dictops['tableformat'].__str__().lower() == ''
             or dictops['tableformat'].__str__().lower() == 'python_aod'
             ):
            dictops['tableformat'] = 'aod'
          ##;;

          ## processing
          try:
            if(dictops['tableformat'] == 'aod'):
              if(dictops['rowfilter'].__str__() != ''):
                  rowfilter     =   dictops['rowfilter'].replace('\n', ' ').replace('\r', '')
                  filterfunc    =   eval( "lambda vout: [row for row in vout %s ]"%(rowfilter) )
                  vout          =   filterfunc(vout)
            elif(True):
                pass

          ##
          except Exception as msg:
            print 'EXCEPTION aware_flourish_influx msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ##
          return vout
        ##enddef

        def jjdict_update(self,jjinput,ddaddon={}):
          '''
          ##beg_func_docs
          - caption:      jjdict_update
            date:         lastmod="20150928.1014"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         update a python dictionary using dictionary.update()
            dreftymacid:  corby_welds_flier
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; required ;; original python dictionary object
             - param: ddaddon ;; required ;; new keys to add to the original python dictionary
          ##end_func_docs
          '''
          if( type(jjinput) == str):
            vout = {"__ERROR__":"__Bad_Dictionary_Input__"}
          if( type(jjinput) == dict):
            vout = jjinput
          ##
          try:
            try:
              vout.update(ddaddon)
            except:
              vout.update({"__blank__":"__blank__"})
          ##
          except Exception as msg:
            return {"__blank__":"__blank__"}
            print 'UNEXPECTED TERMINATION corby_welds_flier msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        def jjchr(self,jjinput):
          '''
          ##beg_func_docs
          - caption:      jjchr
            date:         lastmod="20150917.1254"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         python chr() function
            dreftymacid:  word_orbits_leaver
            detail:  |
              * http://code.activestate.com/recipes/65117-converting-between-ascii-numbers-and-characters/
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; placedholder arg for jinja raw input string
          ##end_func_docs
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

        def jjint(self,jjinput):
          '''
          ##beg_func_docs
          - caption:      jjint
            date:         lastmod="20150917.1254"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         python int() function
            dreftymacid:  ana_julius_yingkow
            detail:  |
              __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; required ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vout = jjinput.__str__()

          ##
          try:
            vout = int(vout)
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        def jjcsv_load(self,jjinput,ssfilepath=''):
          '''
          ##beg_func_docs
          - caption:      jjcsv_load
            date:         lastmod="20150821.1312"
            grp_maj:      data
            grp_med:      csv
            grp_min:      load
            desc:         load a csv file into a python aod
            dreftymacid:  tourism_vans_cobra
            detail:  |
              * __blank__
            dependencies:
              - import csv
            params:
             - param: jjinput     ;; ignored  ;; jinja raw input string
             - param: ssfilepath  ;; required ;; path to a csv file
          ##end_func_docs
          '''

          ##
          try:
              ##
              vout  = []
              ##
              with open(ssfilepath, 'rb') as ffg:
                data = list(csv.reader(ffg))
              ##
              for row in data:
                vout.append(dict(zip(data[0],row)))
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION tourism_vans_cobra msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        def jjdevlog_paths_byyear(self,jjinput,stryear='2015'):
          '''
          ##beg_func_docs
          - caption:      jjdevlog_paths_byyear
            date:         lastmod="Tue Dec 22 16:44:13 2015"
            grp_maj:      devlog
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         |
              BUGNAG: hardwired ssroot path
            dreftymacid:  discs_henhouse_unbundle
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ## trycatch
          try:
            ## init vars
            #vout      =   jjinput.__str__()
            vout      =   []
            ssroot    =   'c:/sm/docs/mydaydirs/%s/*'%(stryear)
            aalist    =   self.jjfile_array_fromdir("",ssroot)
            ##;;

            ## filter list
            aalist    = [ item for item in aalist if(True
                                       and self.jjfiletest(item) == 'dir'
                                       and 'week' in item.__str__().lower()
                                       )]
            ## transform list
            for item in aalist:
              item     = item.replace("\\","/")
              ttfrag01 = item.split('/')[-1]
              ttpath   = "%s/%s%s"%(item,ttfrag01,'devlog.txt')
              if not (self.jjfiletest(ttpath) == 'file'): continue
              vout.append( ttpath )
            ##;;

          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ## return
          return vout
        ##enddef

        def jjdevlog_load(self,jjinput):
          '''
          ##beg_func_docs
          - caption:      jjdevlog_load
            date:         lastmod="Tue Dec 22 15:43:42 2015"
            grp_maj:      devlog
            grp_med:      file
            grp_min:      load
            desc:         load a dreftymac-format devlog file
            dreftymacid:  awash_sneaky_lawmaker
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; required ;; devlog path
          ##end_func_docs
          '''

          ##
          fpath =   jjinput.__str__()
          vdefault  =   { "workstuff" : [], "mystuff" : [] ,"head" : [] }

          ### ********************
          ## trycatch loadfile
          try:
            vraw  =   self.jjfromfile("",fpath)
            if( vraw ):
              vout = vraw
            elif( True ):
              vout = ''
          ##
          except Exception as msg:
            print fpath
            print 'LOAD RAW FILE FAILED stank_verglas_variety msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            vout = vdefault
          ##;;

          ### ********************
          ## trycatch parseyaml
          try:
            vout  =   vout.replace("\t","  ")
            vout  =   yaml.safe_load(vout)
            if (not isinstance(vout,dict)):
              vout = vdefault
          ##
          except Exception as msg:
            print fpath
            print 'YAML PARSE SAFE_LOAD FAILED adapting_exploit_cliche msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            vout = vdefault
          ##;;

          ## return
          return vout
        ##enddef

        def jjdevlog_trybits_xref(self,jjinput):
          '''
          ##beg_func_docs
          - caption:      jjdevlog_trybits_xref
            date:         lastmod="Tue Dec 22 15:43:42 2015"
            grp_maj:      devlog
            grp_med:      trybits
            grp_min:      lookup
            desc:         |
              crossreference trybits directoies with string containing potential crossrefs
            dreftymacid:  yamaha_merger_hankow
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; required ;; devlog path
          ##end_func_docs
          '''

          ##
          fpath =   jjinput.__str__()
          vout  =   ''

          ### ********************
          ## trycatch loadfile
          try:
            vraw  = self.jjfromfile("",fpath)
            vout  =   vraw
          ##
          except Exception as msg:
            print 'LOAD RAW FILE FAILED stank_verglas_variety msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ### ********************
          ## trycatch parseyaml wellformed
          try:
            vout = yaml.safe_load(vout)
          ##
          except Exception as msg:
            print 'YAML PARSE SAFE_LOAD FAILED adapting_exploit_cliche msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ### ********************
          ## trycatch validity
          try:
            if(not vout["workstuff"] ): vout["workstuff"]   = []
            if(not vout["mystuff"] ):   vout["mystuff"]   = []
            if(not vout["head"] ):      vout["head"]   = []
            vout = yaml.safe_load(vout)
          ##
          except Exception as msg:
            print 'VALIDITY CHECK FAILED evenly_ululant_charm msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ## return
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
            dreftymacid: tickets_docks_dan
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
              vout  = "%02d" % datetime.datetime.utcnow().isocalendar()[1]
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        def jjdate_reformat(self,jjinput,innfmt='%Y%m%d%H%M',outfmt='unix'):
          '''
          ## function docs
          - caption:  jjdate_reformat
            date:     lastmod="Tue Dec 08 07:35:57 2015"
            grp_maj:  datetime
            grp_med:  reformat
            grp_min:
            desc:       grab in a date string and reformat and send it to output
            dreftymacid: wish_patent_gargle
            seealso:
              - href="smartpath://mymedia/2014/git/github/myclip/publiclab/pythondatetime.txt" find="slim_poser_hate"
              - href="smartpath://mymedia/2014/git/github/dynamic.yaml/app/demo/demo01.datetime01.txt"
            detail:  |
            ary_supported_getwhat:
              - ''
              - 'datem'
            dependencies:
              - import datetime
            params:
             - param: jjinput  ;; __blank__ ;; __blank__
             - param: getwhat  ;; __blank__ ;; __blank__
             - param: sendwhat ;; __blank__ ;; __blank__
          '''

          ##
          vout  =   ''
          ssg   =   jjinput.__str__()

          ##
          try:
            if(outfmt=='unix'):
              vout  =   time.mktime(datetime.datetime.strptime(ssg, innfmt).timetuple()).__int__()
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        def jjdate_fmt(self,jjinput,getwhat='dates'):
          '''
          ## function docs
          - caption:  jjdate_fmt
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  datetime
            grp_med:  output
            grp_min:
            desc:     get a pre-formatted date string based on a supported_format_keyword
            detail:  |
            supported_format_keyword:
              - 'dates'
              - 'datem'
            dependencies:
              - import datetime
            params:
             - param: jjinput ;; ignored ;; placeholder for raw input string
            dreftymacid: wound_fancy_touring
          '''

          ##
          vout = jjinput.__str__()

          ##
          try:
            now   =   datetime.datetime.now()
            if(False):
              pass
            elif(getwhat.lower()=='dates'):
              vout  =   "%04d%02d%02d.%02d%02d%02d" %(getattr(now,'year')
                                      ,getattr(now,'month')
                                      ,getattr(now,'day')
                                      ,getattr(now,'hour')
                                      ,getattr(now,'minute')
                                      ,getattr(now,'second')
                                      )
            elif(getwhat.lower()=='datem'):
              vout  =   "%04d-%02d-%02d %02d:%02d:%02d" %(getattr(now,'year')
                                      ,getattr(now,'month')
                                      ,getattr(now,'day')
                                      ,getattr(now,'hour')
                                      ,getattr(now,'minute')
                                      ,getattr(now,'second')
                                      )
            elif(getwhat.lower()=='uuid'):
              vout  =   "%04d%02d%02d_%02d%02d%02d" %(getattr(now,'year')
                                      ,getattr(now,'month')
                                      ,getattr(now,'day')
                                      ,getattr(now,'hour')
                                      ,getattr(now,'minute')
                                      ,getattr(now,'second')
                                      )
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
            dreftymacid: slowest_ganger_unguent
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
            dreftymacid: angriest_rings_bertha
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
            dreftymacid: beanie_waksman_taunting
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
          vout = vout.strip()
          ##
          return vout
        ##enddef

        def jjdubsplit(self,jjinput,spliton=';;',splitget=0,runmode='regex'):
          '''
          ## function docs
          - caption:  jjdubsplit
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  string_transform
            grp_med:  string
            grp_min:  split
            desc:     string split and return result from split index
            example: |
              ## simple example
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
              - param: runmode   ;; optional ;; type of split operation to use (regex|plain) (defaults to regex)
            dreftymacid: zeros_cods_views
          '''
          ##
          vout = jjinput.__str__()

          ##
          try:
            if(False):
              pass
            elif(runmode=='plain'):
              vout  =   vout.split(spliton)
            elif(runmode=='regex'):
              vout  =   re.split(spliton, vout,)
            vout  =   vout[splitget]
          except Exception as msg:
            vout  = ''
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

        ##
        def jjfile_toarray(self,jjinput,sgpath=''):
          '''
          ##beg_func_docs
          - caption:  jjfile_toarray
            date:         lastmod="2016-01-08T15:56:02"
            grp_maj:      FileIO
            grp_med:      loadfile
            grp_min:      toarray
            desc:         delete a file using python os.remove
            dreftymacid:  cleric_clam_thaws
            detail:  |
              python os.remove
            dependencies:
              - os
            params:
             - param: jjinput ;; optional ;; path to file
             - param: sgpath ;; optional ;; path to file
          ##end_func_docs
          '''

          ##
          if(str(jjinput)!=''):
            # (self,jjinput,surl=''):
            # sgpath = jjinput.__str__()
            pass
          ##;;

          ##
          try:
            vraw  =   self.jjfromfile(jjinput,sgpath)
            vout  =   vraw.splitlines()
          except Exception as msg:
            print 'FILE HANDLING EXCEPTION ;; cleric_clam_thaws msg@%s %s'%(msg.__repr__(),surl)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pass
          ##;;

          ##
          return vout
        ##enddef

        ##
        def jjfiledelete(self,jjinput,sgpath=''):
          '''
          ##beg_func_docs
          - caption:  jjfiledelete
            date:         lastmod="2016-01-08T15:56:02"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         delete a file using python os.remove
            dreftymacid:  cleric_clam_thaws
            detail:  |
              python os.remove
            dependencies:
              - os
            params:
             - param: jjinput ;; optional ;; path to file
             - param: sgpath ;; optional ;; path to file
          ##end_func_docs
          '''

          ##
          if(str(jjinput)!=''):
            sgpath = jjinput.__str__()
          ##;;

          ##
          try:
            os.remove(sgpath)
          except Exception as msg:
            ## '## File not found cleric_clam_thaws msg@%s %s'%(msg.__repr__(),sgpath)
            pass
          ##;;

          ##
          return ''
        ##enddef
        ## alias_definition
        def jjfile_delete(self,jjinput): return self.jjfiledelete(jjinput,sgpath='')
        ##enddef

        ##
        def jjfilecopy(self,jjinput,sgsrc='',sgdest=''):
          '''
          ##beg_func_docs
          - caption:  jjfilecopy
            date:         lastmod="__lastmod__"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         __desc__
            dreftymacid:  hue_beading_mural
            detail:  |
              __detail__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; ignored ;; placedholder arg for jinja raw input string
             - param: sgsrc ;; required ;; source file path
             - param: sgdest ;; required ;; destination file path
          ##end_func_docs
          '''

          ##
          vout  = "\n## %s copied to %s"%(sgsrc,sgdest)

          ##
          try:
            shutil.copyfile(sgsrc, sgdest)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION just_jan_manlier msg@%s %s'%(msg.__repr__(),sgsrc)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        def jjfiletest(self,jjinput):
          '''
          ##beg_func_docs
          - caption:      jjfiletest
            date:         lastmod="Fri Dec 18 11:05:12 2015"
            grp_maj:      fileio
            grp_med:      grp_med
            grp_min:      grp_min
            tags:         filetest, isdir, isfile,
            desc:         |
              determine if the input string represents a path to a file or directory
              return 'dir'  if dir
              return 'file' if file
              return ''     if not file and not dir
            dreftymacid:  takeaway_magnum_unisex
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vout = jjinput.__str__()

          ##
          try:
            vout = vout
            if (False): pass
            elif (os.path.isdir(vout) == True): vout = 'dir'
            elif (os.path.isfile(vout) == True): vout = 'file'
            elif (True): vout = ''
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        # import os, time
        # dirList = os.listdir("./")
        # for d in dirList:
        #     if os.path.isdir(d) == True:
        #         stat = os.stat(d)
        #         created = os.stat(d).st_mtime
        #         asciiTime = time.asctime( time.gmtime( created ) )
        #         print d, "is a dir  (created", asciiTime, ")"
        #     else:
        #         stat = os.stat(d)
        #         created = os.stat(d).st_mtime
        #         asciiTime = time.asctime( time.gmtime( created ) )
        #         print d, "is a file (created", asciiTime, ")"

        # useless for intended purpose, always returns ddyaml.py
        #def jjfile_currpath(self,jjinput):
        #  '''
        #  ### ##beg_func_docs
        #  ### - caption:      jjfile_currpath
        #  ###   date:         lastmod="20150825.1331"
        #  ###   grp_maj:      grp_maj
        #  ###   grp_med:      grp_med
        #  ###   grp_min:      grp_min
        #  ###   desc:         return os.path.realpah(__file__)
        #  ###   dreftymacid:  obey_heir_midget
        #  ###   detail:  |
        #  ###     * __blank__
        #  ###   dependencies:
        #  ###     - __blank__
        #  ###   params:
        #  ###    - param: jjinput ;; optarity ;; jinja raw input string
        #  ### ##end_func_docs
        #  '''
        #
        #  ##
        #    vout = jjinput.__str__()
        #
        #  ##
        #  try:
        #    vout = __file__
        #  ##
        #  except Exception as msg:
        #    print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
        #    exc_type, exc_obj, exc_tb = sys.exc_info()
        #    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #    print(exc_type, fname, exc_tb.tb_lineno)
        #
        #  ##
        #  return vout
        ###enddef

        ## TODO ;; rename this to jjfile_tostring more consistent naming convention with
        ## jjfile_toarray
        def jjfromfile(self,jjinput,surl=''):
          '''
          ## function docs
          - caption:  jjfromfile
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:  FileIO
            grp_med:  loadfile
            grp_min:  fromfile
            desc:     string.fromfile
            tags:     jjfromfile, jjfile_load, jjfile
            dreftymacid: waterage_eat_formal
            detail:  |
              pull in content from a file to a string
            todo: |
              * figure out why jjfromfile not working
                  * href="csm://mydaydirs/2015/week42/json/proj01test01transform01.txt"
            dependencies:
              - none
            params:
             - param: jjinput   ;;  required  ;;  placeholder argument for jinja
             - param: surl      ;;  required  ;;  file path
          '''
          ##
          vout    =     ''
          if(not 'debug_mode'):
            print "%s -- %s"%(jjinput,surl)
          # if(jjinput.__str__().strip() != ''):
          #   surl = jjinput.__str__()
          #surl    =     surl or jjinput.__str__()
          ##print surl
          ##vout  = open(surl,'r').read()

          ##
          try:
            ## BUGNAG ;; added encode ascii ignore
            vout  =  codecs.open(surl, 'r', 'utf-8').read().replace(u'\xa0', u' ')
            #vout  =   codecs.open(surl, 'r', 'utf-8').read()
            #vout  =   filter(lambda vxx: vxx in string.printable, vout)
            #vout  =   vout.encode('ascii','replace')
            ##print vout
            #vout  = open(surl,'r').read().replace(u'\xa0', ' ')
            #vout  = vout.decode('utf-8').encode('ascii', 'ignore')
            pass
          except Exception as msg:
            print """
            ### ------------------------------------------------------------------------
            ### ------------------------------------------------------------------------
            ### ------------------------------------------------------------------------

            FILE IO HASSLE ;; href="%s"

            ### ------------------------------------------------------------------------
            ### ------------------------------------------------------------------------
            ### ------------------------------------------------------------------------
            """ %(surl)
            print 'UNEXPECTED TERMINATION sharing_client_smearing msg@%s %s'%(msg.__repr__(),surl)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          #return vout.decode('ascii','replace')
          return vout
        ##enddef
        ## alias_definition
        def jjfile_tostring(self,jjinput,surl=''):
          return self.jjfromfile(jjinput,surl)
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
            dreftymacid: viremic_astray_wraiths
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
            print 'UNEXPECTED TERMINATION viremic_astray_wraiths msg@%s'%(msg.__repr__())
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

        def jjhtml_findall(self,jjinput,mytagg='a'):
          '''
          ##beg_func_docs
          - caption:      jjhtml_findall
            date:         lastmod="20150903.1402"
            grp_maj:      string
            grp_med:      html
            grp_min:      scrape
            desc:         use the findall method of beautifulsoup4
            dreftymacid:  nudger_unto_permit
            detail:  |
              * todo ;; add support for attribute based query
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vinput    =   jjinput.__str__()
          soup      =   BeautifulSoup(vinput)
          table     =   soup.findAll(mytagg)

          ##
          try:
            vout = table
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION nudger_unto_permit msg@%s'%(msg.__repr__())
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
            dreftymacid:  stealthy_pleasing_uncivil
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

        def jjhtml5_pretty(self,jjinput):
          """
          ##beg_func_docs
          - caption:      jjhtml5_pretty
            date:         lastmod="20150916.1220"
            grp_maj:      string
            grp_med:      process
            grp_min:      html
            desc:         pretty print using html5print
            dreftymacid:  easing_stricter_unblocks
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; required ;; jinja raw input string
          ##end_func_docs
          """

          ##
          from html5print import HTMLBeautifier

          ##
          ##vout    = jjinput.__str__()
          #print jjinput[2737:]
          #exit()

          #vout    = jjinput.__str__()
          #vout    = jjinput.replace(u'\xa0', ' ').encode('utf-8')
          vout      =   jjinput.replace(u'\xa0',u' ')
          #print vout.encode('utf-8')
          #vout      =   vout.decode('ascii','replace')
          #vout    = jjinput.encode('utf-8')
          #vout    = jjinput.encode('ascii', 'ignore').decode('ascii')
          print vout
          myindd  = 4

          ##
          try:
            ##
            vout    =   (HTMLBeautifier.beautify(vout,indent=myindd,encoding='utf-8'))
            vout    =   re.sub(r"[\r\n]+" , "\n",  vout)
            vout    =   vout.split('<body>')[1]
            vout    =   vout.split('</body>')[0]

          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        def jjhtml_pretty(self,jjinput,bforceascii=True,ballowfrag=False,):
          """
          ## function docs
          - caption:    jjhtml_pretty
            date:       lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:      string
            grp_med:      process
            grp_min:      html
            dreftymacid:  leave_fakery_brag
            desc: pretty print html
            seealso:
              - jjrequesturl
              - href="../../../../../../mytrybits/p/trypython2/lab2014/pyweb/htmlprettyprint.py"
              - TODO ;; in frag mode, figure out how to always get bs4.element.Tag instead of bs4.NavagableString for prettify to always work
            detail: |
                pretty print html using beautifulsoup4
            dependencies:
              - BeautifulSoup bs4
            params:
             - param: jjinput     ;; required   ;; placeholder argument for jinja
             - param: bforceascii ;; __blank__  ;; __blank__
             - param: ballowfrag  ;; __blank__  ;; __blank__
          """

          ##
          rawdata   =   jjinput
          vout      =   ''

          ##
          try:
            ## handle the case with bforceascii
            html  =  rawdata
            if(bforceascii):
              html  = html.decode('ascii','replace')

            # Double curly brackets to avoid problems with .format()
            stripped_markup = html.replace('{','{{').replace('}','}}')

            ## init soup
            #soup = BeautifulSoup(html)

            stripped_markup = BeautifulSoup(stripped_markup)
            unformatted_tag_list = []

            for i, tag in enumerate(stripped_markup.find_all([ 'a'
                                                              , 'a'
                                                              , 'b'
                                                              , 'br'
                                                              , 'button'
                                                              , 'h1'
                                                              , 'h2'
                                                              , 'h3'
                                                              , 'h4'
                                                              , 'h5'
                                                              , 'li'
                                                              , 'span'
                                                              , 'strong'
                                                              ])):
                unformatted_tag_list.append(str(tag))
                tag.replace_with('{' + 'unformatted_tag_list[{0}]'.format(i) + '}')

            reload(sys); sys.setdefaultencoding('utf-8')
            pretty_markup = stripped_markup.prettify().format(unformatted_tag_list=unformatted_tag_list)
            vout = pretty_markup

            ### handle the case with ballowfrag
            ### http://stackoverflow.com/questions/15980757/how-to-prevent-beautifulsoup4-from-adding-extra-htmlbody-tags-to-the-soup
            #if(ballowfrag):
            #  if soup.body:
            #      soup =  soup.body.next
            #      print "%s :: %s"%('ok1' , type(soup))
            #  elif soup.html:
            #      soup =  soup.html.next
            #      print "%s :: %s"%('ok2' , type(soup))
            #  else:
            #      soup =  soup.contents[0]
            #      print "%s :: %s"%('ok3' , type(soup))

            ## bsoup annoyance_buster ;; nastier_uncover_opusz
            ## href="../../../../../../mytrybits/u/tryunicode/txt/bsoupannoyance.txt"
            #vout =  soup.prettify()
            #vout =  vout.encode('ascii', 'ignore')
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        #def jjhtml_pretty(self,jjinput):
        #  '''
        #  ### ##beg_func_docs
        #  ### - caption:      jjhtml_pretty
        #  ###   date:         lastmod="criminal_dividing_her"
        #  ###   grp_maj:      string
        #  ###   grp_med:      process
        #  ###   grp_min:      html
        #  ###   desc:         html pretty method that uses lxml instead of bsoup
        #  ###   dreftymacid:  oils_admits_fatly
        #  ###   detail:  |
        #  ###     * __blank__
        #  ###   dependencies:
        #  ###     - import lxml
        #  ###   params:
        #  ###    - param: jjinput ;; required ;; jinja raw input string
        #  ### ##end_func_docs
        #  '''
        #
        #  ##
        #  vout = jjinput.encode('ascii','ignore').__str__()
        #
        #  ##
        #  try:
        #    from lxml import etree, html
        #    #vout = "<html><body><h1>hello world</h1></body></html>"
        #    reload(sys); sys.setdefaultencoding('utf-8')
        #    document_root =   html.fromstring(vout)
        #    vout          =   (etree.tostring(document_root, encoding='unicode', pretty_print=True))
        #  ##
        #  except Exception as msg:
        #    print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
        #    exc_type, exc_obj, exc_tb = sys.exc_info()
        #    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #    print(exc_type, fname, exc_tb.tb_lineno)
        #
        #  ##
        #  return vout
        ###enddef

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
          ##;;

          ##
          if(hug==''): aahug.append('');aahug.append('');
          if(hug=='"'): aahug.append('"');aahug.append('"');
          if(hug=="'"): aahug.append("'");aahug.append("'");
          if(hug=="["): aahug.append("[");aahug.append("]");
          if(hug=="]"): aahug.append("[");aahug.append("]");
          if(hug=="<"): aahug.append("<");aahug.append(">");
          if(hug==">"): aahug.append("<");aahug.append(">");
          if(hug=="<!--"): aahug.append("<!--\n");aahug.append("\n-->");
          if(hug=="("): aahug.append("(");aahug.append(")");
          if(hug==")"): aahug.append("(");aahug.append(")");
          if(hug=="{"): aahug.append("{");aahug.append("}");
          if(hug=="}"): aahug.append("{");aahug.append("}");
          ##;;

          ##
          try:
            vout = "".join([ aahug[0], vout , aahug[1] ])
          except Exception as msg:
            pass
          try:
            if( aahug.__len__() == 0 ):
              vout = "".join( [hug, vout, hug] )
          except:
            pass
          ##;;

          ##
          return vout
        ##enddef

        def jjindent(self,jjinput,imult=2,strlead=' ',):
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
             - param: imult     ;; optional ;; multiplier for indenter (default 2)
             - param: strlead   ;; optional ;; leading indenter default (single whitespace char)
            output: python string
          """

          ##
          vout = jjinput.__str__()
          imult = int(imult)

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
            dreftymacid:  hazard_veg_ivy
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
          vout = jjinput

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
            vout  = jjinput[index]
          except  IndexError as msg:
            vout  = ''
          except  Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        def jjlistrange(self,jjinput,rbeg=0,rend=-1):
          """
          ## function docs
          - caption:    jjlistrange
            date:       lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:      getinfo
            grp_med:      list
            grp_min:      item
            dreftymacid:  councils_dock_swam
            desc: try to return list item at index
            example: |
              {{ [1,2,3,4,5] |jjlistrange(0,1)      }} --> [1]
              {{ [1,2,3,4,5] |jjlistrange(0,3)      }} --> [1, 2, 3]
              {{ [1,2,3,4,5] |jjlistrange(0,-1)     }} --> [1, 2, 3, 4]
              {{ [1,2,3,4,5] |jjlistrange(0,None)   }} --> [1, 2, 3, 4, 5]
              {{ [1,2,3,4,5] |jjlistrange(3,None)   }} --> [4, 5]
              {{ [1,2,3,4,5] |jjlistrange(-3,None)  }} --> [3, 4, 5]
              {{ [1,2,3,4,5] |jjlistrange(-2,None)  }} --> [4,5]
              {{ [1,2,3,4,5] |jjlistrange(-2,-1)    }} --> [4]
              {{ [1,2,3,4,5] |jjlistrange(-3,-2)    }} --> [3]
            detail: |
                __blank__
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; python list
             - param: rbeg    ;; optional ;; rangebegin
             - param: rend    ;; optional ;; rangeend
            output: python string
          """

          ##
          vout = jjinput

          ##
          try:
            vout  = vout[rbeg:rend]
          except  IndexError as msg:
            vout  = vout
          except  Exception as msg:
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
                NOTE: this is superfluous, jinja already has "join" filter
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

        def jjlistsort(self,jjinput,mode='normal'):
          """
          ## function docs
          - caption:  jjlistsort
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    getinfo
            grp_med:    list
            grp_min:    sort
            dreftymacid:  drinks_gem_shoving
            desc: return a sorted list
            example: |
              {{ ['zulu','alpha','bravo','charl','bravo','delta','echo'] |jjlistsort()            }}
              {{ ['zulu','alpha','bravo','charl','bravo','delta','echo'] |jjlistsort('normal')    }}
              {{ ['zulu','alpha','bravo','charl','bravo','delta','echo'] |jjlistsort('uniq')      }}
              {{ ['zulu','alpha','bravo','charl','bravo','delta','echo'] |jjlistsort('reverse')   }}
              {{ ['zulu','alpha','bravo','charl','bravo','delta','echo'] |jjlistsort('uniq') |jjlistsort('reverse') }}
            detail: |
                __blank__
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; python list
             - param: mode    ;; optional ;; sort mode
            output: python string
          """
          ##
          vout = jjinput

          ##
          try:
            if (mode.lower() == 'normal'):
              vout = sorted(vout)
            if (mode.lower() == 'reverse'):
              vout = sorted(vout, reverse=True)
            if (mode.lower() == 'unique' or mode.lower() == 'uniq'):
              vout =  [ vxx[0] for vxx in itertools.groupby(sorted(vout)) ]
          except  IndexError as msg:
              vout  = ''
          except  Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##
          return vout
        ##enddef

        def jjlistuniq(self,jjinput):
          """
          ## function docs
          - caption:  jjlistuniq
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    getinfo
            grp_med:    list
            grp_min:    unique
            dreftymacid:  eras_oafish_halving
            desc: |
              * return a uniq_list of unique elements from original_list
            example: |
              {{ ['zulu','zulu','zulu','alpha','alpha','alpha','bravo','bravo','bravo',] |jjlistuniq() }}
            detail: |
                __blank__
            dependencies:
              - none
            params:
             - param: jjinput ;; required ;; python list
             - param: mode    ;; optional ;; sort mode
            output: python string
          """
          ##
          ddseen  =   {}
          vout    =   []

          ##
          try:
            for item in jjinput:
              if(item in ddseen.keys()):
                ddseen[item] = ddseen[item] + 1
              elif(True):
                ddseen[item] = 0
              if(ddseen[item] == 0):
                vout.append(item)
          except  IndexError as msg:
              vout  = ''
          except  Exception as msg:
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
        ##enddef
        ## alias_definition
        def jjmarkdowntohtml(self,jjinput): return self.jjmarkdown2html(jjinput)
        ##enddef


        def jjnewline_erase(self,jjinput):
          """
          ## function docs
          - caption:  jjnewline_erase
            date:     lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:    string_transform
            grp_med:    whitespace
            grp_min:    remove
            dreftymacid:  uranism_orate_hangar
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

        def jjfile_array_fromdir(self,jjinput,ssfilespec='',ssmode='glob'):
          """
          ## function docs
          - caption:      jjfile_array_fromdir
            date:         lastmod="Mon 2014-10-20 16:45:46"
            grp_maj:      FileIO
            grp_med:      directory
            grp_min:      traverse
            dreftymacid:  pests_cow_vealing
            desc: python  ArrayFromDirectory
            example: |
              {#- ------------------------------------------------------------------------ -#}
              {%- set ttrootpath  = 'c:/sm/docs/mytrybits/*/*'  -%}
              {%- set ttpathmode  = 'glob'                      -%}
              {%- set mypaths     = ''|jjfile_array_fromdir(ttrootpath,ttpathmode)   -%}
              {#- ------------------------------------------------------------------------ -#}
              {{ mypaths }}
            alias:
              - __blank__
            detail: |
              ## ssmode
              * glob    ;; uses glob.glob to traverse dirs
              * walk    ;; uses os.walk to traverse dirs
              ## seealso
              * href="smartpath://mydaydirs/2015/week22/py/oswalk.demo.py"
              * return a python list result from os.walk
            dependencies:
              - import glob
              - import os
            params:
              - param: jjinput    ;; ignored  ;; placeholder argument for jinja
              - param: ssfilespec ;; required ;; path specification
              - param: ssmode     ;; required ;; file traversal mode
            output: python string
          """
          ##
          ## vout = jjinput.__str__()

          ##
          try:
            if(ssmode.lower()==''):
              pass
            elif(ssmode.lower()=='glob'):
              aResults    =   glob.glob(ssfilespec)
              aResults    =   [ vxx.replace('\\','/') for vxx in aResults ]
              vout        =   aResults
            elif(ssmode.lower()=='walk' or True):
              vout    =   []
              aatemp  =   []
              for root, dirs, files in os.walk(ssfilespec):
                aatemp.extend(  [ "/".join([root,vxx]) for vxx in dirs ] )
              aatemp = [vxx.replace('\\','/') for vxx in aatemp]
              vout = aatemp
          except Exception as msg:
            print 'EXCEPTION pests_cow_vealing msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

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
            dreftymacid:  verbiage_wrapover_wreaths
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

        def jjradioextract(self,jjinput,targfile='',rtregexbeg='',rtregexend='',
                           options={'verbose':True}
                           ):
          '''
          ##beg_func_docs
          - caption:      jjradioextract
            date:         lastmod="20151031.0850"
            grp_maj:      file
            grp_med:      string
            grp_min:      extract
            desc:         radiotable ;; extract a region of a text file using 'radiotable' style regions
            dreftymacid:  atrocity_bluntest_coping
            seealso:
              - href="../../../../../../mymedia/2014/git/github/dynamic.yaml/app/demo/demo01.jjradiotable01.txt"
              - href="../../../../../../mytrybits/y/tryyaml/dynamicyaml/app/demo/demo01.command06.txt"
              - href="../../../../../../mymedia/2014/git/github/myclip/myclip.ddyaml/transform01.yaml.txt"
              - href="https://www.gnu.org/software/emacs/manual/html_node/org/Radio-tables.html"
            detail:  |
              * uses the emacs org mode 'radiotable' metaphor
              * TODO ;; add passthrough support for USEBOM and unicode
            dependencies:
              - import re
              - self.jjfromfile
            params:
             - param: jjinput    ;; required  ;; jinja raw input string
             - param: targfile   ;; required  ;; target destination file for pasting in radiotable
             - param: rtregexbeg ;; required  ;; begin regex token for delimiting radiotable
             - param: rtregexend ;; required  ;; end regex token for delimiting radiotable
             - param: options    ;; optional  ;; local options dictionary
          ##end_func_docs
          '''

          ##
          sgradiobody =   ''
          sgrawtext   =   self.jjfromfile(jjinput,targfile)
          vout        =   ''

          ##
          try:
            vout      =   re.split(rtregexbeg, sgrawtext,)[1]
            vout      =   re.split(rtregexend, vout,)[0]

          ##
          except IndexError as msg:
            print 'Error: Bad regular expression or no match found for jjradioextract? atrocity_bluntest_coping msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION atrocity_bluntest_coping msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ###
          #if(options.has_key('verbose')):
          #  if(options['verbose']==None):     pass
          #  elif(options['verbose']==True):   vout = "".join([vout])
          #  elif(options['verbose']==False):  vout = ''

          ##
          return vout
        ##enddef

        def jjradioreplace(self,jjinput,targfile='',rtregexbeg='',rtregexend='',
                            options={'verbose':False,
                                'cmmt'  : '###',
                                'name'  : 'file_info',
                                'beg'   : 'beg-',
                                'end'   : 'end-',
                                'wrap'  : '<',
                            }
                          ):
          '''
          ##beg_func_docs
          - caption:      jjradioreplace
            date:         lastmod="20150917.1056"
            grp_maj:      file
            grp_med:      string
            grp_min:      modify
            desc:         |
                radiotable ;; replace a region of a text file using 'radiotable' style regions
                * NOTE: this function has met with disappointing results.
                * There are alternative ways to handle this.
                * href="smartpath://mydaydirs/2016/week13/week13devlog.txt" find="uusunrise_firing_paths"
            dreftymacid:  extra_clamp_positive
            seealso:
              - href="c:/sm/docs/mydaydirs/2016/week13/week13devlog.txt" find="uusunrise_firing_paths"            
              - href="smartpath://mymedia/2014/git/github/dynamic.yaml/app/demo/demo01.jjregex.txt" find="erase_showing_measle"
              - href="smartpath://mymedia/2014/git/github/myclip/myclip.ddyaml/transform01.yaml.txt"
              - href="https://www.gnu.org/software/emacs/manual/html_node/org/Radio-tables.html"
            detail:  |
              * uses the emacs org mode 'radiotable' metaphor
              * TODO ;; add passthrough support for USEBOM and unicode
            dependencies:
              - __blank__
            params:
              - param: jjinput    ;; required ;; jinja raw input string
              - param: targfile   ;; required ;; target destination file for pasting in radiotable
              - param: rtregexbeg ;; required ;; begin regex token for delimiting radiotable
              - param: rtregexend ;; required ;; end regex token for delimiting radiotable
              - param: options    ;; optional ;; local options dictionary
          ##end_func_docs
          '''

          ## init vars
          tagbeg      =   ''
          tagend      =   ''
          sgradiobody =   jjinput.__str__()
          sgrawtext   =   self.jjfromfile(jjinput,targfile)
          vout        =   ''
          zopts       =   {}
          zdefaults   =   {'verbose':False,
                                'cmmt'  : '###',
                                'name'  : 'file_info',
                                'beg'   : 'beg-',
                                'end'   : 'end-',
                                'wrap'  : '<',
                          }
          ##
          for vkey in zdefaults:
            if( (vkey in options) and (options[vkey].__str__() != '') ):
              zopts[vkey] = options[vkey]
            elif( True ):
              zopts[vkey] = zdefaults[vkey]
          ##;;

          ##
          if('debugging'):
            oDumper.pprint( zopts )
          ##;;

          ## init vars
          if(None): pass
          elif(rtregexbeg == '' or rtregexend == ''):
            tagbeg      =   self.jjhug(zopts['beg']+zopts['name'],zopts['wrap'])
            tagend      =   self.jjhug(zopts['end']+zopts['name'],zopts['wrap'])
            ##
            rtregexbeg  =   '\s*'+zopts['cmmt']+'\s*'+tagbeg+''
            rtregexend  =   '\s*'+zopts['cmmt']+'\s*'+tagend+''
          ##;;

          ##
          # print tagbeg
          # print tagend
          ##;;

          ##
          try:
            rawpref   = re.split(rtregexbeg, sgrawtext,)[0]
            rawsuff   = re.split(rtregexend, sgrawtext,)[1]
            vout      = "".join([rawpref,sgradiobody,rawsuff])
            self.jjtofile(vout,targfile,'replace')
            vout      = sgradiobody
          ##
          except IndexError as msg:
            print 'Error: Bad regular expression or no match found for jjradioreplace? extra_clamp_positive msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          except Exception as msg:
            print 'UNEXPECTED TERMINATION extra_clamp_positive msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ##
          if(zopts.has_key('verbose')):
            if(zopts['verbose']==None):
              pass
            elif(zopts['verbose']==True):
              vout = vout
            elif(zopts['verbose']==False):
              vout = ''
          ##;;

          ##
          return vout
        ##enddef

        def jjregexreplace(self,jjinput,pattern='',replacement='',flags=''):
          '''
          ## function docs
          - caption:  jjregexreplace
            date:     lastmod="Fri Aug 14 16:27:17 2015"
            grp_maj:      regex
            grp_med:      string
            grp_min:      replace
            dreftymacid:  damp_slicing_leafy
            desc:         __desc__
            detail:  |
              basename
            dependencies:
              - none
            params:
             - param: jjinput      ;;  required   ;;  placeholder argument for jinja
             - param: pattern      ;;  optional   ;;  regex pattern
             - param: replacement  ;;  optional   ;;  string replacement
             - param: flags        ;;  optional   ;;  string representation of python's `re.M` style flags
          '''

          ##
          vout      =   jjinput.__str__()
          ##;;

          ##
          try:
            ##
            if(flags != ''):
              flags     =   reduce(lambda xx,yy: xx|yy, [getattr(re,vxx.upper()) for vxx in list(flags)])
                ## this complex line above is just converting a flat string of 'IM' style flags
                ## into the native python re.I re.M constants
            elif(True):
                flags =   int(0)
            ##
            regex     =   re.compile(pattern,flags)
            vout      =   regex.sub(replacement, vout)
          ##;;

          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ##
          return vout
        ##enddef

        def jjregexfindall(self,jjinput,ssregex='[\w]+'):
          '''
          ##beg_func_docs bkmk001
          - caption:      jjregexfindall
            date:         lastmod="Wed 2015-08-26 12:28:27"
            grp_maj:      regex
            grp_med:      string
            grp_min:      find
            desc:         python regex findall
            dreftymacid:  shaming_java_asocial
            detail:  |
              * __blank__
            seealso:  |
              * regain://joints_hugest_burt   (mytrybits python2)
              * regain://lofter_hyper_chorus  (mytrybits python2)
              * href="../../../../../../mytrybits/y/tryyaml/dynamicyaml/app/demo/barebonesplus.helloworld.txt" find="uuzappan"
            dependencies:
              - import re
            params:
             - param: jjinput ;; required ;; jinja raw input string
             - param: ssregex ;; required ;; regex to run against jjinput
          ##end_func_docs
          '''

          ##
          vout = jjinput.__str__()

          ##
          try:
            oRegex =  re.compile(ssregex,re.M|re.S|re.I)
            vout   =  oRegex.findall(vout)

          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION formal_awing_wolf msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef
        ## alias_definition
        def jjregex_findall(self,jjinput,ssregex): return self.jjregexfindall(jjinput,ssregex)
        ##enddef

        def jjregexsub(self,jjinput,ssregex='[\w]+',ssreplace='__ssreplace__',bstrip=False):
          '''
          ##beg_func_docs bkmk001
          - caption:      jjregexsub
            date:         lastmod="Wed 2015-08-26 12:28:27"
            grp_maj:      regex
            grp_med:      string
            grp_min:      substitute
            desc:         python regex sub
            dreftymacid:  tasty_dario_awaken
            detail:  |
              * __blank__
            seealso:  |
              * href="smartpath://mytrybits/a/tryanylang/datadef/python/stringops_table.txt" find="uralitic_top_surf"
              *
            dependencies:
              - import re
            params:
             - param: jjinput   ;; required ;; jinja raw input string
             - param: ssregex   ;; required ;; regex to run against jjinput
             - param: ssreplace ;; required ;; string replacement
             - param: bstrip    ;; optional ;; boolean whether to strip whitespace
          ##end_func_docs
          '''

          ##
          vout = jjinput.__str__()

          ##
          try:
            repattern   = ssregex
            if(not bstrip):
              vout = re.sub(re.compile(repattern, re.MULTILINE), ssreplace, vout)
            elif(bstrip):
              vout = re.sub(re.compile(repattern, re.MULTILINE), ssreplace.lstrip().rstrip(), vout)
            elif(True):
              vout = re.sub(re.compile(repattern, re.MULTILINE), ssreplace, vout)
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION formal_awing_wolf msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef
        ## alias_definition
        def jjregex_sub(self,jjinput,ssregex,ssreplace,bstrip=False): return self.jjregexsub(jjinput,ssregex,ssreplace,bstrip)
        ##enddef

        #def jjregionreplace(self,jjinput,vreplace='',regbeg='',regend='',):
        #  """
        #  ## function docs
        #  - caption:  jjregionreplace
        #    date:     lastmod="Mon 2014-10-20 16:45:46"
        #    grp_maj:    string_transform
        #    grp_med:    replace
        #    grp_min:    string
        #    dreftymacid:  found_goliath_loyalty
        #    desc: replace a subregion of a string with optional balanced delimiters
        #    detail: |
        #      ## overview
        #      replace a subregion of a string with optional balanced delimiters
        #      ## demo
        #      regain://untwist_disobey_dolby
        #      regain://dynamicyaml
        #    dependencies:
        #      - import uuid
        #    params:
        #     - param: jjinput   ;; required ;; raw input string
        #     - param: vreplace  ;; optional ;; replacement string
        #     - param: regbeg    ;; optional ;; delimiter begin string
        #     - param: regend    ;; optional ;; delimiter end string
        #    output: python array
        #  """
        #  ##
        #  vorigg  = jjinput.__str__()
        #
        #  ##
        #  try:
        #    ## init
        #    newdelim  =   str(uuid.uuid4())
        #    ##;;
        #
        #    ## process
        #    vtempgg     =   vorigg
        #    if(not regbeg == regend):
        #      vtempgg     =   vtempgg.replace(regend,regbeg)
        #    if(not vtempgg == ''):
        #      vtempgg     =   vtempgg.replace(regbeg,newdelim)
        #      vtempgg     =   vtempgg.split(newdelim)
        #      vtempgg[1]  =   "".join([regbeg,vreplace,regend])
        #      vtempgg     =   "".join(vtempgg)
        #    ##;;
        #
        #    ##
        #    vout = vtempgg
        #  except Exception as msg:
        #    print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
        #    exc_type, exc_obj, exc_tb = sys.exc_info()
        #    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #    print(exc_type, fname, exc_tb.tb_lineno)
        #  ##
        #  return vout
        ###enddef

        def jjcurl(self,jjinput,method='put',target='',payload=''):
          '''
          ##beg_func_docs
          - caption:      jjcurl
            date:         lastmod="20151008.1636"
            grp_maj:      grp_maj
            grp_med:      grp_med
            grp_min:      grp_min
            desc:         simulate a curl call. seealso jjrequesturl
            dreftymacid:  armpits_magnet_freshens
            seealso:
              - jjrequesturl
            detail:  |
              * __blank__
            dependencies:
              - import requests
            params:
             - param: jjinput   ;; ignored  ;; jinja raw input string
             - param: method    ;; optarity ;; target url
             - param: target    ;; optarity ;; target url
             - param: payload   ;; optarity ;; data payload
          ##end_func_docs
          '''

          ##
          ## vout = jjinput.__str__()

          ##
          try:
            vout       =     getattr(requests,method)(target,data=payload)
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION armpits_magnet_freshens msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

        def jjrequesturl(self,jjinput,sgurl='http://www.example.com',):
          '''
          ## function docs
          - caption:      jjurl_request
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
        ## alias_definition
        def jjfromurl(self,jjinput,sgurl): return self.jjrequesturl(jjinput,sgurl)
        def jjurl_request(self,jjinput,sgurl): return self.jjrequesturl(jjinput,sgurl)
        ##enddef

        def jjurl_exists(self,jjinput,sgurl='http://www.example.com',):
          '''
          ## function docs
          - caption:      jjurl_exists
            date:         lastmod="Tue 2015-08-11 16:12:12"
            grp_maj:      webscrape
            grp_med:      request
            grp_min:      url
            dreftymacid:  croat_jails_unglue
            desc:         return true/false whether a given url is found
            detail: |
              ## overview
              request the content of a URL using python requests module
            dependencies:
              - import urllib2
            params:
             - param: jjinput   ;; ignored  ;; placeholder for raw input string
             - param: url       ;; optional ;; url defaults to example.com
            output: python array
          '''
          ##
          vout = ''

          ##
          try:
            ret         =   urllib2.urlopen(sgurl)
            if ret.code == 200:
              ffresult = True
          except Exception as msg:
            ffresult = False

          ##
          vout = ffresult

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
            dreftymacid:  wolfish_sword_darken
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
            dreftymacid:  enforcer_cube_herbs
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
            dreftymacid:  pimple_timidity_sweating
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
              vout = "/".join(re.split('[/]+', vout))
              vout = "## create directory %s"%(vout)
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
              * create    ;; create file if not exist, ignore if already exists
              * replace   ;; create file if not exist, overwrite if already exists
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
                vout    = "\n jjtofile failed to write output file %s (permissions issue? or does file already exist?)"%(vout)
              ##
              elif( (os.path.isfile(outpath)) and (writemode=='replace') ):
                pymode  = 'wb'
                vout    = outpath;
                vout    = "\n jjtofile output file %s"%(vout)
              ##
              elif( (os.path.isfile(outpath)) and (writemode=='append') ):
                pymode  = 'ab'
                vout    = outpath;
                vout    = "\n jjtofile append file %s"%(vout)
              ##---

              #print writemode
              #print outpath
              #print pymode

              ## process
              if( not pymode == '' ):
                oFile = open(outpath,pymode)
                if(usebom==True):
                  oFile.write(codecs.BOM_UTF8)
                os.chmod(outpath, 0o700)
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
            dreftymacid: heaven_bishop_diverts
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
             - param: jjinput ;; ignored ;; placeholder argument for jinja
             - param: enum ;; optional ;; add on additional enumeration component
            dreftymacid: vehement_chewer_til
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

        def jjwinexplore(self,jjinput,path='',useback=True):
          '''
          ## function docs
          - caption:  jjwinexplore
            date:     lastmod="Fri Aug 14 16:05:31 2015"
            grp_maj:      __grp_maj__
            grp_med:      __grp_med__
            grp_min:      __grp_min__
            dreftymacid:  guidance_untie_quests
            desc:         open an explorer window
            detail:  |
              open explorer window on a path (currently windows-only)
            dependencies:
              - none
            params:
             - param: jjinput   ;; ignored  ;; placeholder argument for jinja
             - param: path      ;; required ;; winexplore designated path
             - param: useback   ;; optional ;; use backslash instead of fwdslash
          '''

          ## process
          try:
            vout  = "\n## jjwinexplore %s"%(path)
            import subprocess
            if(useback): path = path.replace('/',"\\")
            subprocess.Popen(r'explorer /select,"%s"'%path)
            pass;

          ## exception
          except Exception as msg:
            print 'UNEXPECTED TERMINATION msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ## return
          return vout
        ##enddef
      ##endclass
###!}}}
