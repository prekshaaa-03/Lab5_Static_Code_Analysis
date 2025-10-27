# Issues Identified and Fixes

| Issue | Type (Bug / Style / Security) | Tool | Line(s) | Description | Fix Applied |
|-------|-------------------------------|-------|-----------|--------------|--------------|
| Bare `except:` hides all errors | Bug / Security | Bandit (B110), Flake8 (E722), Pylint (W0702) | 19 | Broad `except` silently ignores exceptions | Replaced with `except KeyError` and `except TypeError` |
| Use of `eval()` function | Security | Bandit (B307), Pylint (W0123) | 59 | `eval()` executes arbitrary code | Removed the line entirely |
| Mutable default argument (`logs=[]`) | Bug | Pylint (W0102) | 8 | List reused across function calls | Changed to `logs=None` and initialized inside |
| File open without `with`/encoding | Bug / Style | Pylint (R1732, W1514) | 26, 32 | Possible file-handle leak and encoding issues | Used `with open(..., encoding="utf-8")` |
| Unused import `logging` | Style | Pylint (W0611), Flake8 (F401) | 2 | `logging` imported but never used | Configured and used logging for messages |
| Missing docstrings | Style | Pylint (C0114, C0116) | All functions | Functions lacked documentation | Added docstrings to each function |

>  All high and medium severity issues were fixed and verified using Pylint, Bandit, and Flake8.
