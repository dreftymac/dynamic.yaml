### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### blockspring_addon
if('python_region'):
###!{{{
###!- caption:  blockspring_addon
###!  date:     created="Thu Jul 16 12:57:02 2015"
###!  goal:     |
###!       support dynamic yaml as a blockspring function
###!  result:   |
###!       __blank__
###!  tags:     __tags__
###!  seealso: |
###!  		* https://open.blockspring.com/dreftymac
###!  desc: |
###!  		__desc__
###!
###!  dreftymacid: vernier_couch_ancients
###!  wwbody: |
      import blockspring
      def block(request, response):
          ## init
          vout    =     ''
          
          ## read upload file
          ffout     =     'ddyaml_output.txt'
          oddyaml   =     DynamicYAML(request.params["txtfile001"])
          vout      =     oddyaml.ddtransform()
          open(ffout,'wb').write(vout)
          response.addFileOutput("outfile",ffout)
          response.end()
          
      ##
      blockspring.define(block)
###!}}}
