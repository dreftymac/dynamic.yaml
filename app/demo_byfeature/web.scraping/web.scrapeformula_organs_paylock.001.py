### <beg-file_info>
### main:
###   - date: created="Thu Mar 17 17:32:46 2016"
###     last: lastmod="Thu Mar 17 17:32:46 2016"
###     tags:   url, requests, http, web, scraping, bsoup,
###     author: created="__author__"
###     dreftymacid: "hornet_krause_blinds"
###     filetype: "ddyaml"
###     seealso: |
###         *
###     desc: |
###         * demo web crawling and scraping
### <end-file_info>
## href="smartpath://mytrybits/y/tryyaml/dynamicyaml/devlog.txt"
## href="smartpath://mymedia/2014/git/github/dynamic.yaml/app/demo/readme.md"
## href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyamlrunner.py"
## href="smartpath://mymedia/2014/git/github/dynamic.yaml/py/ddyaml/jinjafilterdynamicyaml.py"

links_table:
  - { "site":  "http://www.example.com",   }

__yaml__:

  - &uuid001
    caption:      web.scrapeformula_organs_paylock
    desc:  |
      * example using scrapeformula_organs_paylock formula
    processthis:  1
    uuid:         uuid001
    template: |
      ### ------------------------------------------------------------------------
      ### jjurl_request
      ### jjhtml_findall
      {% set ttfindtag = 'p'  -%}
      {% for row in links_table -%}
      {%- set ttlist =  ''|jjurl_request(row.site)
        |jjhtml_findall(ttfindtag)
       -%}
      {% for item in ttlist -%}
      {{ item
          |jjsplit('.')
          |jjlistget(0)
          |jjsplit('>')
          |jjlistget(1)
          }}
      {% endfor %}
      {% endfor %}
