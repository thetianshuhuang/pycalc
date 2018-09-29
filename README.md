# PyCalc

## Usage

Run
```shell
python -i pycalc.py
```

or, for linux, just
```shell
./pycalc
```

(You may need to ```chmod +x pycalc.sh``` to run the shell script.)

## Configuration

Edit ```config.py``` to add more modules to import on startup.

```
{
    "name": name of module,
    "namespace": name to import as; if None, the module is imported as *
        (directly to global namespace)
    "config": configuration options to pass to the _init method of the module
        (optional)
}
```
