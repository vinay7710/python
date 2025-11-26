(# python changes/python.py — Setup & Run)

Description
- Counts how many times the user changed keys while typing a sequence of single-letter key presses.
- The function treats uppercase and lowercase of the same letter as the same key (case-insensitive).

Requirements
- Python 3.8 or newer (no third-party packages required).

Repository files
- Script: `python changes\python.py`

Quick start (PowerShell)
1. Open PowerShell and change to the project directory:

```powershell
cd "C:\Devops\vinay-86S\python\python changes"
```

2. Run the script directly (runs examples if the script has a `__main__` block):

```powershell
python python.py
```

3. Or call the `solution` function from a one-line import (useful for quick checks):

```powershell
python -c "import importlib.util; spec=importlib.util.spec_from_file_location('mod','python.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); print(mod.solution(['W','w','a','A','a','b','B']))"
```

Usage notes
- The current `python.py` contained in the workspace has a known indentation bug where `return changes` is inside the `for` loop — this causes the function to return prematurely. The example usages in the file are also indented inside the function body.
- Recommended minimal fixes:
  - Move `return changes` so it is outside the `for` loop.
  - Add a test harness under `if __name__ == '__main__':` to run example cases when the file is executed directly.

Suggested patch (manual edit)
1. Fix `return` indentation:

```python
	for ch in recording[1:]:
		curr_key = ch.lower()
		if curr_key != prev_key:
			changes += 1
		prev_key = curr_key
	return changes
```

2. Add runnable examples at file bottom:

```python
if __name__ == '__main__':
	example1 = ['W', 'w', 'a', 'A', 'a', 'b', 'B']
	example2 = ['w', 'w', 'a', 'w', 'a']

	print(solution(example1))
	print(solution(example2))
```

Help or next steps
- Want me to apply the minimal fix and add the `__main__` test harness to `python changes\python.py`? I can patch the file and run a quick check locally.

