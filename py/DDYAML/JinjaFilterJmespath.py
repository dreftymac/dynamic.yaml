### <beg-file_info>
### main:
###   - date: created="Tue Jan 19 22:05:55 2016"
###     last: lastmod="Tue Jan 19 22:05:55 2016"
###     tags:   tags
###     dreftymacid: "funds_cola_handhold"
###     filetype: "yaml"
###     seealso: |
###         *
###     desc: |
###         desc
### <end-file_info>

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### init py
if('python_region'):
      ## init py
      import jmespath
      import os
      import sys

      ##
      from JinjaFilterBase import JinjaFilterBase
      from YamlDerivedBaseRepresenter import YamlDerivedBaseRepresenter      
      # from DataHelperUtils import DataHelperUtils
      # from DataHelperDiceware import DataHelperDiceware

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### new_function_snippet
"""
  def [[%tabstop01:caption]](self,jjinput):
    '''
    ##beg_func_docs
    - caption:      [[%tabstop01]]
      date:         lastmod="[[%tabstop:lastmod]]"
      grp_maj:      grp_maj
      grp_med:      grp_med
      grp_min:      grp_min
      desc:         [[%tabstop:desc]]
      dreftymacid:  [[%tabstop:dreftymacid]]
      detail:  |
        * [[%tabstop:blank]]
      dependencies:
        - [[%tabstop:blank]]
      params:
       - param: jjinput ;; optarity ;; jinja raw input string
    ##end_func_docs
    '''

    ##
    vout = jjinput.[[%tabstop:str]]()

    ##
    try:
      vout = vout
    ##
    except Exception as msg:
      print 'UNEXPECTED TERMINATION [[%tabstop:dreftymacid]] msg@%s'%(msg.[[%tabstop:repr]]())
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)

    ##
    return vout
  ##enddef
"""

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### jinja helper JinjaFilterJmespath
if('python_region'):
###!{{{
###!- caption:  JinjaFilterJmespath
###!  date:     created="Thu Jul 16 13:21:33 2015"
###!  dreftymacid: liver_operas_kneads
###!  goal:     |
###!      set of default jinja filters that come with ddyaml out of the box
###!  result:   |
###!       [[%tabstop:blank]]
###!  tags:     ddyaml, filter, addon, jinja
###!  seealso: |
###!          * [[%tabstop:blank]]
###!  desc: |
###!          Currently assumes jinja2 as the templating engine for ddyaml
###!
###!  wwbody: |
      class JinjaFilterJmespath(JinjaFilterBase):

        def jjmespath_query(self,jjinput,ssquery='*',formatas='yamlpretty'):
          '''
          ##beg_func_docs
          - caption:      jjmespath_query
            date:         lastmod="2016-04-01T16:49:56"
            grp_maj:      jmespath
            grp_med:      query
            grp_min:      mydata
            desc:         desc
            dreftymacid:  murk_urology_poverty
            detail:  |
              * blank
            dependencies:
              - jjdata_formatas
            params:
             - param: jjinput ;; optarity ;; jinja raw input string
          ##end_func_docs
          '''

          ##
          vout    = ''
          #mydata  = {"dataroot":jjinput}
          mydata  = jjinput

          ##
          try:
            vout = jmespath.search(ssquery, mydata)
            if(not 'testing'):
                  print "%s -- %s" % ('mydata',  type(mydata)  )
                  print "%s -- %s" % ('ssquery', type(ssquery) )
                  print "%s -- %s" % ('vout',    type(vout)    )

          ##
          except Exception as msg:
            print 'UNEXPECTED TERMINATION element_flunky_guiding msg@%s'%(msg.repr())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

          ##
          return vout
        ##enddef

      ##endclass
###!}}}
