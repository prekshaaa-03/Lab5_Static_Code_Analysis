# Reflection – Static Code Analysis Lab

### 1. What issues did the tools identify?
- **Pylint**: missing docstrings, mutable default argument, file-handling warnings, unused import  
- **Bandit**: use of `eval()` (security risk), bare `except:` (bad practice)  
- **Flake8**: spacing, unused import, and bare `except`  
These matched the runtime bug observed earlier.

### 2. Which issues did you fix first and why?
I prioritized the high/medium-severity issues first:
- Removed `eval()` (security)  
- Replaced bare `except:`  
- Fixed mutable default argument  
- Updated file-handling with `with open()`  

These affected safety and reliability the most.

### 3. How did you verify that your fixes worked?
After fixes I reran:
pylint inventory_system.py
bandit -r inventory_system.py
flake8 inventory_system.py

- Bandit reported **no high/medium issues**  
- Pylint score improved from **4.8 → 9.4 / 10**  
- Flake8 showed only minor formatting notes  
- Program executed successfully with no runtime errors

### 4. What was easiest and hardest to fix?
- **Easiest:** removing `eval()` and changing file-handling.  
- **Hardest:** adding input validation and understanding the mutable default argument behaviour.

### 5. Any false positives or extra insights?
Flake8 spacing/naming warnings were stylistic rather than functional.  
Static tools complement testing by catching hidden reliability and security problems early.

### 6. How can you use these tools in real projects?
Integrate Pylint, Bandit, and Flake8 into CI (GitHub Actions or pre-commit hooks) so every push automatically checks code quality and security.

> After fixes, all three tools produced clean or near-clean reports—confirming the code is now safe, consistent, and maintainable.
