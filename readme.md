# dynamic.yaml

> YAML-based data transformations -- live demo on [blockspring](https://open.blockspring.com/dreftymac/2dc5183fbb912fc3c553fc14bbe15e43) try it now.

## Live Demo

Try it now with [blockspring](https://open.blockspring.com/dreftymac/2dc5183fbb912fc3c553fc14bbe15e43)!

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

* **Step**: Use the data transformation results for anything you want. DONE.

## See also

* **"./research.md"** ;; background-research and related links for this project
    * [research.md](https://github.com/dreftymac/dynamic.yaml/blob/master/research.md)
* **"./cookiecutter.yaml.txt"** ;; links to template-based project generation tools from cookiecutter
    * [cookiecutter project](https://github.com/audreyr/cookiecutter)
    * [cookiecutter.yaml.txt](https://github.com/dreftymac/dynamic.yaml/blob/master/cookiecutter.yaml.txt)

