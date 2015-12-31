### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### XmlssBase
if('python_region'):
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
      
### @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
### XmlssBase
if('python_region'):
  class XmlssBase:
    """
    ### <beg-func_docs>
    ### main:
    ###   - date: created="Wed Dec 30 09:41:06 2015"
    ###     last: lastmod="Wed Dec 30 09:41:06 2015"
    ###     tags: tags
    ###     dreftymacid: "agents_bertha_vague"
    ###     seealso: |
    ###         * href="smartpath://mytrybits/p/trypython2/lab2014/xml/xmlssbase.py"
    ###     desc: |
    ###         2003 msft xmlspreadsheet format
    ### <end-func_docs>
    """

    ##
    def myxmlss_head(self,oparams={}):
      """
      xmlss standard header

      xlauthor    = oparams.get('xlauthor','Valued Customer')
      created   = oparams.get('created',(time.strftime("%Y-%m-%dT%H:%M:%SZ")))
      lastmod   = oparams.get('lastmod',(time.strftime("%Y-%m-%dT%H:%M:%SZ")))
      """
      ## dictionary default values ;; sunrise_crunch_hoax
      xlauthor  = oparams.get('xlauthor','Valued Customer')
      created   = oparams.get('created',(time.strftime("%Y-%m-%dT%H:%M:%SZ")))
      lastmod   = oparams.get('lastmod',(time.strftime("%Y-%m-%dT%H:%M:%SZ")))
      ##
      vout = '''
      <?xml version="1.0"?>
      <?mso-application progid="Excel.Sheet"?>
      <Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
        xmlns:o="urn:schemas-microsoft-com:office:office"
        xmlns:x="urn:schemas-microsoft-com:office:excel"
        xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
        xmlns:html="http://www.w3.org/TR/REC-html40">
       <DocumentProperties xmlns="urn:schemas-microsoft-com:office:office">
        <Author>'''+xlauthor+'''</Author>
        <LastAuthor>'''+xlauthor+'''</LastAuthor>
        <Created>'''+created+'''</Created>
        <LastSaved>'''+lastmod+'''</LastSaved>
        <Version>15.00</Version>
       </DocumentProperties>
       <OfficeDocumentSettings xmlns="urn:schemas-microsoft-com:office:office">
        <AllowPNG/>
       </OfficeDocumentSettings>
       <ExcelWorkbook xmlns="urn:schemas-microsoft-com:office:excel">
        <WindowHeight>11565</WindowHeight>
        <WindowWidth>22035</WindowWidth>
        <WindowTopX>6090</WindowTopX>
        <WindowTopY>30</WindowTopY>
        <ProtectStructure>False</ProtectStructure>
        <ProtectWindows>False</ProtectWindows>
       </ExcelWorkbook>
        <Styles>
         <Style ss:ID="Default" ss:Name="Normal">
          <Alignment ss:Vertical="Bottom"/>
          <Borders/>
          <Font ss:FontName="Calibri" x:Family="Swiss" ss:Size="11" ss:Color="#000000"/>
          <Interior/>
          <NumberFormat/>
          <Protection/>
         </Style>
         <Style ss:ID="s62">
          <Borders>
           <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1"/>
           <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1"/>
           <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1"/>
           <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1"/>
          </Borders>
          <Interior ss:Color="#FFFF00" ss:Pattern="Solid"/>
         </Style>
         <Style ss:ID="s63">
          <NumberFormat ss:Format="Short Date"/>
         </Style>
        </Styles>
      '''
      ##;;

      ##
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef

    ##
    def myxmlss_footer(self,oparams={}):
      """
      xmlss standard footer
      """
      ##
      vout = '''
       </Workbook>
      '''
      ##
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef

    ##
    def myxmlss_headerrow(self,oparams={}):
      """
      xmlss header row (first row xlfieldnames)
      """

      ##
      xlfieldnames    =   oparams.get('xlfieldnames',[])
      sstemp    =   ''
      vout      =   ''
      ##;;

      ##
      for fld in xlfieldnames:
        sstemp += """<Cell><Data ss:Type="String">"""+fld+"""</Data></Cell>"""
      ##
      vout = '''
      <!-- -->
      <Row ss:StyleID="s62">
       '''+sstemp+'''
      </Row>
      '''
      ##;;

      ##
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef

    ##
    def myxmlss_worksheet(self,oparams={}):
      """
      output worksheet
      """

      ## init
      mtt_fldcount = (oparams["data"][0].__len__())
      mtt_rowcount = (oparams["data"].__len__()+1)
      ##;;

      ## init
      vout = ('''
      <Worksheet ss:Name="'''+oparams['xlsheetname']+'''">
      <Table
        ss:ExpandedColumnCount="'''+str(mtt_fldcount)+'''"
        ss:ExpandedRowCount="'''+str(mtt_rowcount)+'''"
        x:FullColumns="1"
        x:FullRows="1"
        ss:DefaultRowHeight="15">
        
        '''+  self.myxmlss_headerrow(oparams) +'''

        '''+  self.myxmlss_datarow(oparams)   +'''

      </Table>
      '''+self.myxmlss_wks_freezepane(oparams)+'''
      </Worksheet>
      ''')
      ##;;

      ## return
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef

    ##
    def myxmlss_wks_freezepane(self,oparams={}):
      """
      xmlss standard footer
      """
      ##
      vout = '''
        <WorksheetOptions xmlns="urn:schemas-microsoft-com:office:excel">
         <Unsynced/>
         <Selected/>
         <FreezePanes/>
         <FrozenNoSplit/>
         <SplitHorizontal>1</SplitHorizontal>
         <TopRowBottomPane>1</TopRowBottomPane>
         <ActivePane>2</ActivePane>
         <Panes>
          <Pane>
           <Number>3</Number>
          </Pane>
          <Pane>
           <Number>2</Number>
           <ActiveRow>0</ActiveRow>
           <RangeSelection>R1</RangeSelection>
          </Pane>
         </Panes>
         <ProtectObjects>False</ProtectObjects>
         <ProtectScenarios>False</ProtectScenarios>
        </WorksheetOptions>
      '''
      ##
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef

    ##
    def myxmlss_datarow(self,oparams={}):
      """
      output worksheet
      """

      ## init
      vout = ''
      mtt_fldcount = oparams['xlfieldnames'].__len__()
      mtt_rowcount = oparams['data'].__len__()
      ##;;

      ## iterate
      for row in oparams["data"]:
        vout += ('''
        <Row>
        ''')
        for ixx, name in enumerate(oparams['xlfieldnames']):
          ###
          row['cellvalue']  =   row[name]
          row['celltype']   =   oparams['xlfieldtypes'][ixx]
          ###
          vout += self.myxmlss_datacell(row)
          ###;
        vout += ('''
        </Row>
        ''')
      ##;;
        # <Cell><Data ss:Type="String">b</Data></Cell>
        # <Cell><Data ss:Type="Number">02</Data></Cell>
        # <Cell><Data ss:Type="Number">7.4</Data></Cell>
      ##;;

      ## return
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef

    ##
    def myxmlss_datacell(self,oparams={}):
      """
      xmlss data cell
      """

      ##
      cellvalue = oparams.get('cellvalue','')
      celltype  = oparams.get('celltype','TEXT')
      created   = oparams.get('created',(time.strftime("%Y-%m-%dT%H:%M:%SZ")))
      lastmod   = oparams.get('lastmod',(time.strftime("%Y-%m-%dT%H:%M:%SZ")))
      ##;;

      ##
      celltype            = celltype.lower()
      typemap             = {}
      typemap['text']     = { 'cellpart':'' , 'typepart':'String' }
      typemap['int']      = { 'cellpart':'' , 'typepart':'Number' }
      typemap['number']   = { 'cellpart':'' , 'typepart':'Number' }
      typemap['float']    = { 'cellpart':'' , 'typepart':'Number' }
      typemap['date']     = { 'cellpart':' ss:StyleID="s63" ' , 'typepart':'DateTime' }
      typemap['string']   = typemap['text']
      thistype = typemap.get(celltype,'text')
      ##
      vout = '''
      <Cell'''+str(thistype['cellpart'])+'''><Data ss:Type="'''+str(thistype['typepart'])+'''">'''+str(cellvalue)+'''</Data></Cell>
      '''
      ##;;

      ##
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef

    ##
    def myxmlss_gen_metadata(self,oparams={}):
      """
      auto-generate-metadata
      """
      
      ##
      ddparams  = {}
      ddparams['xlauthor']        = 'nobody@example.com'
      ddparams['xlsheetname']     = 'sheet01'
      ddparams['xlfieldnames']    = sorted(oparams['data'][0].keys())
      ddparams['xlfieldtypes']    = ["text"] * oparams['data'][0].keys().__len__()
      oparams.update(ddparams)
      ##;;

      ## return
      vout = oparams
      return vout
    ##enddef
    
    ##
    def myxmlss_wellform_metadata(self,oparams={}):
      """
      check for non-well-formed metadata and fix if necessary
      """      
      ##
      try:
        oparams['xlauthor']        = oparams['xlauthor']
        oparams['xlsheetname']     = oparams['xlsheetname']
        oparams['xlfieldnames']    = oparams['xlfieldnames']
        oparams['xlfieldtypes']    = oparams['xlfieldtypes']
      except:
        oparams = self.myxmlss_gen_metadata(oparams)
      ##;;

      ## return
      vout = oparams
      return vout
    ##enddef    

    ##
    def tostring(self,oparams={}):
      """
      xmlss standard footer
      """
      oparams   = self.myxmlss_wellform_metadata(oparams)
      ##
      vout = (""
        + self.myxmlss_head(oparams)
        + self.myxmlss_worksheet(oparams)
        + self.myxmlss_footer(oparams)
        + ""
      )
      ##;;

      ## return
      vout = textwrap.dedent(vout).strip()
      return vout
    ##enddef
  ##endclass
