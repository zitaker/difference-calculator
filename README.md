### Hexlet tests and linter status:

[![Actions Status](https://github.com/zitaker/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/zitaker/python-project-50/actions)
[![Actions my](https://github.com/zitaker/python-project-50/workflows/main/badge.svg)](https://github.com/zitaker/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1871fbf00e66f9f7fca4/maintainability)](https://codeclimate.com/github/zitaker/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/eb547455cfdf164b2ef8/test_coverage)](https://codeclimate.com/github/zitaker/python-project-50/test_coverage)  

## Difference Calculator  

Opportunities:  
1. Support for different input formats: YAML (YML), JSON.
2. Generating reports in the form of:
   * Recursive comparison.
   * Plain format.
   * Json format.

How to use:  
```gendiff path_first_file.(json, yaml, yml) path_ second_file.(json, yaml, yml) --format (stylish, plain, json)```

Help output, arguments and options  
https://asciinema.org/a/6ZXLo2VSle3HgE2gGJpvolUAZ  
```poetry run gendiff -h```  
```poetry run gendiff -f```

Recursive comparison  
https://asciinema.org/a/aU70glJGeG9IGREtMLWCHdkkq  
```gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml --format stylish```  

Plain format  
https://asciinema.org/a/CvRgWFtMMFstS3YSFgjs5kw3e  
```gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml --format plain```  

Json format  
https://asciinema.org/a/zSZE7TyPU0nHB212wC03WSbaD
```gendiff tests/fixtures/filepath1.yaml tests/fixtures/filepath2.yaml --format json```  
