# dynamic.yaml

> YAML-based data transformations - live demo on [blockspring](https://open.blockspring.com/dreftymac/2dc5183fbb912fc3c553fc14bbe15e43).

## Overview

DynamicYaml is a general-purpose, fully-extensible transformation engine for YAML.

The design philosophy of this project:

* enhance YAML by adding the best features from string template tools
    * (currently using python/yaml and python/jinja2)
* support for advanced features and an unlimited range of outputs
* easy extensibility and plugin support

## Live demo (blockspring.com)

Try it now with [blockspring](https://open.blockspring.com/dreftymac/2dc5183fbb912fc3c553fc14bbe15e43).

* **Step**: save the following to a text file on your machine (e.g., helloworld.yaml)
```
dataroot:
  event:
    overview:   Welcome to dynamic yaml!
    date:       20150716.1732
    desc:       A simple introduction to dynamic yaml.
    
  people:
    - fullname:     Bregiono Buckridge
      email:        bregiono@gmail.com
      id:           1
      url:          https://example.com/bregiono
      regioncc:     region001
      
    - fullname:     Antonina Daugherty
      email:        antonina@gmail.com
      id:           1
      url:          https://example.com/antonina
      regioncc:     region001
      
    - fullname:     Preston Boyer
      email:        preston@gmail.com
      id:           3
      url:          https://example.com/preston
      regioncc:     region002
    
__yaml__:
  - template: |
      {{ dataroot |jjdata_formatas('jsonpretty') }}
```

* **Step**: Upload the file to [blockspring](https://open.blockspring.com/dreftymac/2dc5183fbb912fc3c553fc14bbe15e43) and choose "Run"

* **Step**: Use the data transformation results for anything you want. All done!

## See also

* **"./research.md"** ;; background-research and related links for this project
    * [research.md](https://github.com/dreftymac/dynamic.yaml/blob/master/research.md)
    



