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
          
          ## process
          #ffoutzip  =     'ddyaml_output.zip'
          oddyaml   =     DynamicYAML(request.params["txtfile001"])
          vout      =     oddyaml.ddtransform()
          ffout     =     'ddyaml_output.txt'
          open(ffout,'wb').write(vout)
          
          ##
          for ijj,vkk in enumerate(glob.glob('/data/user_files/*')):
            #print "{} : {}".format(ijj, vkk)
            response.addFileOutput("outfile%03d"%(ijj),vkk)
          response.end()
          
      ##
      blockspring.define(block)
###!}}}

