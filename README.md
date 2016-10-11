# Rakuten-Toolbar-Automated

## SETUP
1. Line 11: Fill in Chrome profile path on line 11: `options.add_argument("user-data-dir=PATH")`.     
You can find this by typing `chrome://version/` in your browser.

2. Line 14: Fill in the path to your chrome driver. `(executable_path='DRIVER_PATH', chrome_options=options)`

3. Line 23 & 31: Remove the quotation marks and edit your username `(r"USER")` and password `("PASS")` into it for first run. This is not needed for subsequent runs.

4. Line 34: Fill in the dictionary `dsearch = []` with at least 32 search terms in English/Japanese. Search terms can be repeated. Separate with commas and parse it as a string, for example: `[u"月",u"火"]`.

