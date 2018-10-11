# PyCalc

## Usage

On linux, you can install pycalc with
```shell
make install
```

or, if python 2 is desired,
```shell
make install-py2
```

Otherwise, run
```shell
python -i pycalc.py
```

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
