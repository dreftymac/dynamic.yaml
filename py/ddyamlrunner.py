# -*- coding: utf-8 -*-
### <beg-file_info>
### main:
###   - date: created="Wed Dec 30 12:53:38 2015"
###     last: lastmod="Wed Dec 30 12:53:38 2015"
###     tags: tags
###     author: created="dreftymac"
###     dreftymacid: "drawing_verlaine_neck"
###     seealso: |
###         * href="smartpath://mytrybits/y/tryyaml/dynamicyaml/devlog.txt"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/app/demo/readme.md"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyamlrunner.py"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/dynamicyaml.py"
###         * href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/jinjafilterdynamicyaml.py"
###     desc: |
###         
###         TODO_LINK ;; ddyaml todo href="../.private/txt/devlog.txt" find="chain_stifling_is"
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
      ## local import
      from DDYAML  import  DynamicYAML                 ## href="./DDYAML/DynamicYAML.py"
      from DDYAML  import  JinjaFilterBase             ## href="./DDYAML/JinjaFilterBase.py"
      from DDYAML  import  JinjaFilterDynamicYAML      ## href="./DDYAML/JinjaFilterDynamicYAML.py"
      from DDYAML  import  JinjaFilterJJrun            ## href="./DDYAML/JinjaFilterJJrun.py"
      from DDYAML  import  YamlDerivedBaseRepresenter  ## href="./DDYAML/YamlDerivedBaseRepresenter.py"
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
###!  body: |
      if (__name__ == "__main__"):
        ##
        vout    =   ''
        ffpath  =   "c:/sm/docs/mymedia/2014/git/github/dynamic.yaml/app/demo/demo.topic.excel.txt"
        ffpath  =   "c:/sm/docs/mymedia/2014/git/github/dynamic.yaml/app/demo/barebones.helloworld.yaml.txt"
        ffpath  =   "c:/sm/docs/mymedia/2014/git/github/dynamic.yaml/app/demo/demo.topic.interop.txt"
        ## IMPORTANT  ;; if you have any addon filter classes, add them here ;; viaducts_juiciest_painting
        ## SEEALSO    ;; href="c:/sm/docs/mytrybits/p/trypython2/lab2014/pyjinja/dynamic_yaml.py" find="viaducts_juiciest_painting" 
        aaJinjaAddonFilters = [
          JinjaFilterDynamicYAML(),
          JinjaFilterJJrun(),
        ]
        oparams = {}
        oparams['path']         = ffpath
        oparams['addonFilters'] = aaJinjaAddonFilters
        ##
        odyna   =   DynamicYAML(oparams)
        vout    =   odyna.ddtransform()
        print vout.encode('utf-8','replace')
### <end-region_testiff_20151230125723>
