# -*- coding: utf-8 -*-
"""
### <beg-file_info>
### main:
###   - date: created="Thu Feb 11 12:34:33 2016"
###     last: lastmod="Thu Feb 11 12:34:33 2016"
###     dreftymacid:    "richer_dampen_corker"
###     desc: |
###         temporary scratch tests for ddyaml
###         test the new functionality of YamlEmbedJinja
### <end-file_info>
"""

### ------------------------------------------------------------------------
### begin_: init python
if('python_region'):
###!{{{
###!- caption:  __caption__
###!  dreftymacid: mary_optic_winglet
###!  body: |
      ## std lib
      import datetime
      import json
      import logging
      import operator
      import os
      import re
      import sys
      import textwrap
      import yaml

      ## pprint
      import pprint
      oDumper = pprint.PrettyPrinter(indent=4);

      ## import local lib
      from YamlEmbedJinja import YamlEmbedJinja ### "./YamlEmbedJinja.py"
      pass;
###!}}}

### ------------------------------------------------------------------------
### begin_: nameismain
if(__name__ == '__main__'):
###!{{{
###!- caption:  __caption__
###!  date:     created="Wed Feb 18 13:11:30 2015"
###!  tags:     __tags__
###!  desc: |
###!  		__desc__
###!  dreftymacid: flake_throws_yup
###!  body: |

      ##
      otest     =   YamlEmbedJinja()
      rawyaml   =   '''
        maininfo:
          fname:    homer
          lname:    simpson
          age:      33
        alphainfo:
          alpha:    "one"
          bravo:    "{{ alphainfo.alpha }}"
          charlie:  "{{ bravoinfo.alpha }}"
        bravoinfo:
          alpha:    "two"
          bravo:    "{{ alphainfo.bravo }}"
          charlie:  "{{ bravoinfo.bravo }}"
        charlieinfo:
          alpha:    "three"
          bravo:    "{{ alphainfo.charlie }}"
          charlie:  "{{ charlieinfo.charlie }}"
        documents_table:
          - caption: alpha
            wwbody: >
              {% set tttest = [maininfo.fname,maininfo.lname] %} {{ [maininfo.fname,maininfo.lname] |title() }} is {{maininfo.age * 1}} !
          - caption: bravo
            wwbody: >
              {{maininfo.fname |title() }} {{maininfo.lname |title() }} is {{maininfo.age * 2}} !
          - caption: charlie
            wwbody: >
              {{maininfo.fname |title() }} {{maininfo.lname |title() }} is {{maininfo.age * 3}} !
        __yaml__:
          - &uuid001
            processthis: 1
            template: |
              {% for row in documents_table -%}
              {{- row.wwbody -}}
              {% endfor %}
      '''

      ##
      # rawyaml     =   textwrap.dedent( rawyaml )
      # rawyaml     =   rawyaml.lstrip()

      ##
      ## tmptemplate =   yaml.safe_load( rawyaml )['__yaml__'][0]['template']

      ##
      vout        =   otest.template_render_1stpass(yaml=rawyaml)
      print vout
      pass;

###!}}}
