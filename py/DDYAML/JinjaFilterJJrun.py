### <beg-file_info>
### main:
###   - date: created="Tue Jan 19 22:05:55 2016"
###     last: lastmod="Tue Jan 19 22:05:55 2016"
###     tags:   tags 
###     dreftymacid:    "funds_cola_handhold"
###     filetype:       "yaml"
###     seealso: |
###         *
###     desc: |
###         desc
### <end-file_info>

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### init py
if('python_region'):
      ## init py
      import os
      import subprocess
      
      ##
      from JinjaFilterBase import JinjaFilterBase
      from DataHelperUtils import DataHelperUtils
      from DataHelperDiceware import DataHelperDiceware

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
### jinja helper JinjaFilterJJrun
if('python_region'):
###!{{{
###!- caption:  JinjaFilterJJrun
###!  date:     created="Thu Jul 16 13:21:33 2015"
###!  dreftymacid: glint_unjam_cheapen
###!  goal:     |
###!      set of default jinja filters that come with ddyaml out of the box
###!  result:   |
###!       __blank__
###!  tags:     ddyaml, filter, addon, jinja
###!  seealso: |
###!          * __blank__
###!  desc: |
###!          Currently assumes jinja2 as the templating engine for ddyaml
###!
###!
###!          
###!  wwbody: |
      class JinjaFilterJJrun(JinjaFilterBase):

        ### ------------------------------------------------------------------------
        ### begin_: 

        def jjrun_popen(self,jjinput,scmd=''):
          '''
          ##beg_func_docs
          - caption:      jjrun_popen
            date:         lastmod="2016-01-04T16:35:22"
            grp_maj:      python
            grp_med:      interop
            grp_min:      popen
            desc:         run a command using python's os.popen command
            dreftymacid:  charcoal_endanger_finger
            example:
              - 
            seealso:
              - href="smartpath://mytrybits/p/trypython2/lab2014/py/barebones_interop.py" find="sank_ceram_trim"
            detail: |
              __detail__
            dependencies:
                - import os
            params:
             - param: jjinput   ;; optional ;; command input
             - param: scmd      ;; optional ;; command input if jjinput is blank
          ##end_func_docs
          '''

          ##
          vout  = ''
          if(jjinput):
            scmd  =  jjinput
          ##;;

          ##
          try:
              # scmd = [
              #   ''
              #   ,'c:/programs/cygwin/bin/mintty.exe'
              #   ,'--exec c:/programs/cygwin/bin/bash --login -i'
              #   ,'-c "find /cygdrive/c/sm/docs/mydaydirs/2015"'
              # ]
              # scmd  =   " ".join(scmd)
              os.popen(scmd)
          except Exception as msg:
            vout = ''
            print 'EXCEPTION charcoal_endanger_finger msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;
          
          ##
          return vout
        ##enddef
        
        def jjrun_firefox(self,jjinput
                          ,srunwebl='https://www.google.com'
                          ,srunargs='-new-tab'
                          ,srunpath=r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
                          ):
          '''
          ##beg_func_docs
          - caption:      jjrun_firefox
            date:         lastmod="2016-01-19T21:08:04"
            grp_maj:      python  
            grp_med:      interop
            grp_min:      firefox
            desc:         run firefox with optional args
            dreftymacid:  venatic_impure_forego
            seealso: 
              - href="https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options?redirectlocale=en-US&redirectslug=Command_Line_Options"
              - href="../../../app/demo/demo.topic.interop.txt"
            detail:  |
              * __blank__
            dependencies:
              - __blank__
            params:
             - param: jjinput ;; ignored ;; jinja raw input string
             - param: srunwebl ;; optional ;; target weblink
             - param: srunargs ;; optional ;; cmdline flags
             - param: srunpath ;; optional ;; path to firefox executable
          ##end_func_docs
          '''
        
          ##
          vout = jjinput.__str__()
        
          ##
          try:
            subprocess.call([srunpath,srunargs,srunwebl])
          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION __dreftymacid__ msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
        
          ##
          return vout
        ##enddef

      ##endclass
###!}}}
