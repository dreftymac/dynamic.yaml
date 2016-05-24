#! /usr/bin/python
# -*- coding: utf-8 -*-
### <beg-file_info>
### main:
###   - date: created="Wed Dec 30 12:53:38 2015"
###     last: lastmod="Wed Dec 30 12:53:38 2015"
###     tags: tags
###     author: created="dreftymac"
###     dreftymacid: "drawing_verlaine_neck"
###     seealso: |
###         ## mytrybits devlog
###         * href="smartpath://mytrybits/y/tryyaml/dynamicyaml/devlog.txt"
###         * cd /cygdrive/c/sm/docs/mymedia/2014/git/github/dynamic.yaml
###
###         ## local paths
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/app/demo/readme.md"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyamlrunner.py"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/dynamicyaml.py"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/jinjafilterdynamicyaml.py"
###     desc: |
###         TODO_LINK ;; ddyaml todo href="../.private/txt/devlog.txt" find="chain_stifling_is"
###         TODO ;; figure out why ddyaml has such a difficult time parsing myclip files
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
      ## init
      import os
      import sys
      from optparse import OptionParser

      ## local import ;; forget_burial_was::001
      from DDYAML  import  DynamicYAML                 ## href="./DDYAML/DynamicYAML.py"
      from DDYAML  import  JinjaFilterBase             ## href="./DDYAML/JinjaFilterBase.py"
      from DDYAML  import  JinjaFilterDynamicYAML      ## href="./DDYAML/JinjaFilterDynamicYAML.py"
      from DDYAML  import  JinjaFilterJJrun            ## href="./DDYAML/JinjaFilterJJrun.py"
      from DDYAML  import  JinjaFilterJmespath         ## href="./DDYAML/JinjaFilterJmespath.py"
      from DDYAML  import  YamlDerivedBaseRepresenter  ## href="./DDYAML/YamlDerivedBaseRepresenter.py"
      from DDYAML  import  YamlEmbedJinja              ## href="./DDYAML/YamlEmbedJinja.py"
      from DDYAML  import  DataHelperUtils             ## href="./DDYAML/DataHelperUtils.py"
      from DDYAML  import  XmlssBase                   ## href="./DDYAML/XmlssBase.py"
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
###!  		* href="c:/sm/docs/mytrybits/p/trypython2/lab2014/pyjinja/dynamic_yaml.py"
###!  desc: |
###!  		__desc__
###!
###!  dreftymacid: uhuru_vagrant_means
###!
###!  wwbody: |
if (__name__ == "__main__"):

      ### ------------------------------------------------------------------------
      ##  process_commandline_input
      desc   = (
      '''dynamic yaml runner -- see https://github.com/dreftymac/dynamic.yaml
      ''')
      strversion  = 'dynamic yaml runner -- version 20160122.001'
      parser      = OptionParser(description=desc,version=strversion)
    
      ### ********************
      parser.add_option("-f", "--fileinput"
                        ,type="string"
                        ,default=''
                        ,action='store'
                        ,dest="fileinput"
                        ,metavar="<INPUT_FILEPATH>"
                        ,nargs=1
                        ,help="Specify a primary input file containing dynamic yaml."
                        )
      
      parser.add_option("-g", "--globalvar"
                    ,type="string"
                    ,default=[]
                    ,action='append'
                    ,dest="globals"
                    ,metavar="<VARNAME> <VARVALUE>"
                    ,nargs=2
                    ,help="Specify a global variable to make available to all templates."
                    )
    
      ### ********************
      (options, args) = parser.parse_args()
    
      ### ********************
      options_dict = vars(options)
      ##
      if(not 'debugging'):
        print( options_dict )
        # oDumper.pprint( args )
        pass;
      ##;;
    
      ### ------------------------------------------------------------------------
      ##  invoke_ddyaml_runner
      vout    =   ''
      ffpath  =   ''
      oparams =   {}
      ##;;
    
      ##
      try:
        ffpath  =   options_dict["fileinput"]
      except:
        ffpath  =   ""
      ##;;
      
      ## default addon filters ;; forget_burial_was::002
      aaJinjaAddonFilters = [
        JinjaFilterDynamicYAML(),
        JinjaFilterJJrun(),
        JinjaFilterJmespath(),
      ]
      ##;;
    
      ##
      oparams['path']               =   ffpath
      oparams['addonFilters']       =   aaJinjaAddonFilters
      oparams['globals']            =   options_dict['globals']
      #oparams['globals']['ggblank'] =   '__blank__'
      ##;;
    
      ##
      odyna   =   DynamicYAML(oparams)
      vout    =   odyna.ddtransform()
      print vout.encode('utf-8','replace')
      ##;;
### <end-region_testiff_20151230125723>

'''
sample runlines

cd /cygdrive/c/sm/docs/mymedia/2014/git/github/dynamic.yaml/py
./ddyamlrunner.py --file="../app/demo/bare.hello.txt"
./ddyamlrunner.py --file="../app/demo/barebones.globalvar.txt" --globalvar=ggto "World" --globalvar=ggfrom "Homer Simpson"

'''
