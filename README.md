# dumbo

## About
Simple python package

## How to install

```
pip install git+https://github.com/rizvand/dumbo.git
```
Install from specific branch

```
pip install git+https://github.com/rizvand/dumbo.git@<branch_name>
```
Ex:
```
pip install git+https://github.com/rizvand/dumbo.git@master
```


## Usage
```
>>> from dumbo.person import RandomPerson
>>> p = RandomPerson()
>>> p.identity()
{'name': 'Derek Moore', 'address': 'Unit 8542 Box 0772\nDPO AE 76016'}
```