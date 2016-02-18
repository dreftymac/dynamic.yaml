### <beg-file_info>
### main:
###   - date: created="Thu Feb 11 12:06:50 2016"
###     last: lastmod="Thu Feb 11 12:06:50 2016"
###     tags: yaml, jinja2, embed, preprocess
###     dreftymacid: "misery_veratrum_magazine"
###     filetype: "yaml"
###     seealso: |
###         * href="./zzscratchtest.py"
###     desc: |
###         process ordinary YAML with embedded jinja2
###         return ordinary YAML with the jinja2 interpolated
### <end-file_info>

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### init py
if('python_region'):
      ## init py
      import jinja2
      import os
      import sys
      import textwrap
      import yaml
      pass;

### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### YamlEmbedJinja
if('python_region'):
###!{{{
###!- caption:  YamlEmbedJinja
###!  date:     created="2016-02-11T12:08:40"
###!  tags:     yaml, jinja, embedded, preprocess
###!  seealso: |
###!      * __blank__
###!  desc: |
###!      process ordinary YAML with embedded jinja2
###!      return output with the jinja2 interpolated
###!  dreftymacid: meatiest_awful_humid
###!  wwbody: |

      class YamlEmbedJinja(object):
        """
        process
        """

        ##
        def __init__(self,**kwargs):

          ## init myoptions
          self.myoptions = {}
          self.myoptions['ddyaml_string_enddata']  = '__yaml__'
          self.myoptions['ddyaml_string_configs']  = '__yamlconfig__'
              ## TODO: add support for hand-entered configs
          ##
          for tmpname, tmpvarr in kwargs.items():
              self.myoptions[tmpname] = tmpvarr
          ##
          self.my_ddyaml_string_enddata   = self.myoptions['ddyaml_string_enddata']
          self.my_ddyaml_string_configs   = self.myoptions['ddyaml_string_configs']
          ##;;

          ## init jinja Environment
          self.Environment = jinja2.Environment(
            extensions=[
              'jinja2.ext.do'
              ,'jinja2.ext.loopcontrols'
              ]
            #,finalize=self.oenv_finalize
            )
          self.oenv = self.Environment
          ##;;

          ## init yamlregions
          self.yamlregions = {}
          self.yamlregions['primary']  = ''   ##;; region_primary ;; either plain yaml or yaml+embedded placeholders
          self.yamlregions['dynamic']  = ''   ##;; region_dynamic ;; processing blocks that can output anything
          ## self.yamlregions['configs']  = ''   ##;; region_configs ;; configuration settings that can be specified by hand
          ## DEPRECATED ;; 2016-02-12T07:47:11 ;; instead devise a way to handle configs in the dynamic yaml region 
          ##;;
        ##enddef

        # ## TODO ;; refactor this to generic output spitter of function docs or whatever
        # def spitparams(self):
        #   return self.myoptions
        # ##enddef

        def split_into_sections_ddyaml(self,**kwargs):
          ## init
          args          =   {}
          args['yaml']        =   ''    ## rawyaml ;; raw input yaml string
          args['splitby']     =   ''    ## splitby ;; string token to split on
          ##
          for tmpname, tmpvarr in kwargs.items():
            args[tmpname] = tmpvarr
          ##
          data_hasnt_failed   =   True
          rawyaml             =   args['yaml']
          splitby             =   args['splitby']
          ##;;

          ## return
          return  rawyaml.split(splitby)
        ##enddef

        # ## TODO ;; improve this with custom raise exceptions instead of returning True/False
        # def validate_iswellformed_ddyaml(self,**kwargs):
        #   ## init
        #   args          =   {}
        #   args['yaml']  =   ''    ## rawyaml ;; raw input yaml string
        #   ##
        #   for tmpname, tmpvarr in kwargs.items():
        #     args[tmpname] = tmpvarr
        #   ##
        #   data_hasnt_failed   =   True
        #   rawyaml             =   args['yaml']
        #   ##;;
        # 
        #   ## can have no more than one of these tokens in the sourceinput
        #   ## count the number of sections that result from splitting on these tokens
        #   ## if more than 2 sections result, we have more than one token
        #   sctn_enddata      =   self.split_into_sections_ddyaml(yaml=rawyaml,splitby=self.my_ddyaml_string_enddata)
        #   if(sctn_enddata.__len__() > 2):
        #     data_hasnt_failed = False
        #   ##
        #   sctn_yamlconfigs  =   self.split_into_sections_ddyaml(yaml=rawyaml,splitby=self.my_ddyaml_string_configs)
        #   if(sctn_yamlconfigs.__len__() > 2):
        #     data_hasnt_failed = False
        #   ##;;
        # 
        #   ## return
        #   return data_hasnt_failed
        # ##enddef

        ##
        def template_render_1stpass(self,**kwargs):
          ### <beg-function_docs>
          ###   - date: created="Thu Feb 11 13:25:28 2016"
          ###     last: lastmod="Thu Feb 11 13:25:28 2016"
          ###     funcname: "template_render_1stpass"
          ###     funcdesc: |
          ###           process the yamlregions yamlregions_primary section
          ###           allows for embedded jinja inside source YAML data
          ###
          ###           processing region_primary section is brittle because interpolating
          ###           embedded jinja has potential of breaking the yaml syntax
          ###     funcparams:
          ###          - yaml     ;; string ;; raw yaml input with potentially embedded jinja
          ###     funcreturns:
          ###          - raw yaml string ;; yaml as a raw string
          ###     funcdetails: |
          ###          __funcdetails__
          ###     dreftymacid: blast_tinworks_reply
          ###     tags: __tags__
          ###     seealso: |
          ###         *
          ### <end-function_docs>
          
          ## init
          args = {}
          for tmpname, tmpvarr in kwargs.items():
            args[tmpname] =   tmpvarr
          data_firstpass  =   None
          raws_firstpass  =   ''
          vout            =   ''
          splitby         =   self.my_ddyaml_string_enddata          
          ##;;          
                  
          ##trycatch ;; init_params
          try:
            ## rawyaml init
            rawyaml   =   args['yaml']
            rawyaml   =   textwrap.dedent( rawyaml )
            rawyaml   =   rawyaml.lstrip()
            regions   =   rawyaml.split(splitby)
            ## 
            if (regions.__len__() == 2):
              self.yamlregions['primary'] = textwrap.dedent(regions[0]).lstrip()
              self.yamlregions['dynamic'] = ("%s%s")%(splitby,textwrap.dedent(regions[1]).lstrip())
            if (regions.__len__() == 1):
              self.yamlregions['primary'] = textwrap.dedent(regions[0]).lstrip()
              #self.yamlregions['dynamic'] = ("%s%s%s")%("\n\n",splitby,"\n")
              self.yamlregions['dynamic'] = ''
            ## debug print
            # print self.yamlregions['primary']
            # print self.yamlregions['dynamic']
            # exit()
          except Exception as msg:
            print '## EXCEPTION hangs_dali_hawker_000 ( missing argument <yaml>? ;; yaml possibly_broken_syntax? ) msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;                  
          
          ##trycatch ;; firstpass
          try:
            ## firstpass yaml data load
            data_firstpass = yaml.safe_load( rawyaml )
            data_firstpass.pop(self.my_ddyaml_string_enddata, None) ## remove region_dynamic portion of ddyaml workbook

            ## pprint
            # import pprint
            # oDumper = pprint.PrettyPrinter(indent=4);
            # oDumper.pprint( data_firstpass )            
            
            ## first-pass template processing
            proc_template   =   self.oenv.from_string( self.yamlregions['primary'] )
            vout            =   proc_template.render( data_firstpass )
            vout            =   "%s\n%s"%(vout,self.yamlregions['dynamic'])
            ##print vout
            ##;;
          except Exception as msg:
            print '## EXCEPTION waveland_wavelike__001 ( yaml possibly_broken_syntax? ) msg@%s'%(msg.__repr__())
            print "\n".join(["## %s"%(vxx) for vxx in rawyaml.splitlines() ])
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;          
          
          ## return
          return vout
        ##enddef
        
        ##
        def template_render_2pass(self,**kwargs):
          ### <beg-function_docs>
          ###   - date: created="Thu Feb 11 13:25:28 2016"
          ###     last: lastmod="Thu Feb 11 13:25:28 2016"
          ###     funcname: "template_render_2pass"
          ###     funcdesc: |
          ###           perform two-pass processing of raw YAML
          ###           allows for embedded jinja inside source YAML data
          ###           * first pass  == placeholder substitution in YAML sourcedata  (region_primary)
          ###           * second pass == placeholder substitution in YAML enddata     (region_dynamic)
          ###     funcparams:
          ###          - yaml     ;; string ;; raw yaml input with potentially embedded jinja
          ###          - template ;; string ;; the template to apply on the secndpass processing step
          ###     funcreturns:
          ###          - __returntype__ ;; __returndesc__
          ###     funcdetails: |
          ###          __funcdetails__
          ###     dreftymacid: blast_tinworks_reply
          ###     tags: __tags__
          ###     seealso: |
          ###         *
          ### <end-function_docs>

          ## init
          args = {}
          for tmpname, tmpvarr in kwargs.items():
            args[tmpname] =   tmpvarr
          data_firstpass  =   None
          data_secndpass  =   None
          vout            =   ''
          ##;;

          ##trycatch ;; init_params
          try:
            ## rawyaml load
            rawyaml   =   args['yaml']
            rawyaml   =   textwrap.dedent( rawyaml )
            rawyaml   =   rawyaml.lstrip()
          except Exception as msg:
            print '## EXCEPTION waveland_wavelike__000 ( missing argument <yaml>? ;; yaml possibly_broken_syntax? ) msg@%s'%(msg.__repr__())
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ##trycatch ;; firstpass
          try:
            ## firstpass data load
            data_firstpass = yaml.safe_load( rawyaml )
            data_firstpass.pop(self.my_ddyaml_string_enddata, None) ## remove ddyaml_string_enddata portion of ddyaml workbook
            data_firstpass.pop(self.my_ddyaml_string_configs, None) ## remove ddyaml_string_configs portion of ddyaml workbook
            #print data_firstpass
            #exit()

            ## pprint
            # import pprint
            # oDumper = pprint.PrettyPrinter(indent=4);
            # oDumper.pprint( data_firstpass )            
            
            ## first-pass template processing
            proc_template   =   self.oenv.from_string( yaml.safe_dump(data_firstpass) )
            vout            =   proc_template.render( data_firstpass )
            ##print vout
            ##;;
          except Exception as msg:
            print '## EXCEPTION waveland_wavelike__001 ( yaml possibly_broken_syntax? ) msg@%s'%(msg.__repr__())
            print "\n".join(["## %s"%(vxx) for vxx in rawyaml.splitlines() ])
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          # ##trycatch ;; secndpass
          # try:
          #   ## secndpass data load
          #   data_secndpass  =   yaml.safe_load( vout )
          #   ## secndpass template processing
          #   proc_template   =   self.oenv.from_string( args['template'] )
          #   vout            =   proc_template.render( data_secndpass )
          #   ##;;
          # except Exception as msg:
          #   print '## EXCEPTION waveland_wavelike__002 ( yaml possibly_broken_syntax? ) msg@%s'%(msg.__repr__())
          #   print "\n".join(["## %s"%(vxx) for vxx in vout.splitlines() ])
          #   exc_type, exc_obj, exc_tb = sys.exc_info()
          #   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
          #   print(exc_type, fname, exc_tb.tb_lineno)
          ##;;

          ## return
          return vout
        ##enddef

      ##endclass

###!}}}
